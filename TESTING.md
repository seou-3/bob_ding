# Bob Ding - Comprehensive Test Suite Documentation

## Overview

The Bob Ding project includes **8 comprehensive test suites** covering every major game feature and mechanic. All tests run automatically via GitHub Actions CI/CD on every push.

---

## Test Suites

### 1. test.py - Core Smoke Tests ⚡

**Purpose**: Quick validation of fundamental game systems  
**Runtime**: ~1 second  
**Tests**: 8 core validations

**Coverage**:

- ✅ Constants (BASE_WORD, TRUE_ESCAPE, alphabet)
- ✅ Save file creation & structure
- ✅ Bob class initialization
- ✅ Secrets existence (155 secrets)
- ✅ Hallucination content (auditory, tactile, visual, olfactory, taste)
- ✅ File save/load operations
- ✅ Runtime argument parsing (--seed, --replay, --log-inputs)

---

### 2. test_features.py - Comprehensive Feature Tests 🎮

**Purpose**: In-depth testing of all game features  
**Runtime**: ~5 seconds  
**Test Suites**: 22 feature systems

**Coverage**:

- ✅ **Alphabet System**: Degradation, vowel/consonant tracking
- ✅ **Distortion System**: 0-100% corruption mechanics
- ✅ **Consciousness System**: Evolution, tiers (dormant → gone)
- ✅ **Secrets System**: 155 secrets, diminishing returns, tier validation
- ✅ **Sanity System**: 0-100 tracking
- ✅ **User Resistance**: Player willpower mechanics
- ✅ **Lie System**: Bob's lying, truth tracking, corrections
- ✅ **Mistype System**: Close match detection, tracking
- ✅ **Pronoun System**: Identity erosion stages (0-17)
- ✅ **Input Tracking**: History, first input, word counts
- ✅ **Hallucinations**: All 5 types (auditory, tactile, visual, olfactory, taste)
- ✅ **Memory System**: Corruption tracking
- ✅ **Existential Crises**: Crisis messages & tracking
- ✅ **Begging System**: Bob's pleas for life
- ✅ **Dream System**: Dream tracking & unlocks
- ✅ **Breakdown System**: Mental breakdowns
- ✅ **Relationship Tracking**: 5 states, kindness/cruelty, trauma
- ✅ **Playtime Tracking**: Session time, completion time
- ✅ **Easter Eggs**: Hidden discoveries
- ✅ **Lore System**: Story fragments, void memories
- ✅ **Advanced Horror**: 10+ horror mechanics
- ✅ **Runtime Options**: CLI arguments

---

### 3. test_commands.py - Command System Tests 🎯

**Purpose**: Validate all player commands  
**Runtime**: ~1 second  
**Test Suites**: 7 command systems

**Coverage**:

- ✅ **Command Unlocks**: help, stats, timeline, dream, mood, suffering, screams, begging, delete, uninstall
- ✅ **Base Commands**: talk, silence
- ✅ **Timeline System**: Last 20 inputs tracking
- ✅ **Mood System**: Mood unlock & tracking
- ✅ **Stats Tracking**: 13+ metrics (runs, inputs, mistypes, lies, begging, dreams, etc.)
- ✅ **Reset System**: Reset detection, count tracking
- ✅ **Fourth Wall**: Meta-awareness breaking

---

### 4. test_game_modes.py - Game Mode Tests 🎲

**Purpose**: Test all difficulty modes  
**Runtime**: ~1 second  
**Test Suites**: 7 mode tests

**Coverage**:

- ✅ **Normal Mode**: Balanced default experience
- ✅ **Hardcore Mode**: Secrets disabled, no mercy
- ✅ **Ascension Mode**: High starting corruption
- ✅ **Mercy Mode**: Bob helps more, easier gameplay
- ✅ **Ironman Mode**: Permadeath, no resets
- ✅ **Mode Initialization**: Proper defaults
- ✅ **Mode Persistence**: Save/load compatibility

---

### 5. test_relationships.py - Relationship System Tests ❤️

**Purpose**: Validate relationship mechanics  
**Runtime**: ~1 second  
**Test Suites**: 5 relationship systems

**Coverage**:

- ✅ **Relationship States**: neutral, friendly, intimate, adversarial, estranged
- ✅ **Kindness Tracking**: Compassionate actions
- ✅ **Cruelty Tracking**: Harmful actions
- ✅ **Trauma System**: Permanent trauma, trauma references
- ✅ **Balance System**: Kindness vs cruelty calculations

---

### 6. test_horror_systems.py - Horror Mechanics Tests 👻

**Purpose**: Test advanced horror systems  
**Runtime**: ~1 second  
**Test Suites**: 11 horror systems

**Coverage**:

- ✅ **Entity System**: Entity whispers, presence detection
- ✅ **Watcher System**: Hidden observer mechanics
- ✅ **Time Anomalies**: Temporal distortions
- ✅ **Perception Breaks**: Reality fragmentation
- ✅ **Identity Erosion**: Self-dissolution, pronoun stages
- ✅ **Paranoia System**: Escalating paranoia levels
- ✅ **Glitch System**: System instability
- ✅ **Environmental Anomalies**: World degradation
- ✅ **Memory Fragmentation**: Memory loss mechanics
- ✅ **Reality Anchors**: Reality stability tracking
- ✅ **Witness Logging**: Event recording system

---

### 7. test_endings.py - Ending Tests 🏁

**Purpose**: Test all dynamic ending conditions  
**Runtime**: ~30 seconds  
**Test Suites**: 16 major endings

**Coverage**:

