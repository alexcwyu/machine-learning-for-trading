# Lossless published Parquet and canonical runtime views

## Purpose and authorization

Finish the existing trading-maintenance goal by making its genuine original CI artifacts fit the existing 90 MiB physical-file ceiling without changing data, model identities, lineage or assertions. The user explicitly instructed autonomous sensible decisions while offline, so implementation does not wait for additional design or worktree approval. No additional test cases may be added.

## Decision and alternatives

Use separate publication and runtime views. Published large canonical Parquet files become ordered contiguous Parquet parts under the same logical artifact path, with a validated manifest. Existing seeding and research-workspace staging reconstruct a genuine regular file at the destination only. This preserves the consumer API and its original byte fingerprint. Raising the limit would weaken the real GitHub storage requirement; reducing rows or precision would change the original input. Passing dataset directories directly to consumers would break pinned regular-file lineage code, so neither approach is selected.

## Existing evidence

The genuine NASDAQ financial artifact contains 558,456 rows and 120,527,027 bytes. Two contiguous parts written with the unchanged canonical settings occupy 60,964,707 and 59,629,985 bytes. Polars read, scan and schema operations preserve all rows, ordering, nulls and Float32 bits. Re-encoding their concatenation reproduces the exact original SHA256 `ffa3cd85815f998dfa30a0b05fd8175fbed36c8f8527e689a59e3650d8246679` and byte size. These are controls, not permission to trust a copied checksum.

## Storage format and interfaces

Add `case_studies/utils/published_artifacts.py` as the single publication/materialization owner. It uses the existing `artifact_digest._PARQUET_WRITE_SETTINGS` unchanged.

- `publish_artifact(source: Path, destination: Path, max_bytes: int = 90 * 1024 * 1024) -> Path`: ordinary files at or below the ceiling copy byte for byte; oversized canonical Parquet becomes a directory at the logical destination. Preserve source files.
- `materialize_artifact(path: Path) -> Path`: recognize only the versioned publication manifest, validate its real ordered parts, write and verify the exact canonical regular file, then replace the copied destination dataset atomically. Ordinary files are unchanged.
- `materialize_tree(root: Path) -> None`: materialize recognized datasets in an owned runtime/staging tree; never modify the publication source.

Manifest format version is 1. Record the logical filename, original canonical SHA256 and byte size, schema with column order, row count, and ordered `part-00000.parquet` entries with actual SHA256, size and row count. Parts must be regular files confined to the dataset directory, without duplicate names, traversal or escaping symlinks. Every physical part must fit the original ceiling; recursively split contiguous row ranges if measured parts remain oversized. Fail clearly for an unsplittable row or noncanonical source rather than changing its values or encoding.

## Routing and unchanged contracts

`tests/conftest.py` keeps `intermediates_dir` and its publication root unchanged. Extend only destination seeding after the existing copy. `seeded_output_dir` already sets `ML4T_OUTPUT_DIR`; existing paths therefore direct modeling, coverage and lineage to the actual reconstructed regular files. `scripts/create_experiment.py` materializes copied staging inputs before atomic research-workspace publication.

Publication-side fixture registry and artifact audit must distinguish logical canonical artifacts from physical parts. Their logical hashes come from actual verified canonical materialization in an owned cache outside the published tree; size reporting explicitly separates canonical bytes and physical storage bytes. Do not hash a directory or count its parts as separate logical models. Existing CI plain-copy consumers require the same materialization hook. Keep independent registry bootstrap inputs canonical; use a verified runtime cache only if they actually point to published shards.

Never modify `case_studies/utils/registry/lineage.py`, its source-SHA assertion, any of the five restored numeric/codec/CV guard files, the original size gate, model parameters, goldens or case inventory. No new skips or synthetic inputs. No model version bumps.

## Failure, atomicity and verification

Verify part checksums, ordered row count/schema and canonical reconstruction checksum from actual data. Failed verification leaves the original copied dataset intact and removes only owned temporary files. Destination replacement preserves existing stale-removal and idempotence semantics. Independent pytest workers keep independent runtime roots. Source publication and runtime materialization are explicitly different operations.

Run existing seeded-output, fixture registry, artifact audit, encoding, CV and pinned-lineage cases, then the unchanged size gate against a genuine sharded publication control. Reconcile original-node coverage separately. One-off evidence controls may check corruption and exact reconstruction; do not add pytest cases. Preserve exact commands and original data/source hashes. An isolated worktree protects currently running main-workspace jobs; no main fixture mutation or merge until coordinated with its owner.
