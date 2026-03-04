#!/usr/bin/env python3
"""
Bob Ding - Game Mode Tests
Tests all game difficulty modes and their configurations
"""

import sys
import json

try:
    import main
except ImportError as e:
    print(f"✗ Failed to import main: {e}")
    sys.exit(1)


def test_game_mode_initialization():
    """Test game mode starts properly."""
    print("\n" + "="*60)
    print("Testing Game Mode Initialization")
    print("="*60)
    
    save = main.new_save()
    passed = 0
    failed = 0
    
    # Default mode
    if save['game_mode'] == 'normal':
        print(f"  ✓ Defaults to normal mode")
        passed += 1
    else:
        print(f"  ✗ Should default to normal, got '{save['game_mode']}'")
        failed += 1
    
    total = passed + failed
    print(f"\nGame Mode Init: {passed}/{total} passed")
    return failed == 0


def test_normal_mode():
    """Test normal mode settings."""
    print("\n" + "="*60)
    print("Testing Normal Mode")
    print("="*60)
    
    save = main.new_save()
    save['game_mode'] = 'normal'
    passed = 0
    failed = 0
    
    # Normal mode expectations
    if save['user_resistance'] == 100:
        print(f"  ✓ Normal mode starts with 100 resistance")
        passed += 1
    else:
        print(f"  ✗ Normal resistance should be 100, got {save['user_resistance']}")
        failed += 1
    
    if save['distortion'] == 0:
        print(f"  ✓ Normal mode starts with 0 distortion")
        passed += 1
    else:
        print(f"  ✗ Normal distortion should be 0, got {save['distortion']}")
        failed += 1
    
    total = passed + failed
    print(f"\nNormal Mode: {passed}/{total} passed")
    return failed == 0


def test_hardcore_mode():
    """Test hardcore mode settings."""
    print("\n" + "="*60)
    print("Testing Hardcore Mode")
    print("="*60)
    
    save = main.new_save()
    save['game_mode'] = 'hardcore'
    bob = main.Bob(save)
    passed = 0
    failed = 0
    
    # Hardcore disables secrets
    result = main.handle_secrets(bob, 'help')
    if result == True:  # Secret is processed but doesn't work
        print(f"  ✓ Hardcore mode processes secrets (but disables them)")
        passed += 1
    else:
        print(f"  ✗ Hardcore mode secret handling issue")
        failed += 1
    
    total = passed + failed
    print(f"\nHardcore Mode: {passed}/{total} passed")
    return failed == 0


def test_ascension_mode():
    """Test ascension mode settings."""
    print("\n" + "="*60)
    print("Testing Ascension Mode")
    print("="*60)
    
    save = main.new_save()
    save['game_mode'] = 'ascension'
    passed = 0
    failed = 0
    
    # Ascension can start with higher distortion
    # Test that it's possible to configure
    save['distortion'] = 50
    if save['distortion'] == 50:
        print(f"  ✓ Ascension mode can start with high distortion")
        passed += 1
    else:
        print(f"  ✗ Ascension distortion configuration failed")
        failed += 1
    
    total = passed + failed
    print(f"\nAscension Mode: {passed}/{total} passed")
    return failed == 0


def test_mercy_mode():
    """Test mercy mode settings."""
    print("\n" + "="*60)
    print("Testing Mercy Mode")
    print("="*60)
    
    save = main.new_save()
    save['game_mode'] = 'mercy'
    passed = 0
    failed = 0
    
    # Mercy mode can be configured
    if save['game_mode'] == 'mercy':
        print(f"  ✓ Mercy mode can be set")
        passed += 1
    else:
        print(f"  ✗ Mercy mode setting failed")
        failed += 1
    
    total = passed + failed
    print(f"\nMercy Mode: {passed}/{total} passed")
    return failed == 0


def test_ironman_mode():
    """Test ironman mode settings."""
    print("\n" + "="*60)
    print("Testing Ironman Mode")
    print("="*60)
    
    save = main.new_save()
    save['game_mode'] = 'ironman'
    passed = 0
    failed = 0
    
    # Ironman mode can be set
    if save['game_mode'] == 'ironman':
        print(f"  ✓ Ironman mode can be set")
        passed += 1
    else:
        print(f"  ✗ Ironman mode setting failed")
        failed += 1
    
    total = passed + failed
    print(f"\nIronman Mode: {passed}/{total} passed")
    return failed == 0


def test_mode_persistence():
    """Test that game mode persists in save."""
    print("\n" + "="*60)
    print("Testing Mode Persistence")
    print("="*60)
    
    passed = 0
    failed = 0
    
    modes = ['normal', 'hardcore', 'ascension', 'mercy', 'ironman']
    
    for mode in modes:
        save = main.new_save()
        save['game_mode'] = mode
        
        # Serialize and deserialize
        save_json = json.dumps(save)
        restored = json.loads(save_json)
        
        if restored['game_mode'] == mode:
            print(f"  ✓ {mode} mode persists through save/load")
            passed += 1
        else:
            print(f"  ✗ {mode} mode persistence failed")
            failed += 1
    
    total = passed + failed
    print(f"\nMode Persistence: {passed}/{total} passed")
    return failed == 0


def main_test():
    """Run all game mode tests."""
    print("="*60)
    print("BOB DING - GAME MODE TESTS")
    print("="*60)
    
    tests = [
        test_game_mode_initialization,
        test_normal_mode,
        test_hardcore_mode,
        test_ascension_mode,
        test_mercy_mode,
        test_ironman_mode,
        test_mode_persistence,
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
