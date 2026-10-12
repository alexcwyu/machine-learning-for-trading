# MLFT validation — 2026-10-12

The original inventory contains **8,333 existing test nodes in 430 modules**. Validation combines retained terminal module results and exact original-node recovery runs. It is not a claim that one full-suite invocation passed. The authoritative per-node record is [original case coverage](../../docs/maintenance-2026-10-12/mlft-original-case-coverage.json); unresolved identities and genuine prerequisites are recorded in [failure explanations](../../docs/maintenance-2026-10-12/mlft-original-failure-explanations.json). The final inventory reconciliation is still in progress while the remaining original notebook cases execute.

No cases were added. All original numeric/hash literals and CAE model version 1 are preserved. The five previously modified identity files have been restored byte-for-byte from the original HEAD. Earlier results obtained with changed pins do not validate those original contracts.

## Runtime and immutable identities

Python 3.14.8 runs the complete managed environment. The attempted Python 3.15 full resolution conflicts with Feast's Pandas constraint and the available ml4t-backtest wheel requirements. The frozen lock selects the latest compatible Polars 1.44.2, preserving the original canonical Parquet SHA and holdout hash; Polars 2 fails those immutable contracts. Torch remains the latest 2.11.0.

The original strict main scope passes **151 cases and fails one CAE identity case** in 20.17 seconds. On macOS arm64 the seeded CAE prediction digest is `22ba1b43276579c8`, against the original `82a8721e8c074459`. Genuine Python 3.13 and Torch 2.10 controls reproduce the same host mismatch and do not justify a host downgrade.

The unchanged CAE case passes with its original version 1 and `82a8721e8c074459` on actual canonical Linux/amd64 CPU using both official Torch 2.10.0 (6.45 seconds) and latest 2.11.0 (7.08 seconds). NumPy 2.3.5, Pandas 2.3.3, SciPy 1.17.1, current identical model source and the unchanged float64 workload were retained. This is platform-scoped identity evidence, not an alteration of the host model backend or golden.

## Existing case fixes

| Original scope | Change and outcome |
| --- | --- |
| Source/provenance/research configuration | 74 cases pass in 121.03 seconds. The release fallback digest excludes transient executed notebooks and bytecode caches, preventing concurrent cleanup races. Paired source changes retain original executed outputs with an explicit provenance reason. |
| ETF date boundaries | Seven ISO holdout boundaries become actual date literals, preserving their values and intervals. Existing ETF/factor prerequisite cases pass. |
| ARIMA teaching notebook | Explicit positional indexes preserve all chronological returns and original ARIMA orders. The existing case passes in 29.73 seconds with native compilation and optimization enabled. |
| Native PyTensor compiler | The optional actual Apple clang adapter removes only PyTensor's invalid `-ld64` library argument. Native C/JIT, graph optimization and every other compiler flag remain. |
| Options symbol identity | Genuine public class-B aliases map BRKB/BFB to the bundled BRK.B/BF.B share namespace. The full-production original 633-symbol roster passes all 10 cases in 0.73 seconds. Original options research scopes retain their observed prices and rows. |
| Native thread ownership | The real Apple Accelerate controller uses its public getter/setter; each actual IPCA worker owns its thread mode. The original no-leak fixture restores Torch thread, deterministic, cuDNN and CPU RNG state. |
| CFTC download | The actual provider falls back from malformed HTTP403 HTML to bounded curl retrieval of a genuine ZIP, validates the archive and named CSV, and retains provider cache/schema behavior. |

Homebrew libomp 23.1.3 is selected through `DYLD_LIBRARY_PATH`; a physical image inventory confirms one OpenMP library after importing actual Torch, sklearn and LightGBM. No duplicate-runtime bypass, binary patch, weakened assertion, disabled optimizer or model-version repin is used.

## Genuine data and producer evidence

Complete public production inputs remain retained: NASDAQ 48,880,176 minute rows over 505 sessions; options 366,242,819 observed rows over 1,259 sessions; all 100 configured ETFs and 470,662 rows. Real options lifecycle, surfaces and straddles are materialized. Official observed FRED data supplies 23 configured series; ALFRED initial-release vintages are a separate credentialed prerequisite.

The unchanged original CI builders produce their declared ETF/NASDAQ/options fixture budgets from those inputs, plus actual AQR, Fama–French and options EDA inputs. The original producers complete all five stages for each of ETFs, NASDAQ, equity-option analytics and options. The options sampler retains its original draws/tune/chains and diagnostics. The NASDAQ temporal stage adds the real 22 features to its 66 financial features, satisfying the unchanged 88-feature pilot contract.

Earlier full-input artifacts are retained separately when genuine CI outputs are routed into the original model fixture's read directories. No production input is removed. Fresh producer sidecars are verified against the actual compatible-codec value digest.

The original 90 MiB per-file Git publication gate remains failing for the 114.94 MiB NASDAQ financial fixture. Separate genuine lossless encoding controls yield 112.64, 105.92 and 102.75 MiB, preserving the complete schema, rows, values, null counts and every nonnull float bit. Neither the canonical writer nor the original gate is changed. The controls do not prove all possible lossless storage approaches have been exhausted.

## Build and remaining scope

The latest main `uv sync --frozen --all-groups --all-extras`, wheel, source distribution and source `compileall` pass. Focused source Ruff checks pass. Existing conditional skips retain their original blocker logic.

Remaining original notebook nodes execute with their declared parameters and prerequisites. The original model registry fixture explicitly reads production case-study directories, so it must receive actual matching producer artifacts rather than merely an environment path. Missing paid CME/DataBento and US-equity/Quandl inputs, ALFRED API access, private test-data checkout access, model populations, specialized containers/services and native platform requirements are reported separately. A missing artifact is not called privately unobtainable without proving its genuine public producer prerequisites.


## Subsequent genuine prerequisite recovery

The unchanged original crypto downloaders complete all 19 configured symbols
(866,868 hourly bars, 107,839 premium rows, 108,157 actual funding settlements).
The original CI builder applies its prescribed 10-symbol fixture contract.
Matching the financial stage's funding join key to the actual price timestamp
schema preserves values and yields all five original producer stages passing
in 86 seconds. Original affected test nodes continue separately.

The actual ETF LSTM registry fixture now trains six epochs only for the original
case whose assertion requires checkpoints 5 and 6; its copied shared presets are
restored after the case. The existing linear/GBM/LSTM and checkpoint-parameter
checks pass (four cases, 101.74 seconds). Original assertion literals and shared
two-epoch producer defaults remain unchanged.

The source-configured Neo4j Community 2026.02.2 service is provisioned as an owned
isolated container on loopback ports 17474/17687, with separate owned volumes and
the original authentication configuration. Existing ports/containers were
checked before creation. Original graph cases are rerun against that real
service; graph inputs and provider credentials remain independently required.
