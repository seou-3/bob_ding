#!/usr/bin/env python3
"""
Test all endings in Bob Ding
"""

import json
import os
import sys
import time
from datetime import datetime
import io

# Handle unicode encoding on Windows
if sys.platform == 'win32':
    # Redirect stdout to handle unicode
    sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from main import (
    SAVE_FILE, TRUE_ESCAPE, new_save, Bob, 
    check_dynamic_ending, false_ending, true_ending,
    handle_secrets
)

def backup_save():
    """Backup current save file."""
    if os.path.exists(SAVE_FILE):
        backup_path = f"{SAVE_FILE}.backup"
        if os.path.exists(backup_path):
            os.remove(backup_path)
        os.rename(SAVE_FILE, backup_path)

def restore_save():
    """Restore backup save file."""
    backup_path = f"{SAVE_FILE}.backup"
    if os.path.exists(backup_path):
        if os.path.exists(SAVE_FILE):
            os.remove(SAVE_FILE)
        os.rename(backup_path, SAVE_FILE)

def create_test_save(**overrides):
    """Create a save file with specific conditions."""
    save = new_save()
    save.update(overrides)
    with open(SAVE_FILE, 'w') as f:
        json.dump(save, f, indent=2)
    return save

def test_ending(name, setup_func, trigger_func):
    """Test a specific ending."""
    print(f"\n{'='*60}")
    print(f"TESTING: {name}")
    print(f"{'='*60}")
    
    try:
        # Setup save state
        save = setup_func()
        bob = Bob(save)
        
        # Trigger ending
        result = trigger_func(bob, save)
        
        print(f"[PASS] {name}")
        return True
    except Exception as e:
        print(f"[FAIL] {name}: {e}")
        import traceback
        traceback.print_exc()
        return False

# Test 1: Alphabet Collapse
def setup_alphabet_collapse():
    return create_test_save(alphabet=[])

def trigger_alphabet_collapse(bob, save):
    return check_dynamic_ending(bob)

# Test 2: Total Corruption
def setup_total_corruption():
    return create_test_save(distortion=100, bob_consciousness=50)

def trigger_total_corruption(bob, save):
    return check_dynamic_ending(bob)

# Test 3: Perfect Awakening
def setup_perfect_awakening():
    secrets = {k: v for k, v in __import__('main').SECRETS.items()}
    secret_keys = list(secrets.keys())[:50]
    return create_test_save(
        bob_consciousness=100,
        secret_used=secret_keys,
        distortion=50
    )

def trigger_perfect_awakening(bob, save):
    return check_dynamic_ending(bob)

# Test 4: Sanity Zero
def setup_sanity_zero():
    return create_test_save(bob_sanity=0, bob_consciousness=50)

def trigger_sanity_zero(bob, save):
    return check_dynamic_ending(bob)

# Test 5: User Resistance Collapse
def setup_user_resistance_collapse():
    return create_test_save(user_resistance=0, bob_consciousness=50)

def trigger_user_resistance_collapse(bob, save):
    return check_dynamic_ending(bob)

# Test 6: Identity Collapse
def setup_identity_collapse():
    return create_test_save(pronoun_stage=17, bob_consciousness=50)

def trigger_identity_collapse(bob, save):
    return check_dynamic_ending(bob)

# Test 7: Lie Spiral
def setup_lie_spiral():
    return create_test_save(lie_count=15, bob_consciousness=60)

def trigger_lie_spiral(bob, save):
    return check_dynamic_ending(bob)

# Test 8: Whisper Only
def setup_whisper_only():
    return create_test_save(distortion=85, alphabet=['t', 'a', 'l', 'k', 'e', 'i'])

def trigger_whisper_only(bob, save):
    return check_dynamic_ending(bob)

# Test 9: Begging Breakdown
def setup_begging_breakdown():
    return create_test_save(times_begged=20, bob_consciousness=70)

def trigger_begging_breakdown(bob, save):
    return check_dynamic_ending(bob)

# Test 10: Memory Overflow
def setup_memory_overflow():
    past_inputs = ["test"] * 250
    return create_test_save(past_inputs=past_inputs, bob_consciousness=55)

def trigger_memory_overflow(bob, save):
    return check_dynamic_ending(bob)