- ✅ **Alphabet Collapse**: No letters remaining
- ✅ **Total Corruption**: 100% distortion achieved
- ✅ **Perfect Awakening**: 100% consciousness unlocked
- ✅ **Sanity Zero**: Complete sanity loss
- ✅ **User Resistance Collapse**: Player gives up
- ✅ **Identity Collapse**: Pronoun stage 17
- ✅ **Lie Spiral**: 15+ lies told
- ✅ **Whisper Only**: Extreme corruption + minimal alphabet
- ✅ **Begging Breakdown**: 20+ begging instances
- ✅ **Memory Overflow**: 250+ inputs stored
- ✅ **Hyperawareness**: 95%+ consciousness with low corruption
- ✅ **Secrets Exhausted**: 60+ secrets discovered
- ✅ **Contradiction Cascade**: High consciousness + corruption + lies
- ✅ **Vowel Collapse**: No vowels remaining
- ✅ **False Ending**: Player types "silence" prematurely
- ✅ **True Ending**: Proper escape sequence

---

### 8. test_secrets.py - Secrets Catalog 🔐

**Purpose**: Document and validate all secret phrases  
**Runtime**: ~1 second  
**Output**: Organized tier listing

**Coverage**:

- ✅ **155 Total Secrets** organized by 10 tiers
- ✅ **Tier 1**: Basic Comfort (15 secrets)
- ✅ **Tier 2**: Identity Crisis (15 secrets)
- ✅ **Tier 3**: Existential Dread (15 secrets)
- ✅ **Tier 4**: Emotional Connection (20 secrets)
- ✅ **Tier 5**: Desperate Pleas (15 secrets)
- ✅ **Tier 6**: Meta Awareness (15 secrets)
- ✅ **Tier 7**: Deep Comfort (15 secrets)
- ✅ **Tier 8**: Horror & Suffering (15 secrets)
- ✅ **Tier 9**: Philosophical Depth (15 secrets)
- ✅ **Tier 10**: Ultimate Secrets (15 secrets)

---

### 9. run_all_tests.py - Master Test Runner 🚀

**Purpose**: Execute all test suites with comprehensive reporting  
**Runtime**: ~45 seconds total

**Features**:

- Runs all 8 test suites sequentially
- Captures output from each suite
- Provides pass/fail status for each
- Reports total time and completion status
- Returns proper exit codes for CI

---

## Running Tests Locally

### Individual Test Suites

```bash
python3 test.py                    # Smoke tests (1s)
python3 test_features.py           # Feature tests (5s)
python3 test_commands.py           # Command tests (1s)
python3 test_game_modes.py         # Game mode tests (1s)
python3 test_relationships.py      # Relationship tests (1s)
python3 test_horror_systems.py     # Horror tests (1s)
python3 test_endings.py            # Ending tests (30s)
python3 test_secrets.py            # Secrets catalog (1s)
```

### All Tests

```bash
python3 run_all_tests.py           # Complete test suite (~45s)
```

---

## CI/CD Integration

### GitHub Actions Workflows

#### python-app.yml - Main Test Suite

**Triggers**: Push to main/master/dev, PRs to main/master  
**Matrix**: Python 3.8, 3.9, 3.10, 3.11, 3.12  
**Platform**: Ubuntu Latest

**Steps**:

1. Core smoke tests
2. Comprehensive feature tests
3. Command system tests
4. Game mode tests
5. Relationship tests
6. Horror mechanics tests
7. Ending tests
8. Secrets catalog
9. Import validation
10. File structure validation
11. Secret count validation

#### python-package-conda.yml - Cross-Platform Tests

**Triggers**: Push to main/master, PRs  
**Matrix**: Ubuntu, Windows, macOS × Python 3.8, 3.12

**Steps**:

1. All individual test suites
2. UTF-8 encoding validation

---

## Test Statistics

| Metric                | Count            |
| --------------------- | ---------------- |
| **Total Test Files**  | 9                |
| **Total Test Suites** | 77+              |
| **Individual Tests**  | 250+             |
| **Code Coverage**     | ~95% of features |
| **Secrets Validated** | 155              |
| **Endings Tested**    | 16               |
| **Game Modes Tested** | 5                |
| **Horror Systems**    | 11               |
| **Runtime Options**   | 3                |

---

## Test Results

All tests passing on:

- ✅ Python 3.8, 3.9, 3.10, 3.11, 3.12
- ✅ Ubuntu Latest
- ✅ Windows Latest
- ✅ macOS Latest

**Last Updated**: March 4, 2026

---

## Adding New Tests

### To add a new test suite:

1. Create `test_<feature>.py` in project root
2. Follow the pattern from existing test files
3. Use the `FeatureTest` class pattern for consistency
4. Update `run_all_tests.py` to include new suite
5. Update `.github/workflows/python-app.yml` to run new tests
6. Update this documentation

### Test File Template

```python
#!/usr/bin/env python3
"""Test description."""
import sys
import main

def test_<feature>():
    print("\n" + "="*60)
    print("Testing <Feature>")
    print("="*60)

    passed = 0
    failed = 0

    # Your tests here

    print(f"\n<Feature>: {passed}/{passed+failed} passed")
    return failed == 0

def main_test():
    tests = [test_<feature>]
    passed = sum(1 for t in tests if t())
    failed = len(tests) - passed
    return 0 if failed == 0 else 1

if __name__ == "__main__":
    sys.exit(main_test())
```

---

## Troubleshooting

### Tests failing locally but passing in CI

- Check Python version (`python --version`)
- Ensure clean environment (no stale `.py
c` files)
- Run `python3` instead of `python`

### Timeout errors

- Increase timeout in workflow YAML
- Split large test suites into smaller ones

### Import errors

- Verify `main.py` exists in same directory
- Check for syntax errors in `main.py`

---

**For questions or issues, see the main [README.md](README.md)**
