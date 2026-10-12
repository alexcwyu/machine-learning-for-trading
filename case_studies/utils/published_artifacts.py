"""Lossless publication storage; consumers receive verified canonical regular files.

Publication roots contain physical parts. Only copied, owned runtime/staging trees
are materialized. Canonical byte identity remains the original writer's identity.
"""

from __future__ import annotations

import hashlib
import json
import os
import shutil
import tempfile
from collections.abc import Iterator
from contextlib import contextmanager
from pathlib import Path

import polars as pl

from .artifact_digest import _PARQUET_WRITE_SETTINGS

MANIFEST_NAME = "published-parquet.json"
MAX_BYTES = 90 * 1024 * 1024


def file_sha256(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as source:
        for block in iter(lambda: source.read(1 << 20), b""):
            digest.update(block)
    return digest.hexdigest()


def _schema(frame: pl.DataFrame) -> list[list[str]]:
    return [[name, str(dtype)] for name, dtype in frame.schema.items()]


def is_published_artifact(path: Path) -> bool:
    return path.is_dir() and (path / MANIFEST_NAME).exists()


def _manifest(path: Path) -> dict:
    if path.is_symlink() or (path / MANIFEST_NAME).is_symlink():
        raise ValueError(f"Publication dataset/manifest must not be a symlink: {path}")
    record = json.loads((path / MANIFEST_NAME).read_text())
    if (
        not isinstance(record, dict)
        or record.get("format") != "ml4t-published-parquet"
        or type(record.get("version")) is not int
        or record["version"] != 1
    ):
        raise ValueError(f"Unsupported publication manifest: {path}")
    if record.get("logical_filename") != path.name:
        raise ValueError(f"Publication logical filename differs: {path}")
    limit = record.get("max_part_bytes")
    if type(limit) is not int or not 0 < limit <= MAX_BYTES:
        raise ValueError(f"Invalid physical part ceiling: {path}")
    for field in ("canonical_bytes", "rows"):
        if type(record.get(field)) is not int or record[field] < 0:
            raise ValueError(f"Invalid manifest {field}: {path}")
    if not isinstance(record.get("schema"), list):
        raise ValueError(f"Invalid manifest schema: {path}")
    parts = record.get("parts")
    if not isinstance(parts, list) or not parts:
        raise ValueError(f"No ordered publication parts: {path}")
    names = []
    for index, part in enumerate(parts):
        if not isinstance(part, dict) or part.get("name") != f"part-{index:05d}.parquet":
            raise ValueError(f"Invalid/duplicate/unordered part filename: {path}")
        name = part["name"]
        names.append(name)
        candidate = path / name
        if (
            candidate.is_symlink()
            or not candidate.is_file()
            or candidate.resolve().parent != path.resolve()
        ):
            raise ValueError(f"Part is not a confined regular file: {candidate}")
        for field in ("bytes", "rows"):
            if type(part.get(field)) is not int or part[field] < 0:
                raise ValueError(f"Invalid part {field}: {candidate}")
        if candidate.stat().st_size != part["bytes"] or part["bytes"] > limit:
            raise ValueError(f"Part size/ceiling differs: {candidate}")
        if file_sha256(candidate) != part.get("sha256"):
            raise ValueError(f"Part checksum differs: {candidate}")
    if set(p.name for p in path.iterdir()) != {MANIFEST_NAME, *names}:
        raise ValueError(f"Unlisted publication entries: {path}")
    return record


def _reconstruct(path: Path, destination: Path) -> dict:
    record = _manifest(path)
    frames = []
    for part in record["parts"]:
        frame = pl.read_parquet(path / part["name"])
        if frame.height != part["rows"] or _schema(frame) != record["schema"]:
            raise ValueError(f"Part row count/schema differs: {path / part['name']}")
        frames.append(frame)
    frame = pl.concat(frames, rechunk=True)
    if frame.height != record["rows"] or _schema(frame) != record["schema"]:
        raise ValueError(f"Canonical row count/schema differs: {path}")
    frame.write_parquet(destination, **_PARQUET_WRITE_SETTINGS)
    if destination.stat().st_size != record["canonical_bytes"] or file_sha256(
        destination
    ) != record.get("canonical_sha256"):
        raise ValueError(f"Reconstructed canonical byte identity differs: {path}")
    return record


def publish_artifact(source: Path, destination: Path, max_bytes: int = MAX_BYTES) -> Path:
    """Copy a file, or publish measured contiguous canonical Parquet parts.

    The source is never changed. A destination must be new, avoiding replacement
    of unrelated publication state. Noncanonical oversized inputs fail closed.
    """
    source, destination = Path(source), Path(destination)
    if type(max_bytes) is not int or not 0 < max_bytes <= MAX_BYTES:
        raise ValueError("max_bytes must be within the original 90 MiB ceiling")
    if not source.is_file():
        raise ValueError(f"Publication source must be a regular file: {source}")
    if destination.exists() or destination.is_symlink():
        raise FileExistsError(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(
        prefix=".parquet-publish-", dir=destination.parent
    ) as temporary:
        staging = Path(temporary) / destination.name
        if source.stat().st_size <= max_bytes:
            shutil.copy2(source, staging)
            if file_sha256(staging) != file_sha256(source):
                raise ValueError(f"Copied source checksum differs: {source}")
        else:
            if source.suffix != ".parquet":
                raise ValueError(f"Oversized input is not canonical Parquet: {source}")
            frame = pl.read_parquet(source)
            staging.mkdir()
            parts = []

            def split(offset: int, length: int) -> None:
                candidate = staging / f"part-{len(parts):05d}.parquet"
                frame.slice(offset, length).write_parquet(candidate, **_PARQUET_WRITE_SETTINGS)
                size = candidate.stat().st_size
                if size > max_bytes:
                    candidate.unlink()
                    if length <= 1:
                        raise ValueError(f"Unsplittable row exceeds physical ceiling: {source}")
                    left = length // 2
                    split(offset, left)
                    split(offset + left, length - left)
                else:
                    parts.append(
                        {
                            "name": candidate.name,
                            "bytes": size,
                            "rows": length,
                            "sha256": file_sha256(candidate),
                        }
                    )

            split(0, frame.height)
            record = {
                "format": "ml4t-published-parquet",
                "version": 1,
                "logical_filename": destination.name,
                "canonical_sha256": file_sha256(source),
                "canonical_bytes": source.stat().st_size,
                "schema": _schema(frame),
                "rows": frame.height,
                "max_part_bytes": max_bytes,
                "parts": parts,
            }
            (staging / MANIFEST_NAME).write_text(json.dumps(record, indent=2) + "\n")
            # Prove this source is reconstructible before publishing any part.
            _reconstruct(staging, Path(temporary) / "canonical-check.parquet")
        os.replace(staging, destination)
    return destination


def materialize_artifact(path: Path) -> Path:
    """Replace a copied dataset with its verified canonical regular file.

    Verification finishes before destination changes. Portable replacement of a
    nonempty directory uses two same-filesystem renames and rollback on failure.
    Call only on an owned runtime/staging copy, never on a publication source.
    """
    path = Path(path)
    if not is_published_artifact(path):
        return path
    with tempfile.TemporaryDirectory(prefix=".parquet-materialize-", dir=path.parent) as temporary:
        temporary = Path(temporary)
        canonical = temporary / path.name
        _reconstruct(path, canonical)
        backup = temporary / "dataset"
        try:
            os.replace(path, backup)
            os.replace(canonical, path)
        except BaseException:
            if backup.exists() and not path.exists():
                os.replace(backup, path)
            raise
    return path


def materialize_tree(root: Path) -> None:
    """Materialize recognized datasets only in the caller's copied runtime tree."""
    root = Path(root)
    if is_published_artifact(root):
        materialize_artifact(root)
        return
    for parent, directories, _ in os.walk(root, followlinks=False):
        for name in list(directories):
            candidate = Path(parent) / name
            if is_published_artifact(candidate):
                materialize_artifact(candidate)
                directories.remove(name)


@contextmanager
def verified_canonical_file(path: Path) -> Iterator[Path]:
    """Audit a logical artifact using actual canonical bytes in a private cache.

    The published path is untouched. Ordinary files retain their exact behavior.
    Each dataset audit revalidates real parts and the reconstructed file.
    """
    path = Path(path)
    if not is_published_artifact(path):
        yield path
        return
    with tempfile.TemporaryDirectory(prefix="ml4t-canonical-audit-") as temporary:
        canonical = Path(temporary) / path.name
        _reconstruct(path, canonical)
        yield canonical


def logical_artifacts(root: Path) -> Iterator[Path]:
    """Walk logical Parquet artifacts without treating their parts as models."""
    for parent, directories, files in os.walk(root, followlinks=False):
        for name in sorted(list(directories)):
            candidate = Path(parent) / name
            if candidate.suffix == ".parquet":
                if not is_published_artifact(candidate):
                    raise ValueError(f"Unrecognized Parquet dataset: {candidate}")
                yield candidate
                directories.remove(name)
        for name in sorted(files):
            if name.endswith(".parquet"):
                yield Path(parent) / name


def publish_tree(source: Path, destination: Path) -> Path:
    """Publish a new physical fixture tree from unchanged canonical inputs."""
    source, destination = Path(source).resolve(), Path(destination).absolute()
    if not source.is_dir():
        raise ValueError(f"Publication source tree is absent: {source}")
    if source == destination.resolve() or source in destination.resolve().parents:
        raise ValueError("Publication destination must be outside its source tree")
    if destination.exists() or destination.is_symlink():
        raise FileExistsError(destination)
    destination.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.TemporaryDirectory(
        prefix=".fixture-publish-", dir=destination.parent
    ) as temporary:
        staging = Path(temporary) / destination.name
        staging.mkdir()
        for parent, directories, files in os.walk(source, followlinks=False):
            for name in directories:
                if (Path(parent) / name).is_symlink():
                    raise ValueError(
                        f"Publication source contains a directory symlink: {Path(parent) / name}"
                    )
            (staging / Path(parent).relative_to(source)).mkdir(parents=True, exist_ok=True)
            for name in sorted(files):
                path = Path(parent) / name
                publish_artifact(path, staging / path.relative_to(source))
        os.replace(staging, destination)
    return destination


def main() -> None:
    """Explicit fixture publication or owned-runtime materialization entry point."""
    import argparse

    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="operation", required=True)
    publish = commands.add_parser("publish", help="publish a new fixture tree; preserve source")
    publish.add_argument("source", type=Path)
    publish.add_argument("destination", type=Path)
    materialize = commands.add_parser(
        "materialize", help="reconstruct an owned copied runtime tree"
    )
    materialize.add_argument("root", type=Path)
    args = parser.parse_args()
    if args.operation == "publish":
        publish_tree(args.source, args.destination)
    else:
        materialize_tree(args.root)


if __name__ == "__main__":
    main()
