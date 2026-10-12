# Complete MLFT dependency graph — current Python 3.15 control

The current complete graph cannot resolve on Python 3.15 under its published
dependency contracts. The universal control fails in 2.53 seconds, and a second
control restricted to this actual macOS arm64 host fails in 1.75 seconds. Both
stop at the same Pandas version contradiction before compilation or notebook
execution. These are dependency-resolution results, not test-node outcomes.

The separate control copies the current 548-entry lock and complete project
metadata, retaining every dependency, compatibility cap, extra, development
group and official Gensim source route. Only the control's Python range changes
from `>=3.13,<3.15` to `>=3.15,<3.16`. The actual-host control additionally limits
resolution to Darwin arm64. The main source, lock and runtime remain unchanged.

| Current official release | Source dependency contract |
| --- | --- |
| [Feast 0.66.0](https://pypi.org/project/feast/0.66.0/) | `pandas>=1.4.3,<3` |
| [ml4t-backtest 0.1.12](https://pypi.org/project/ml4t-backtest/0.1.12/) | `pandas>=3.0.5` when `python_version >= '3.15'`; `pandas>=2.3.3` below 3.15 |

The verified official source archives contain these same requirements in their
`pyproject.toml` files, at Feast line 25 and ml4t-backtest lines 84–85. Their
Pandas version intersection is empty for Python 3.15. Compiling a missing wheel
does not alter that declared conflict; a validated upstream compatibility change
would be required. No bound is overridden, dependency withheld, or old package
selected merely to suppress this result.

The [native RoughPy/esig source control](roughpy-native315.md) separately builds
and passes 1,495 unchanged upstream cases on actual Python 3.15. That genuine
source route cures its compiler-header issue and demonstrates why a missing
wheel alone does not establish an unavoidable interpreter limitation. It does
not resolve the complete project's independent dependency contradiction.

## Retained standalone evidence

- [Control provenance and unchanged main source/lock hashes](mlft-full548-python315-resolution-control-provenance.json)
- [Current official release metadata](mlft-current315-feast-pandas-backtest-official-metadata.json)
- [Verified official source archive hashes and requirement lines](mlft-current315-original-source-dependency-constraints.json)
- [Universal command/result](machine-learning-for-trading-current-full548-python315-universal-metadata-resolution.json) and [terminal log](machine-learning-for-trading-current-full548-python315-universal-metadata-resolution.log)
- [Actual-host command/result](machine-learning-for-trading-current-full548-python315-actual-arm64-metadata-resolution.json) and [terminal log](machine-learning-for-trading-current-full548-python315-actual-arm64-metadata-resolution.log)

Python 3.14 remains the highest verified compatible complete-project runtime.
No new MLFT cases are counted and no Python 3.15 full-suite success is claimed.
