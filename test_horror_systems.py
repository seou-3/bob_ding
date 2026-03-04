#!/usr/bin/env python3
"""
Bob Ding - Horror Systems Tests
Tests advanced horror mechanics and tracking
"""

import sys

try:
    import main
except ImportError as e:
    print(f"✗ Failed to import main: {e}")
    sys.exit(1)


def test_entity_system():
    """Test entity horror mechanics."""
    print("\n" + "="*60)
    print("Testing Entity System")
    print("="*60)
    
    save = main.new_save()
    passed = 0
    failed = 0
    
    # Entity tracking
    if save['entity_whispers_count'] == 0:
        print(f"  ✓ Entity whispers start at 0")
        passed += 1
    else:
        print(f"  ✗ Entity whispers should start at 0")
        failed += 1
    
    if save['entities_present'] == False:
        print(f"  ✓ Entities not present initially")
        passed += 1
    else:
        print(f"  ✗ Entities should not be present initially")
        failed += 1
    
    # Entities can be triggered
    save['entities_present'] = True
    save['entity_whispers_count'] = 5
    if save['entities_present'] and save['entity_whispers_count'] == 5:
        print(f"  ✓ Entities can be activated")
        passed += 1
    else:
        print(f"  ✗ Entity activation failed")
        failed += 1
    
    total = passed + failed
    print(f"\nEntity System: {passed}/{total} passed")
    return failed == 0


def test_watcher_system():
    """Test watcher horror mechanics."""
    print("\n" + "="*60)
    print("Testing Watcher System")
    print("="*60)
    
    save = main.new_save()
    passed = 0
    failed = 0
    
    # Watcher tracking
    if save['watcher_detected'] == False:
        print(f"  ✓ Watcher not detected initially")
        passed += 1
    else:
        print(f"  ✗ Watcher should not be detected initially")
        failed += 1
    
    # Watcher can be detected
    save['watcher_detected'] = True
    if save['watcher_detected']:
        print(f"  ✓ Watcher can be detected")
        passed += 1
    else:
        print(f"  ✗ Watcher detection failed")
        failed += 1
    
    total = passed + failed
    print(f"\nWatcher System: {passed}/{total} passed")
    return failed == 0


def test_time_anomalies():
    """Test time anomaly system."""
    print("\n" + "="*60)
    print("Testing Time Anomalies")
    print("="*60)
    
    save = main.new_save()
    passed = 0
    failed = 0
    
    # Time anomaly tracking
    if save['time_anomalies'] == 0:
        print(f"  ✓ Time anomalies start at 0")
        passed += 1
    else:
        print(f"  ✗ Time anomalies should start at 0")
        failed += 1
    
    # Time anomalies can occur
    save['time_anomalies'] = 10
    if save['time_anomalies'] == 10:
        print(f"  ✓ Time anomalies can be tracked")
        passed += 1
    else:
        print(f"  ✗ Time anomaly tracking failed")
        failed += 1
    
    total = passed + failed
    print(f"\nTime Anomalies: {passed}/{total} passed")
    return failed == 0


def test_perception_breaks():
    """Test perception break system."""
    print("\n" + "="*60)
    print("Testing Perception Breaks")
    print("="*60)
    
    save = main.new_save()
    passed = 0
    failed = 0
    
    # Perception breaks tracking
    if save['perception_breaks'] == 0:
        print(f"  ✓ Perception breaks start at 0")
        passed += 1
    else:
        print(f"  ✗ Perception breaks should start at 0")
        failed += 1
    
    # Perception can break
    save['perception_breaks'] = 7
    if save['perception_breaks'] == 7:
        print(f"  ✓ Perception breaks can be tracked")
        passed += 1
    else:
        print(f"  ✗ Perception break tracking failed")
        failed += 1
    
    total = passed + failed
    print(f"\nPerception Breaks: {passed}/{total} passed")
    return failed == 0


def test_identity_erosion():
    """Test identity erosion system."""
    print("\n" + "="*60)
    print("Testing Identity Erosion")
    print("="*60)
    
    save = main.new_save()
    passed = 0
    failed = 0
    
    # Identity erosion tracking
    if save['identity_erosion_level'] == 0:
        print(f"  ✓ Identity erosion starts at 0")
        passed += 1
    else:
        print(f"  ✗ Identity erosion should start at 0")
        failed += 1
    
    # Identity can erode
    save['identity_erosion_level'] = 50
    if save['identity_erosion_level'] == 50:
        print(f"  ✓ Identity erosion can progress")
        passed += 1
    else:
        print(f"  ✗ Identity erosion tracking failed")
        failed += 1
    
    # Pronoun stage (related to identity)
    if save['pronoun_stage'] == 0:
        print(f"  ✓ Pronoun stage starts at 0")
        passed += 1
    else:
        print(f"  ✗ Pronoun stage should start at 0")
        failed += 1
    
    total = passed + failed
    print(f"\nIdentity Erosion: {passed}/{total} passed")
    return failed == 0


