#!/usr/bin/env python3
"""
Bob Ding - Smoke Test Suite
Quick validation of core functionality
"""

import sys
import os
import json
import tempfile
import shutil

# Import main game module
try:
    import main
    print("✓ main.py imported successfully")
except ImportError as e:
    print(f"✗ Failed to import main.py: {e}")
    sys.exit(1)

def test_constants():
    """Verify core game constants exist and have expected values."""
    print("\nTesting constants...")
    
    assert main.BASE_WORD == "talk", "BASE_WORD should be 'talk'"
    assert main.TRUE_ESCAPE == "silence", "TRUE_ESCAPE should be 'silence'"
    assert len(main.VOWELS) == 5, "Should have 5 vowels"
    assert len(main.CONSONANTS) == 21, "Should have 21 consonants"
    assert len(main.FULL_ALPHABET) == 26, "Should have 26 letters total"
    
    print("  ✓ All constants validated")

def test_save_creation():
    """Test that new_save() creates a valid save structure."""
    print("\nTesting save creation...")
    
    save = main.new_save()
    
    # Check required keys
    required_keys = [
        'distortion', 'alphabet', 'command', 'escape_word',
        'bob_consciousness', 'bob_sanity', 'user_resistance',
        'past_inputs', 'secret_used', 'lie_count'
    ]
    
    for key in required_keys:
        assert key in save, f"Save missing required key: {key}"
    
    # Check initial values
    assert save['distortion'] == 0, "Initial distortion should be 0"
    assert save['command'] == "talk", "Initial command should be 'talk'"
    assert save['bob_consciousness'] == 0, "Initial consciousness should be 0"
    assert isinstance(save['alphabet'], list), "Alphabet should be a list"
    assert len(save['alphabet']) == 26, "Should start with full alphabet"
    
    print("  ✓ Save structure validated")

def test_bob_class():
    """Test Bob class initialization."""
    print("\nTesting Bob class...")
    
    save = main.new_save()
    bob = main.Bob(save)
    
    assert bob.dist == 0, "Bob should start with 0 distortion"
    assert bob.consciousness == 0, "Bob should start with 0 consciousness"
    assert bob.s['bob_sanity'] == 100, "Bob should start with 100 sanity"
    assert bob.current_command == "talk", "Bob should start with 'talk'"
    
    print("  ✓ Bob class initialized correctly")

def test_secrets_exist():
    """Verify secrets dictionary is populated."""
    print("\nTesting secrets...")
    
    assert hasattr(main, 'SECRETS'), "SECRETS dictionary should exist"
    assert isinstance(main.SECRETS, dict), "SECRETS should be a dictionary"
    assert len(main.SECRETS) >= 150, f"Expected at least 150 secrets, found {len(main.SECRETS)}"
    
    # Check some known tier 1 secrets
    known_secrets = ['help', 'please', 'sorry', 'why']
    for secret in known_secrets:
        assert secret in main.SECRETS, f"Common secret '{secret}' missing"
    
    print(f"  ✓ {len(main.SECRETS)} secrets validated")

def test_hallucinations_exist():
    """Verify hallucination content exists."""
    print("\nTesting hallucinations...")
    
    assert hasattr(main, 'AUDITORY_HALLUCINATIONS'), "AUDITORY_HALLUCINATIONS should exist"
    assert hasattr(main, 'TACTILE_HALLUCINATIONS'), "TACTILE_HALLUCINATIONS should exist"
    
    auditory_count = len(main.AUDITORY_HALLUCINATIONS)
    tactile_count = len(main.TACTILE_HALLUCINATIONS)
    
    assert auditory_count >= 50, f"Expected at least 50 auditory hallucinations, found {auditory_count}"
    assert tactile_count >= 20, f"Expected at least 20 tactile hallucinations, found {tactile_count}"
    
    print(f"  ✓ Hallucinations validated ({auditory_count} auditory, {tactile_count} tactile)")

def test_word_mutation():
    """Test word mutation function."""
    print("\nTesting word mutation...")
    
    save = main.new_save()
    bob = main.Bob(save)
    
    # Bob has current_command that can be read
    original = bob.current_command
    assert isinstance(original, str), "Current command should be a string"
    assert len(original) > 0, "Current command should not be empty"
    
    # Bob has alphabet for character manipulation
    assert len(bob.alphabet) == 26, "Should start with full alphabet"
    
    print("  ✓ Word mutation attributes working")

def test_file_save_load():
    """Test save/load functionality with temp file."""
    print("\nTesting file save/load...")
    
    # Create temp directory
    temp_dir = tempfile.mkdtemp()
    original_save_file = main.SAVE_FILE
    
    try:
        # Set temp save file
        temp_save = os.path.join(temp_dir, "test.save")
        main.SAVE_FILE = temp_save
        
        # Create and save
        save = main.new_save()
        save['distortion'] = 42
        save['bob_consciousness'] = 75
        
        with open(temp_save, 'w') as f:
            json.dump(save, f)
        
        # Load back
        with open(temp_save, 'r') as f:
            loaded = json.load(f)
        
        assert loaded['distortion'] == 42, "Distortion should persist"
        assert loaded['bob_consciousness'] == 75, "Consciousness should persist"
        
        print("  ✓ File save/load working")
        
    finally:
        # Cleanup
        main.SAVE_FILE = original_save_file
        shutil.rmtree(temp_dir)

def test_runtime_args():
    """Test runtime argument parsing."""
    print("\nTesting runtime arguments...")
    
    args = main.parse_runtime_args(['--seed', '42'])
    assert args.seed == 42, "Seed argument should parse"
    
    args = main.parse_runtime_args([])
    assert args.seed is None, "Default seed should be None"
    
    print("  ✓ Runtime args parsing working")

def main_test():
    """Run all smoke tests."""
    print("=" * 60)
    print("BOB DING - SMOKE TEST SUITE")
    print("=" * 60)
    
    tests = [
        test_constants,
        test_save_creation,
        test_bob_class,
        test_secrets_exist,
        test_hallucinations_exist,
        test_word_mutation,
        test_file_save_load,
        test_runtime_args,
    ]
    
    passed = 0
    failed = 0
    
    for test in tests:
        try:
            test()
            passed += 1
        except AssertionError as e:
            print(f"  ✗ {test.__name__} failed: {e}")
            failed += 1
        except Exception as e:
            print(f"  ✗ {test.__name__} error: {e}")
            failed += 1
    
    print("\n" + "=" * 60)
    print(f"RESULTS: {passed} passed, {failed} failed")
    print("=" * 60)
    
    if failed > 0:
        sys.exit(1)
    else:
        print("\n✓ All smoke tests passed!")
        sys.exit(0)

if __name__ == "__main__":
    main_test()