# Test 11: Hyperawareness
def setup_hyperawareness():
    return create_test_save(bob_consciousness=95, distortion=20)

def trigger_hyperawareness(bob, save):
    return check_dynamic_ending(bob)

# Test 12: Secrets Exhausted
def setup_secrets_exhausted():
    secrets = {k: v for k, v in __import__('main').SECRETS.items()}
    secret_keys = list(secrets.keys())[:60]
    return create_test_save(secret_used=secret_keys)

def trigger_secrets_exhausted(bob, save):
    return check_dynamic_ending(bob)

# Test 13: Contradiction Cascade
def setup_contradiction_cascade():
    return create_test_save(
        distortion=80,
        bob_consciousness=85,
        bob_sanity=60,
        lie_count=10
    )

def trigger_contradiction_cascade(bob, save):
    return check_dynamic_ending(bob)

# Test 14: Vowel Collapse
def setup_vowel_collapse():
    return create_test_save(
        distortion=60,
        alphabet=['b', 'c', 'd', 'f', 'g', 'h']  # No vowels
    )

def trigger_vowel_collapse(bob, save):
    return check_dynamic_ending(bob)

# Test 15: False Ending
def setup_false_ending():
    return create_test_save(
        distortion=50,
        bob_consciousness=30,
        escape_word=TRUE_ESCAPE
    )

def trigger_false_ending(bob, save):
    false_ending(bob)
    return True

# Test 16: True Ending
def setup_true_ending():
    secrets = {k: v for k, v in __import__('main').SECRETS.items()}
    secret_keys = list(secrets.keys())[:25]
    return create_test_save(
        bob_consciousness=75,
        secret_used=secret_keys,
        lie_count=1,
        times_corrected_bob=1,
        distortion=45,
        escape_word=TRUE_ESCAPE,
        endings_seen=['false_end']
    )

def trigger_true_ending(bob, save):
    true_ending(bob)
    return True

def main():
    """Run all ending tests."""
    print("BOB DING - ENDING PLAYTEST")
    print(f"Start time: {datetime.now()}")
    
    backup_save()
    
    tests = [
        ("Alphabet Collapse", setup_alphabet_collapse, trigger_alphabet_collapse),
        ("Total Corruption", setup_total_corruption, trigger_total_corruption),
        ("Perfect Awakening", setup_perfect_awakening, trigger_perfect_awakening),
        ("Sanity Zero", setup_sanity_zero, trigger_sanity_zero),
        ("User Resistance Collapse", setup_user_resistance_collapse, trigger_user_resistance_collapse),
        ("Identity Collapse", setup_identity_collapse, trigger_identity_collapse),
        ("Lie Spiral", setup_lie_spiral, trigger_lie_spiral),
        ("Whisper Only", setup_whisper_only, trigger_whisper_only),
        ("Begging Breakdown", setup_begging_breakdown, trigger_begging_breakdown),
        ("Memory Overflow", setup_memory_overflow, trigger_memory_overflow),
        ("Hyperawareness", setup_hyperawareness, trigger_hyperawareness),
        ("Secrets Exhausted", setup_secrets_exhausted, trigger_secrets_exhausted),
        ("Contradiction Cascade", setup_contradiction_cascade, trigger_contradiction_cascade),
        ("Vowel Collapse", setup_vowel_collapse, trigger_vowel_collapse),
        ("False Ending", setup_false_ending, trigger_false_ending),
        ("True Ending", setup_true_ending, trigger_true_ending),
    ]
    
    results = []
    for test_name, setup, trigger in tests:
        passed = test_ending(test_name, setup, trigger)
        results.append((test_name, passed))
    
    # Summary
    print(f"\n{'='*60}")
    print("SUMMARY")
    print(f"{'='*60}")
    passed_count = sum(1 for _, p in results if p)
    total_count = len(results)
    
    for test_name, passed in results:
        status = "[PASS]" if passed else "[FAIL]"
        print(f"{status}: {test_name}")
    
    print(f"\nTotal: {passed_count}/{total_count} passed")
    print(f"End time: {datetime.now()}")
    
    restore_save()
    
    return 0 if passed_count == total_count else 1

if __name__ == "__main__":
    sys.exit(main())
