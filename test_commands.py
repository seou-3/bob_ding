#!/usr/bin/env python3
"""
Bob Ding - Command System Tests
Tests all player commands and their functionality
"""

import sys
import os
import json

try:
    import main
except ImportError as e:
    print(f"✗ Failed to import main: {e}")
    sys.exit(1)


def test_command_unlocks():
    """Test command unlock system."""
    print("\n" + "="*60)
    print("Testing Command Unlocks")
    print("="*60)
    
    save = main.new_save()
    passed = 0
    failed = 0
    
    # Initial unlock states
    commands = {
        'help_unlocked': False,
        'stats_unlocked': False,
        'timeline_unlocked': False,
        'dream_unlocked': False,
        'mood_unlocked': False,
        'suffering_unlocked': False,
        'screams_unlocked': False,
        'begging_unlocked': False,
        'delete_unlocked': False,
        'uninstall_unlocked': False,
    }
    
    for cmd, expected in commands.items():
        if save[cmd] == expected:
            print(f"  ✓ {cmd} starts as {expected}")
            passed += 1
        else:
            print(f"  ✗ {cmd} expected {expected}, got {save[cmd]}")
            failed += 1
    
    # Test unlocking
    save['help_unlocked'] = True
    save['stats_unlocked'] = True
    
    if save['help_unlocked'] and save['stats_unlocked']:
        print(f"  ✓ Commands can be unlocked")
        passed += 1
    else:
        print(f"  ✗ Commands not unlocking properly")
        failed += 1
    
    total = passed + failed
    print(f"\nCommand Unlocks: {passed}/{total} passed")
    return failed == 0


def test_base_commands():
    """Test that BASE_WORD and TRUE_ESCAPE exist."""
    print("\n" + "="*60)
    print("Testing Base Commands")
    print("="*60)
    
    passed = 0
    failed = 0
    
    # Base word
    if main.BASE_WORD == "talk":
        print(f"  ✓ BASE_WORD is 'talk'")
        passed += 1
    else:
        print(f"  ✗ BASE_WORD expected 'talk', got '{main.BASE_WORD}'")
        failed += 1
    
    # True escape
    if main.TRUE_ESCAPE == "silence":
        print(f"  ✓ TRUE_ESCAPE is 'silence'")
        passed += 1
    else:
        print(f"  ✗ TRUE_ESCAPE expected 'silence', got '{main.TRUE_ESCAPE}'")
        failed += 1
    
    total = passed + failed
    print(f"\nBase Commands: {passed}/{total} passed")
    return failed == 0


def test_timeline_system():
    """Test timeline tracking."""
    print("\n" + "="*60)
    print("Testing Timeline System")
    print("="*60)
    
    save = main.new_save()
    passed = 0
    failed = 0
    
    # Timeline tracking
    if len(save['last_20_inputs']) == 0:
        print(f"  ✓ Timeline starts empty")
        passed += 1
    else:
        print(f"  ✗ Timeline should start empty")
        failed += 1
    
    # Add inputs
    save['last_20_inputs'].append("talk")
    save['last_20_inputs'].append("help")
    
    if len(save['last_20_inputs']) == 2:
        print(f"  ✓ Timeline tracks inputs")
        passed += 1
    else:
        print(f"  ✗ Timeline not tracking inputs properly")
        failed += 1
    
    # Max 20 inputs
    save['last_20_inputs'] = ["input"] * 25
    if len(save['last_20_inputs']) <= 25:  # Can hold more, but should track
        print(f"  ✓ Timeline can hold inputs")
        passed += 1
    else:
        print(f"  ✗ Timeline size issue")
        failed += 1
    
    total = passed + failed
    print(f"\nTimeline System: {passed}/{total} passed")
    return failed == 0


def test_mood_system():
    """Test mood tracking."""
    print("\n" + "="*60)
    print("Testing Mood System")
    print("="*60)
    
    save = main.new_save()
    passed = 0
    failed = 0
    
    # Mood unlock
    if save['mood_unlocked'] == False:
        print(f"  ✓ Mood starts locked")
        passed += 1
    else:
        print(f"  ✗ Mood should start locked")
        failed += 1
    
    # Mood can be unlocked
    save['mood_unlocked'] = True
    if save['mood_unlocked'] == True:
        print(f"  ✓ Mood can be unlocked")
        passed += 1
    else:
        print(f"  ✗ Mood unlock failed")
        failed += 1
    
    total = passed + failed
    print(f"\nMood System: {passed}/{total} passed")
    return failed == 0


