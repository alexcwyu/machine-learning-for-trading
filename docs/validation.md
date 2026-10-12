# MLFT validation — 2026-10-12

The original inventory contains **8,333 existing test nodes in 430 modules**. The current dynamic collection contains **8,327 identities: 7,644 pass, 467 conditional skips and 216 fail, with zero unverified current nodes**. Results combine retained terminal runs and exact-node recovery across actual input/platform scopes; no single full-suite green invocation is claimed. [Per-node coverage](maintenance/mlft-original-case-coverage.json), [failure explanations](maintenance/mlft-original-failure-explanations.json) and [inventory reconciliation](maintenance/mlft-original-current-inventory-reconciliation.json) preserve the evidence.

Ten obsolete skip-declaration guard parameter identities and one empty fold placeholder retire from the original collection. Genuine artifacts activate five parameterizations of the unchanged existing fold test. Historical outcomes of all eleven retired identities remain separate; none is relabeled as a current pass. No test source cases or assertions were removed or added. The 216 current failures comprise 188 missing genuine input/artifact prerequisites and 28 runtime or contract failures requiring diagnosis. Their modules are: chapter notebooks 82, Docker notebooks 85, case studies 44, model registry two, artifact specs one, backtest presets one and fixture-population backtests one. Locally producible prerequisites remain actionable work.

No cases were added. All original numeric/hash literals and CAE model version 1 are preserved. The five previously modified identity files have been restored byte-for-byte from the original HEAD. Earlier results obtained with changed pins do not validate those original contracts.

## Runtime and immutable identities

Python 3.14.8 runs the complete managed environment. The attempted Python 3.15 full resolution conflicts with Feast's Pandas constraint and the available ml4t-backtest wheel requirements. The frozen lock selects the latest compatible Polars 1.44.2, preserving the original canonical Parquet SHA and holdout hash; Polars 2 fails those immutable contracts. Torch remains the latest 2.11.0.

The original strict main scope passes **151 cases and fails one CAE identity case** in 20.17 seconds. On macOS arm64 the seeded CAE prediction digest is `22ba1b43276579c8`, against the original `82a8721e8c074459`. Genuine Python 3.13 and Torch 2.10 controls reproduce the same host mismatch and do not justify a host downgrade.

The unchanged CAE case passes with its original version 1 and `82a8721e8c074459` on actual canonical Linux/amd64 CPU using both official Torch 2.10.0 (6.45 seconds) and latest 2.11.0 (7.08 seconds). A subsequent actual Python 3.14.8/latest Torch 2.11.0 Linux control also passes in 5.97 seconds. NumPy 2.3.5, Pandas 2.3.3, SciPy 1.17.1, current identical model source and the unchanged float64 workload were retained. This is platform-scoped identity evidence, not an alteration of the host model backend or golden.

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

The original 90 MiB per-file Git publication gate now passes using genuine published Parquet parts and a verified manifest. All 1,177 physical fixture files fit the unchanged ceiling. Seeding reconstructs canonical regular files in the separate runtime destination through [the publication materializer](../case_studies/utils/published_artifacts.py), preserving all six logical NASDAQ hashes and existing regular-file consumers. The canonical writer, numerical data, source-pinned lineage and seven original guard/writer files remain unchanged. The fresh integrated original storage scope passes all 132 cases in 9.34 seconds on merge `d3e1ce336`.

The earlier 114.94 MiB single-file failure and lossless encoding controls (112.64, 105.92 and 102.75 MiB) remain historical diagnostics. Published physical parts and reconstructed runtime files serve their respective original publication and execution contracts.

## Build and remaining scope

The current source `4736e270` passes fresh wheel/source-distribution builds (1.34 seconds) and strict compilation of all 1,218 Git-tracked Python files (1.71 seconds). The universal frozen lock now contains 548 package entries; the native host contains 516 installed distributions. All prior locked package versions are preserved. Focused source Ruff checks pass. Genuine completed prerequisites permit obsolete skip declarations to retire; remaining conditional skips retain their blocker logic.

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


## Exact provider adjustment and downstream consumer recovery

The actual Yahoo raw IWM bar has Low exactly equal to Close. Upstream yfinance
multiplies OHLC by AdjClose/Close but assigns AdjClose directly to Close; this
can round an equal raw low one ULP above adjusted close. The owned ETF producer
wraps that actual conversion only while downloading, preserves provider AdjClose
exactly for raw OHLC fields exactly equal to raw Close, and retains every other
upstream formula. It restores the upstream callable afterwards. No quote clipping,
comparison tolerance or assertion changes are used.