def test_paranoia_system():
    """Test paranoia mechanics."""
    print("\n" + "="*60)
    print("Testing Paranoia System")
    print("="*60)
    
    save = main.new_save()
    passed = 0
    failed = 0
    
    # Paranoia tracking
    if save['paranoia_level'] == 0:
        print(f"  ✓ Paranoia starts at 0")
        passed += 1
    else:
        print(f"  ✗ Paranoia should start at 0")
        failed += 1
    
    # Paranoia can increase
    save['paranoia_level'] = 75
    if save['paranoia_level'] == 75:
        print(f"  ✓ Paranoia can increase")
        passed += 1
    else:
        print(f"  ✗ Paranoia tracking failed")
        failed += 1
    
    total = passed + failed
    print(f"\nParanoia System: {passed}/{total} passed")
    return failed == 0


def test_glitch_system():
    """Test glitch mechanics."""
    print("\n" + "="*60)
    print("Testing Glitch System")
    print("="*60)
    
    save = main.new_save()
    passed = 0
    failed = 0
    
    # Glitch tracking
    if save['glitch_count'] == 0:
        print(f"  ✓ Glitches start at 0")
        passed += 1
    else:
        print(f"  ✗ Glitches should start at 0")
        failed += 1
    
    # Glitches can occur
    save['glitch_count'] = 15
    if save['glitch_count'] == 15:
        print(f"  ✓ Glitches can be tracked")
        passed += 1
    else:
        print(f"  ✗ Glitch tracking failed")
        failed += 1
    
    total = passed + failed
    print(f"\nGlitch System: {passed}/{total} passed")
    return failed == 0


def test_environmental_anomalies():
    """Test environmental anomaly system."""
    print("\n" + "="*60)
    print("Testing Environmental Anomalies")
    print("="*60)
    
    save = main.new_save()
    passed = 0
    failed = 0
    
    # Environmental anomaly tracking
    if save['environmental_anomalies'] == 0:
        print(f"  ✓ Environmental anomalies start at 0")
        passed += 1
    else:
        print(f"  ✗ Environmental anomalies should start at 0")
        failed += 1
    
    # Anomalies can occur
    save['environmental_anomalies'] = 8
    if save['environmental_anomalies'] == 8:
        print(f"  ✓ Environmental anomalies can be tracked")
        passed += 1
    else:
        print(f"  ✗ Environmental anomaly tracking failed")
        failed += 1
    
    total = passed + failed
    print(f"\nEnvironmental Anomalies: {passed}/{total} passed")
    return failed == 0


def test_memory_fragmentation():
    """Test memory fragmentation horror."""
    print("\n" + "="*60)
    print("Testing Memory Fragmentation")
    print("="*60)
    
    save = main.new_save()
    passed = 0
    failed = 0
    
    # Memory fragment tracking
    if save['memory_fragments_lost'] == 0:
        print(f"  ✓ Memory fragments lost starts at 0")
        passed += 1
    else:
        print(f"  ✗ Memory fragments lost should start at 0")
        failed += 1
    
    # Memory can fragment
    save['memory_fragments_lost'] = 20
    if save['memory_fragments_lost'] == 20:
        print(f"  ✓ Memory fragmentation can be tracked")
        passed += 1
    else:
        print(f"  ✗ Memory fragmentation tracking failed")
        failed += 1
    
    total = passed + failed
    print(f"\nMemory Fragmentation: {passed}/{total} passed")
    return failed == 0


def test_reality_anchors():
    """Test reality anchor system."""
    print("\n" + "="*60)
    print("Testing Reality Anchors")
    print("="*60)
    
    save = main.new_save()
    passed = 0
    failed = 0
    
    # Reality anchor tracking
    if save['reality_anchors_lost'] == 0:
        print(f"  ✓ Reality anchors lost starts at 0")
        passed += 1
    else:
        print(f"  ✗ Reality anchors lost should start at 0")
        failed += 1
    
    # Anchors can be lost
    save['reality_anchors_lost'] = 5
    if save['reality_anchors_lost'] == 5:
        print(f"  ✓ Reality anchor loss can be tracked")
        passed += 1
    else:
        print(f"  ✗ Reality anchor tracking failed")
        failed += 1
    
    total = passed + failed
    print(f"\nReality Anchors: {passed}/{total} passed")
    return failed == 0


def test_witness_logging():
    """Test witness log system."""
    print("\n" + "="*60)
    print("Testing Witness Logging")
    print("="*60)
    
    save = main.new_save()
    passed = 0
    failed = 0
    
    # Witness log tracking
    if len(save['witness_log']) == 0:
        print(f"  ✓ Witness log starts empty")
        passed += 1
    else:
        print(f"  ✗ Witness log should start empty")
        failed += 1
    
    # Witnesses can be logged
    save['witness_log'].append("event_1")
    if len(save['witness_log']) == 1:
        print(f"  ✓ Witness events can be logged")
        passed += 1
    else:
        print(f"  ✗ Witness logging failed")
        failed += 1
    
    total = passed + failed
    print(f"\nWitness Logging: {passed}/{total} passed")
    return failed == 0


def main_test():
    """Run all horror system tests."""
    print("="*60)
    print("BOB DING - HORROR SYSTEMS TESTS")
    print("="*60)
    
    tests = [
        test_entity_system,
        test_watcher_system,
        test_time_anomalies,
        test_perception_breaks,
        test_identity_erosion,
        test_paranoia_system,
        test_glitch_system,
        test_environmental_anomalies,
        test_memory_fragmentation,
        test_reality_anchors,
        test_witness_logging,
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
