"""One-off genuine-fixture diagnostic; no additional pytest cases."""

from pathlib import Path
import importlib.util, json
from tests.fixture_registry import shipped_artifact_shas
from case_studies.utils.published_artifacts import file_sha256, MANIFEST_NAME, materialize_tree
from tests.conftest import seed_case_study_intermediates

source = Path(
    "/Users/alex/workspaces/trading/.runtime/maintenance-2026-10-12/mlft-fixture/intermediates"
)
publication = Path(
    "/Users/alex/workspaces/trading/.runtime/maintenance-2026-10-12/mlft-shards-controls/fixture/intermediates"
)
case = "nasdaq100_microstructure"
canonical_shas = shipped_artifact_shas(source / case)
published_shas = shipped_artifact_shas(publication / case)
assert canonical_shas == published_shas
spec = importlib.util.spec_from_file_location(
    "publication_audit", Path("scripts/artifact_audit.py")
)
audit = importlib.util.module_from_spec(spec)
spec.loader.exec_module(audit)
audit.get_case_study_dir = lambda _: publication / case
on_disk, scope, absent = audit.walk(case, publication)
assert set(on_disk) == set(canonical_shas)
assert not absent
runtime = publication.parent.parent / "seeded-control" / case
seed_case_study_intermediates(publication / case, runtime)
original = source / case / "features/financial.parquet"
reconstructed = runtime / "features/financial.parquet"
assert reconstructed.is_file() and file_sha256(original) == file_sha256(reconstructed)
materialize_tree(runtime)  # repeat is ordinary-file no-op
files = [p for p in publication.rglob("*") if p.is_file()]
all_equal = []
for p in source.rglob("*"):
    if p.is_file():
        relative = p.relative_to(source)
        dest = publication / relative
        if dest.is_file():
            assert file_sha256(p) == file_sha256(dest)
            all_equal.append(relative.as_posix())
        else:
            assert dest.is_dir() and (dest / MANIFEST_NAME).is_file()
result = {
    "source_root": str(source),
    "publication_root": str(publication),
    "every_published_physical_file_within_90MiB": all(
        p.stat().st_size <= 90 * 1024**2 for p in files
    ),
    "physical_files": len(files),
    "largest_physical_file_bytes": max(p.stat().st_size for p in files),
    "ordinary_files_verified_byte_identical": len(all_equal),
    "logical_registry_hashes_identical": True,
    "logical_artifact_count": len(on_disk),
    "audit_scope": scope,
    "runtime_canonical_regular_file": reconstructed.is_file(),
    "runtime_sha256": file_sha256(reconstructed),
    "publication_still_directory": (publication / case / "features/financial.parquet").is_dir(),
}
assert result["every_published_physical_file_within_90MiB"]
Path("docs/maintenance-2026-10-12/mlft-shards-publication-audit-control.json").write_text(
    json.dumps(result, indent=2) + "\n"
)
print(json.dumps(result, indent=2))