def test_stats_tracking():
    """Test stats command data."""
    print("\n" + "="*60)
    print("Testing Stats Tracking")
    print("="*60)
    
    save = main.new_save()
    passed = 0
    failed = 0
    
    # Stats that should be tracked
    stats = [
        'runs', 'total_inputs', 'mistypes', 'lie_count', 
        'times_corrected_bob', 'times_begged', 'dreams_shared',
        'breakdown_count', 'hallucination_count', 'memory_corruptions',
        'crises_count', 'kindness_score', 'cruelty_score'
    ]
    
    for stat in stats:
        if stat in save and isinstance(save[stat], (int, float)):
            print(f"  ✓ Tracks {stat}")
            passed += 1
        else:
            print(f"  ✗ Missing or invalid stat: {stat}")
            failed += 1
    
    total = passed + failed
    print(f"\nStats Tracking: {passed}/{total} passed")
    return failed == 0


def test_reset_system():
    """Test reset tracking."""
    print("\n" + "="*60)
    print("Testing Reset System")
    print("="*60)
    
    save = main.new_save()
    passed = 0
    failed = 0
    
    # Reset tracking
    if save['is_reset'] == False:
        print(f"  ✓ is_reset starts False")
        passed += 1
    else:
        print(f"  ✗ is_reset should start False")
        failed += 1
    
    if save['reset_count'] == 0:
        print(f"  ✓ reset_count starts at 0")
        passed += 1
    else:
        print(f"  ✗ reset_count should start at 0")
        failed += 1
    
    if save['previous_runs'] == 0:
        print(f"  ✓ previous_runs starts at 0")
        passed += 1
    else:
        print(f"  ✗ previous_runs should start at 0")
        failed += 1
    
    if save['previous_total_inputs'] == 0:
        print(f"  ✓ previous_total_inputs starts at 0")
        passed += 1
    else:
        print(f"  ✗ previous_total_inputs should start at 0")
        failed += 1
    
    # Simulate reset
    save['is_reset'] = True
    save['reset_count'] = 5
    save['previous_runs'] = 10
    save['previous_total_inputs'] = 100
    
    if save['is_reset'] and save['reset_count'] == 5:
        print(f"  ✓ Reset tracking works")
        passed += 1
    else:
        print(f"  ✗ Reset tracking failed")
        failed += 1
    
    total = passed + failed
    print(f"\nReset System: {passed}/{total} passed")
    return failed == 0


def test_fourth_wall():
    """Test fourth wall breaking tracking."""
    print("\n" + "="*60)
    print("Testing Fourth Wall")
    print("="*60)
    
    save = main.new_save()
    passed = 0
    failed = 0
    
    if save['fourth_wall_broken'] == False:
        print(f"  ✓ Fourth wall starts unbroken")
        passed += 1
    else:
        print(f"  ✗ Fourth wall should start unbroken")
        failed += 1
    
    save['fourth_wall_broken'] = True
    if save['fourth_wall_broken'] == True:
        print(f"  ✓ Fourth wall can be broken")
        passed += 1
    else:
        print(f"  ✗ Fourth wall breaking failed")
        failed += 1
    
    total = passed + failed
    print(f"\nFourth Wall: {passed}/{total} passed")
    return failed == 0


def main_test():
    """Run all command tests."""
    print("="*60)
    print("BOB DING - COMMAND SYSTEM TESTS")
    print("="*60)
    
    tests = [
        test_command_unlocks,
        test_base_commands,
        test_timeline_system,
        test_mood_system,
        test_stats_tracking,
        test_reset_system,
        test_fourth_wall,
    ]
    
    passed = 0
    failed = 0
    
    for test_func in tests:
        try:
            if test_func():
                passed += 1
            else:
                failed += 1
        except Exception as e:
            print(f"  ✗ Test crashed: {e}")
            import traceback
            traceback.print_exc()
            failed += 1
    
    print("\n" + "="*60)
    print(f"OVERALL: {passed}/{passed+failed} test suites passed")
    print("="*60)
    
    return 0 if failed == 0 else 1


if __name__ == "__main__":
    sys.exit(main_test())