The unchanged full ETF configuration downloads all 100 symbols and 470,662 rows
into a separate genuine snapshot in 26.53 seconds; the prior inputs remain
retained. Both original commission/slippage notebook cases pass. All eight
original baseline guards pass against the refreshed snapshot in 3.27 seconds,
including the original published Sharpe 0.743 and return 1.9675 literals.

The original crypto linear and GBM canonical producers complete with their
unchanged invocation parameters, copied presets and non-preview execution.
Their genuine artifacts are seeded for downstream original consumer checks;
the previous seed view is retained separately.

The original Chapter 16 signal-method comparison and its Docker notebook case
now both pass after genuine crypto canonical producers complete. The repeated
Chapter 11/12 consumers subsequently advance through genuine firm populations to absent FX populations.
Other latent-factor/DL/causal and downstream allocation/cost populations still
require their actual producers; the current failed-node record distinguishes
these from credentialed inputs and image-specific native prerequisites.


### Further genuine public fixture recovery

The unchanged author-data downloader and persistent tensor converter produce
1,218,555 firm-characteristic stock-month observations (115.66 seconds). The
original CI builder retains its prescribed 200 most-observed firms per split
and all their monthly histories: 119,898 rows. All six canonical original
feature/evaluation/linear/GBM stages pass in 42.87 seconds. The recovered original
firm pipeline/model-registry scope records 32 passes, four failures and five
existing conditional skips in 495.76 seconds. Actual canonical data is routed
to the selected CI data root's sibling intermediates, with preceding views
retained. The Chapter 11/12 consumers now reach absent FX populations.

All 26 original ETF and equity-option analysis/validation/allocation/risk/cost
producer invocations pass in 618.50 seconds. The analogous eleven original
firm validation producer invocations pass in 104.07 seconds. These are genuine
producer scopes, distinct from original test-node counts.

A real seeding defect overwrote canonical prediction digests with whole-frame
digests including the label metadata. The actual writer and reader use the
unchanged `published_prediction_digest`, excluding that constant label. The
[seeding helper](../tests/fixtures/seed_results.py) now uses that same function.
Identical genuine prediction frames retain their original content identities;
no literal, writer or numeric golden changes. Twenty original seeding, encoding,
source-lineage and consumer contracts pass in 16.68 seconds, including the
previously failing equity-option strategy analysis.

The genuine Financial Phrasebank author archive supplies all four agreement
levels (2,264/3,453/4,217/4,846 sentences). Its original CI builder copies the
2,264 all-agreement rows verbatim. The complete genuine NASDAQ ITCH session is 5,597,158,940 bytes. Its unchanged official Rust parser processes the full session; the original CI builder retains its prescribed first 500 A/P messages per five symbols plus five R rows. Two lifecycle cases additionally pass against the complete production input, without enlarging the CI budget. Four remaining microstructure cases require real DataBento MBO, a distinct input.

The original SEC 13F bulk quarter provides 2,863,210 canonical holdings; the original CI builder selects its declared 600 managers, retaining 1,327,852 whole positions. The actual ten-institution producer supplies 25,414 edges and 8,311 stock features. The four original word2vec/asset-embedding nodes now pass across retained native recovery runs. Original institutional-holdings chapter/Docker scopes pass against the genuine owned Neo4j service. The supply-graph workflow still requires its actual SEC corpus and Qwen extraction.

The original firm strategy analysis executes all 70 cells successfully after verbatim copies of 40 tracked release benchmark files. The corrected canonical route and expired-declaration guard scope records 82 passes and seven existing skips. ETF holdout predictions, holdout backtest and strategy analysis all pass with unchanged canonical parameters (37.15 seconds). Both original Chapter/Docker live-trading winner cases pass. After removing only the now-obsolete ETF strategy skip declaration, its original node and the existing override/skip-contract scope pass: 79 passes and seven existing skips in 28.13 seconds. Equity-option holdout registry and ETF SDF assertions remain separate diagnoses.


## Current Gensim native source route

