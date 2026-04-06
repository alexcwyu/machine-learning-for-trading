# Migration Guide: machine-learning-for-trading

**Branch**: `feature/ayu_develop`
**Standard**: See `docs/PYTHON_MODERN_STANDARD.md` in the trading workspace root.

## Overview

This project has been modernized on the `feature/ayu_develop` branch to use the 2026 Python tooling stack. When syncing from upstream (default branch), the following changes must be re-applied if upstream overwrites them.

## What Changed

### 1. Build System (pyproject.toml)
- **Build backend**: None (this is a notebook/script collection, not a distributable package)
- **PEP 621 metadata**: Project metadata in `[project]` table
- **Dependencies**: Managed by `uv`, lockfile in `uv.lock`
- **Note**: Runtime dependencies (numpy, pandas, scikit-learn, etc.) are not declared in pyproject.toml since this project uses conda environments defined in `installation/`. Only dev tooling is managed by uv.

### 2. Removed Legacy Files
No legacy build files existed (no setup.py, setup.cfg, or requirements.txt). The conda environment files in `installation/` are preserved as-is.

### 3. Source Layout
- **Layout**: Unchanged -- this is a notebook collection, not a package
- **Structure**: Numbered chapter directories (`01_machine_learning_for_trading/`, etc.) with Jupyter notebooks and supporting Python scripts
- **No src/ migration**: Not applicable for notebook collections

### 4. Tooling Configuration (in pyproject.toml)

#### Ruff (linting + formatting)
```toml
[tool.ruff]
line-length = 88
target-version = "py313"

[tool.ruff.lint]
select = ["E", "W", "F", "I", "UP", "B", "SIM", "C4", "RUF", "PERF", "TC", "PTH"]
ignore = ["E501"]

[tool.ruff.lint.per-file-ignores]
"tests/*" = ["S101"]
"__init__.py" = ["F401"]
```

#### Pyright (type checking)
```toml
[tool.pyright]
pythonVersion = "3.13"
typeCheckingMode = "basic"
```

#### Pytest
```toml
[tool.pytest.ini_options]
minversion = "9.0"
addopts = ["-ra", "-q", "--strict-markers", "--import-mode=importlib"]
testpaths = ["tests"]
pythonpath = ["src"]
xfail_strict = true
filterwarnings = ["error"]
```

### 5. Python Version
- `.python-version` set to `3.13`
- `requires-python = ">=3.13"` in pyproject.toml

## After Upstream Sync Checklist

When merging upstream changes into `feature/ayu_develop`:

1. **Delete re-added legacy files**: `setup.py`, `setup.cfg`, `requirements.txt`, `MANIFEST.in`, `poetry.lock` (if any appear)
2. **Check pyproject.toml**: Upstream may add a pyproject.toml. Keep `[tool.ruff]`, `[tool.pyright]`, `[tool.pytest]` sections intact.
3. **Re-lock**: Run `uv lock` to update `uv.lock` with any new/changed dependencies.
4. **Verify**: Run `uv sync`.

## Quick Commands

```bash
uv sync                                    # Install dev deps
uv run pytest                              # Run tests
uv run ruff check .                        # Lint
uv run ruff format .                       # Format
uv lock                                    # Re-generate lockfile
```

## Notes

- This project is a companion repository to the book "Machine Learning for Algorithmic Trading" by Stefan Jansen
- Heavy ML dependencies (numpy, pandas, tensorflow, etc.) are managed via conda environments in `installation/`, not via uv
- The pyproject.toml is used only for dev tooling (ruff, pyright, pytest) configuration
