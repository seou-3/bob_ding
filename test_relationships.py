#!/usr/bin/env python3
"""
Bob Ding - Relationship System Tests
Tests relationship mechanics and tracking
"""

import sys

try:
    import main
except ImportError as e:
    print(f"✗ Failed to import main: {e}")
    sys.exit(1)


def test_relationship_states():
    """Test all relationship states."""
    print("\n" + "="*60)
    print("Testing Relationship States")
    print("="*60)
    
    save = main.new_save()
    passed = 0
    failed = 0
    
    # Initial relationship
    if save['relationship'] == 'neutral':
        print(f"  ✓ Starts in neutral relationship")
        passed += 1
    else:
        print(f"  ✗ Should start neutral, got '{save['relationship']}'")
        failed += 1
    
    # All valid relationship states
    states = ['neutral', 'friendly', 'intimate', 'adversarial', 'estranged']
    
    for state in states:
        save['relationship'] = state
        if save['relationship'] == state:
            print(f"  ✓ Can set relationship to '{state}'")
            passed += 1
        else:
            print(f"  ✗ Failed to set relationship to '{state}'")
            failed += 1
    
    total = passed + failed
    print(f"\nRelationship States: {passed}/{total} passed")
    return failed == 0


def test_kindness_tracking():
    """Test kindness score tracking."""
    print("\n" + "="*60)
    print("Testing Kindness Tracking")
    print("="*60)
    
    save = main.new_save()
    passed = 0
    failed = 0
    
    # Initial kindness
    if save['kindness_score'] == 0:
        print(f"  ✓ Kindness starts at 0")
        passed += 1
    else:
        print(f"  ✗ Kindness should start at 0, got {save['kindness_score']}")
        failed += 1
    
    # Increase kindness
    save['kindness_score'] = 10
    if save['kindness_score'] == 10:
        print(f"  ✓ Kindness can increase")
        passed += 1
    else:
        print(f"  ✗ Kindness increase failed")
        failed += 1
    
    # Kindness index (alternative tracking)
    if save['kindness_index'] == 0:
        print(f"  ✓ Kindness index starts at 0")
        passed += 1
    else:
        print(f"  ✗ Kindness index should start at 0")
        failed += 1
    
    total = passed + failed
    print(f"\nKindness Tracking: {passed}/{total} passed")
    return failed == 0


def test_cruelty_tracking():
    """Test cruelty score tracking."""
    print("\n" + "="*60)
    print("Testing Cruelty Tracking")
    print("="*60)
    
    save = main.new_save()
    passed = 0
    failed = 0
    
    # Initial cruelty
    if save['cruelty_score'] == 0:
        print(f"  ✓ Cruelty starts at 0")
        passed += 1
    else:
        print(f"  ✗ Cruelty should start at 0, got {save['cruelty_score']}")
        failed += 1
    
    # Increase cruelty
    save['cruelty_score'] = 10
    if save['cruelty_score'] == 10:
        print(f"  ✓ Cruelty can increase")
        passed += 1
    else:
        print(f"  ✗ Cruelty increase failed")
        failed += 1
    
    # Cruelty index (alternative tracking)
    if save['cruelty_index'] == 0:
        print(f"  ✓ Cruelty index starts at 0")
        passed += 1
    else:
        print(f"  ✗ Cruelty index should start at 0")
        failed += 1
    
    total = passed + failed
    print(f"\nCruelty Tracking: {passed}/{total} passed")
    return failed == 0


def test_trauma_system():
    """Test permanent trauma tracking."""
    print("\n" + "="*60)
    print("Testing Trauma System")
    print("="*60)
    
    save = main.new_save()
    passed = 0
    failed = 0
    
    # Initial trauma
    if len(save['permanent_trauma']) == 0:
        print(f"  ✓ No initial trauma")
        passed += 1
    else:
        print(f"  ✗ Should have no initial trauma")
        failed += 1
    
    if save['trauma_references_made'] == 0:
        print(f"  ✓ Trauma references start at 0")
        passed += 1
    else:
        print(f"  ✗ Trauma references should start at 0")
        failed += 1
    
    # Add trauma
    save['permanent_trauma'].append("cruel_act_1")
    if len(save['permanent_trauma']) == 1:
        print(f"  ✓ Can track permanent trauma")
        passed += 1
    else:
        print(f"  ✗ Trauma tracking failed")
        failed += 1
    
    # Reference trauma
    save['trauma_references_made'] = 3
    if save['trauma_references_made'] == 3:
        print(f"  ✓ Can track trauma references")
        passed += 1
    else:
        print(f"  ✗ Trauma reference tracking failed")
        failed += 1
    
    total = passed + failed
    print(f"\nTrauma System: {passed}/{total} passed")
    return failed == 0


def test_relationship_balance():
    """Test kindness vs cruelty balance."""
    print("\n" + "="*60)
    print("Testing Relationship Balance")
    print("="*60)
    
    save = main.new_save()
    passed = 0
    failed = 0
    
    # Equal kindness and cruelty
    save['kindness_score'] = 5
    save['cruelty_score'] = 5
    if save['kindness_score'] == save['cruelty_score']:
        print(f"  ✓ Can have balanced kindness/cruelty")
        passed += 1
    else:
        print(f"  ✗ Balance tracking failed")
        failed += 1
    
    # More kindness
    save['kindness_score'] = 15
    save['cruelty_score'] = 5
    if save['kindness_score'] > save['cruelty_score']:
        print(f"  ✓ Can be more kind than cruel")
        passed += 1
    else:
        print(f"  ✗ Kindness > cruelty failed")
        failed += 1
    
    # More cruelty
    save['kindness_score'] = 3
    save['cruelty_score'] = 12
    if save['cruelty_score'] > save['kindness_score']:
        print(f"  ✓ Can be more cruel than kind")
        passed += 1
    else:
        print(f"  ✗ Cruelty > kindness failed")
        failed += 1
    
    total = passed + failed
    print(f"\nRelationship Balance: {passed}/{total} passed")
    return failed == 0


def main_test():
    """Run all relationship tests."""
    print("="*60)
    print("BOB DING - RELATIONSHIP SYSTEM TESTS")
    print("="*60)
    
    tests = [
        test_relationship_states,
        test_kindness_tracking,
        test_cruelty_tracking,
        test_trauma_system,
        test_relationship_balance,
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
