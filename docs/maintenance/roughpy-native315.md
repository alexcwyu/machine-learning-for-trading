# Native RoughPy and esig — Python 3.15 source control

The isolated native Python 3.15.0 build passes in **169.55 seconds**. Genuine
RoughPy 0.3.0, esig 1.0.0 and pyrecombine 1.0.1 import and calculate the original
public signature example correctly with current NumPy 2.5.4. The unchanged
upstream RoughPy Python suite records **1,495 passes and 35 existing skips in
1.60 seconds**. These upstream cases are supplementary dependency evidence;
they are not included in MLFT's original 8,333-node inventory or its current
8,327-node collection. The main project remains on Python 3.14.

## Exact compiler repair and preserved source

The first unchanged source attempt stops at missing Autoconf tools. Genuine
Homebrew Autoconf 2.73, Automake 1.19 and Libtool 2.6.2 cure that prerequisite.
The next attempt reaches native compilation, then fails on range-v3/meta's
standard-library forward declarations against host libc++ 220106. It does not
reach a demonstrated Python 3.15 binding incompatibility.

The [official upstream fix](https://github.com/ericniebler/range-v3/commit/bef4198ccababd6d130e1f56aa015faaaddd1f1d)
changes only the visibility-version guard for libc++ 22. The isolated control
copies the original vcpkg range-v3 0.12.0#4 port into RoughPy's already declared
`tools/ports` overlay and applies that exact [licensed patch](roughpy-range-v3-upstream-bef4198.patch).
The [upstream license](roughpy-range-v3-upstream-LICENSE.txt) and original port
copyright installation are retained. No numerical source, compiler flag,
header alias, Python ABI substitution or backend change is used. The original
`pybind11<3.0.0` build requirement remains intact. CMake and vcpkg use two build
jobs to bound resource use.

All **814 original core, configuration, Python and C++ source files** retain
exact official release-archive bytes after the successful build. Only the
licensed external dependency-overlay files are added. The original archive SHA
is `db5d5ee5319c504603061687756c7f88cdd28a3103b58ecc01a411e98dfa0119`.

## Retained terminal evidence

- [Exact upstream port and license provenance](mlft-roughpy-native315-upstream-port-provenance.json)
- [Post-build original-source identity](mlft-roughpy-native315-success-original-core-identity.json)
- [Actual Python 3.15 native binding and signature control](mlft-genuine-native315-roughpy-esig-binding-control.json)
- [Successful source build command/result](machine-learning-for-trading-genuine-roughpy-native315-supported-upstream-port.json) and [build log](machine-learning-for-trading-genuine-roughpy-native315-supported-upstream-port.log)
- [Unchanged upstream test command/result](machine-learning-for-trading-roughpy-upstream-existing-python315-binding-cases.json) and [test log](machine-learning-for-trading-roughpy-upstream-existing-python315-binding-cases.log)

The original compiler failures remain in the workspace campaign records. This
control establishes source and binding feasibility for this dependency. It
does not establish that the complete MLFT dependency graph resolves or that all
MLFT notebooks execute on Python 3.15. The complete-project Feast/Pandas/backtest
constraints require their own current source-backed resolution probe.