Gensim 4.4.0 remains the current release. Its PyPI source archive contains stale generated C incompatible with Python 3.14 and omits one `.pyx` file needed for complete regeneration. The lock instead selects the complete official release commit `ee2642b4fa26e689ba4595067504668bc7a89016`. Its supported Cython regeneration builds genuine native CPython 3.14 extensions; 201 original algorithm/header files remain unchanged. No compiler flag or numerical algorithm changes are used. All four original text-node scopes pass after genuine Phrasebank and 13F recovery. The unchanged immutable guard scope passes 53 cases in 4.91 seconds.

This is locally verified Python 3.14 compatibility, not a claim of upstream official support. The Git source selection belongs to uv configuration/lock data and is not conveyed by plain pip installation of this project's wheel metadata. PEP 517 build requirements are lower bounds rather than a fully locked compiler toolchain. The original official amd64 Python 3.12 image remains available, but its four investigated notebook runs failed kernel startup under this host's emulation; those terminal failures remain recorded.


The genuine ETF canonical holdout/strategy producers complete all 11, eight and
40 original cells, respectively. The recovered live-trading consumers pass
against their genuine seeded artifacts. The obsolete ETF strategy declaration
retires one additional parameterized skip guard, giving the current collection
8,327 identities while preserving all 8,333 original identities and historical
outcomes separately. The unchanged full-population canonical firm causal-DML producer passes all
11 cells in 75.52 seconds; its original per-cell timeout is retained.


The actual canonical firm causal producer uses the full declared genuine CI
population and unchanged defaults, with no preview reductions. Both original
Chapter/Docker causal-insights nodes now pass in 12.77 seconds. The actual
canonical firm IPCA producer also passes all 14 cells in 77.10 seconds, using
the source's declared CPU implementation and four workers. Previous owned seed
views are backed up before genuine output is copied. Its two original latent
insights consumers still fail, now reaching the absent FX latent population
rather than the firm prerequisite. Configured OANDA, ALFRED and paid market-data
credentials are absent; no alternate financial observations are substituted.

The separately reviewed optional-cleaning repair preserves the original loader
exception branches and guards. Both original preprocessing nodes pass; the
absent Sharadar section does not execute. The [source review and actual input
scope](maintenance/preprocessing-review.md) records the original failure,
minimal repair, unchanged AST outside the intended assignments and genuine
executed datasets. The isolated official native signature controls are recorded below.


### Genuine native signature recovery

Current esig 1.0.0 and RoughPy 0.3.0 provide a genuine official CPython 3.14
arm64 native wheel; pyrecombine 1.0.1 builds from its unchanged source. The exact
frozen isolated environment preserves all original package versions and adds
only those three dependencies. Both original path-signature notebook nodes and
53 unchanged identity guards pass (55 cases, 40.20 seconds). After frozen main
sync adds the same dependencies, that exact original scope passes again in
38.37 seconds. These are native Python 3.14 runs of the Chapter and Docker-named
cases; the earlier official-image kernel-startup failures remain separate.
Actual esig/RoughPy, NumPy 2.3.5, Torch 2.11.0, sklearn and LightGBM imports plus
signature calculation load one physical Homebrew libomp 23.1.3 image. No runtime
patch, backend substitution or golden change is used.

The Python 3.15 source attempt first stops at missing Autoconf tools. After their
genuine installation, it reaches native compilation and fails on range-v3/meta
standard-library forward declarations against the host's newer libc++ headers
(282.39 seconds). All 814 checked official RoughPy core files are unchanged.
This is not a demonstrated Python 3.15 binding-API failure. The reviewed exact
upstream dependency-header fix subsequently passes in the isolated supported
port overlay: native build 169.55 seconds, followed by 1,495 unchanged upstream
Python cases passing and 35 existing skips in 1.60 seconds. All 814 original
core/configuration/Python/C++ files remain identical. The [standalone source and
binding proof](maintenance/roughpy-native315.md) retains the exact upstream
commit, license, patch and terminal evidence. No Python 3.15 main-runtime
success or additional MLFT test-node passes are claimed.

The original EconML DML teaching Chapter and Docker-named cases also pass with
current genuine inputs (34.85 seconds). Their source, parameters and assertions
remain unchanged; the former Docker-node zero-sample failure is retained as
historical evidence. The aggregate-synthesis nodes still refuse genuine
incomplete backtest coverage, now at the actual GBM one-day candidate; that
coverage bar remains unchanged. The equity-option holdout registry case requires
the genuine original stage-18 canonical CUDA holdout population, not an empty
replacement database.
