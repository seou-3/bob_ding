# CI/CD Setup for Bob Ding

## Overview

Lightweight GitHub Actions CI workflows that run automated tests on every push.

## What Was Added

### 1. GitHub Actions Workflows

#### `.github/workflows/python-app.yml`

- **Purpose**: Main test suite runner
- **Triggers**: Push to main/master/dev branches, PRs to main/master
- **Python Versions**: 3.8, 3.9, 3.10, 3.11, 3.12
- **Tests Run**:
  - Smoke tests (`test.py`)
  - Ending tests (`test_endings.py`)
  - Secrets catalog display (`test_secrets.py`)
  - Import validation (`import main`)
- **Validation Job**:
  - File structure checks
  - Secret count validation (ensures ≥150 secrets)

#### `.github/workflows/python-package-conda.yml`

- **Purpose**: Cross-platform testing
- **Platforms**: Ubuntu, Windows, macOS
- **Python Versions**: 3.8, 3.12
- **Tests**:
  - Smoke tests
  - Ending tests
  - UTF-8 encoding validation (ensures horror symbols display correctly)

### 2. Improved Test Suite

#### `test.py` (New Smoke Test)

Replaced placeholder with comprehensive smoke tests:

- ✓ Constants validation (BASE_WORD, TRUE_ESCAPE, alphabet)
- ✓ Save structure validation
- ✓ Bob class initialization
- ✓ Secrets existence (155 secrets)
- ✓ Hallucinations content (155 auditory, 154 tactile)
- ✓ Word mutation attributes
- ✓ File save/load functionality
- ✓ Runtime argument parsing

All 8 tests pass successfully.

### 3. `.gitignore`

Added comprehensive ignore rules for:

- Runtime artifacts (`bob_ding.save`, `.bob_*` files)
- Test outputs (`test_input.txt`, replay logs)
- Python build artifacts
- Virtual environments
- IDE files
- Coverage reports

### 4. Documentation

Added **Testing** section to `README.md`:

- Commands to run each test suite
- CI/CD overview
- Test matrix details

## Running Tests Locally

```bash
# Quick validation
python3 test.py

# Full ending tests (takes ~30 seconds)
python3 test_endings.py

# View all 155 secrets
python3 test_secrets.py
```

## CI Behavior

### On Push

1. Runs smoke tests across 5 Python versions (3.8-3.12)
2. Validates all 16 major game endings
3. Cross-platform tests on Ubuntu, Windows, macOS
4. Checks file integrity and secret count

### On Pull Request

- Same as push, but only for PRs to main/master branches

## Test Results

Current status:

- ✅ Smoke tests: 8/8 passed
- ✅ Ending tests: 16/16 passed
- ✅ Cross-platform: Ubuntu ✓, Windows ✓, macOS ✓
- ✅ Python versions: 3.8-3.12 all supported

## Maintenance

### Adding New Tests

1. Add test functions to `test.py` or create new test files
2. Update workflow files to include new test commands
3. Run locally to validate before pushing

### Modifying CI Triggers

Edit workflow files:

- `on.push.branches` - controls which branches trigger CI
- `on.pull_request.branches` - controls PR targets
- `strategy.matrix.python-version` - Python versions to test

## Notes

- No external dependencies required (pure Python stdlib)
- Tests are deterministic and can run in parallel
- UTF-8 encoding validation ensures horror glyphs render correctly
- Secret count validation prevents accidental deletions
