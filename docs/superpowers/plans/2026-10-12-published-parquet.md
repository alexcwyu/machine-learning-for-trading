# Published Parquet Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Pass the original physical-file ceiling with lossless published parts and exact canonical regular runtime files.

**Architecture:** One publication/materialization module owns checksums and reconstruction; existing destination-copy boundaries invoke it. Pinned lineage and ordinary-file behavior remain unchanged.

**Tech Stack:** Python 3.14.8, highest compatible Polars 1.44.2, hashlib/JSON/pathlib/tempfile, existing uv environment and original pytest cases.

**Spec:** `docs/superpowers/specs/2026-10-12-published-parquet-design.md`

## Global Constraints

- Physical parts <= 90 * 1024 * 1024 bytes; unchanged original gate.
- Existing `_PARQUET_WRITE_SETTINGS`, source/data/rows/order/nulls/Float32 bits, canonical SHA and model identities remain exact.
- No additional tests, assertion/golden/source-SHA repins, model versions, skips or synthetic inputs.
- Work only in this isolated branch; source data and main runtime remain untouched until coordinated integration.

## Review Focus

- Tampered or escaping manifest parts must fail without modifying source/destination data.
- Ordinary single-file artifacts and all original encoding/lineage pins remain identical.
- Stale destination contents and repeated seeds retain original replacement/idempotence behavior.
- Canonical reconstruction must be verified from real parts, not accepted from metadata alone.
- Publication audit counts logical artifacts separately from physical parts; no directory-stat gate trick.

### Task 1: Owned artifact publication and materialization

**Files:** Create `case_studies/utils/published_artifacts.py`; reference unchanged `case_studies/utils/artifact_digest.py` settings.
**Interfaces:** Implement exactly the three signatures and version-one manifest in the spec.

- [ ] Record current original ceiling failure and retain the provided temporary exact-byte controls.
- [ ] Implement measured contiguous splitting, confined checksums, source preservation and verified atomic destination materialization.
- [ ] Exercise one-off controls for actual NASDAQ parts/reconstruction and tampered manifests; record evidence without adding pytest cases.
- [ ] Run original `tests/test_artifact_digest_encoding.py` and `tests/test_registry_lineage.py`; require unchanged pins and passing cases.
- [ ] Commit only owned module/docs.

### Task 2: Seeding and research workspace boundaries

**Files:** Modify `tests/conftest.py` destination `seed_case_study_intermediates`; `scripts/create_experiment.py` staging copy; inspect actual CI copy steps and registry bootstrap helpers before making narrowly needed routing changes.
**Interfaces:** Call `materialize_tree(root)` only in owned copied runtime/staging directories. Publication sources stay sharded; consumers receive genuine regular files.

- [ ] Implement destination-only hooks, preserving ordinary files, stale removal and independent worker roots.
- [ ] Run existing `tests/test_seeded_output_dir.py`, `tests/test_fixture_registry_identity.py`, `tests/test_modeling_input_lineage.py`, `tests/test_holdout_cv_derivation.py` and relevant actual research-workspace cases.
- [ ] Verify pinned lineage and all five restored guard files remain byte-identical to the original branch.
- [ ] Commit owned routing changes.

### Task 3: Publication helpers and original budget proof

**Files:** Existing `tests/fixture_registry.py`, `scripts/artifact_audit.py`, and explicit fixture-publishing entry point adjacent to the original fixture generation workflow as needed. Do not modify the original producer math or original gate.
**Interfaces:** Logical identity comes from an actual verified canonical cache file; physical footprint includes every real part.

- [ ] Adapt publication-side inspection only where direct directory consumption would fail; maintain original ordinary-file semantics.
- [ ] Produce a separate genuine published CI fixture control, preserving the current original main fixture.
- [ ] Run unchanged `tests/test_fixture_file_size_ceiling.py`, original audit/fixture identity cases and affected original consumers against the control.
- [ ] Record logical original byte SHA, physical part sizes/checksums, original data equality and all command outcomes.
- [ ] Update source-linked Markdown/HTML-ready documentation with class/sequence/workflow diagrams; commit owned changes and report exact branch commits for later main integration.
