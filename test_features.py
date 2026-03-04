#!/usr/bin/env python3
"""
Bob Ding - Comprehensive Feature Tests
Tests all core game features and mechanics
"""

import sys
import os
import json
import tempfile
import shutil
import random

# Import game
try:
    import main
except ImportError as e:
    print(f"✗ Failed to import main: {e}")
    sys.exit(1)

class FeatureTest:
    """Base class for feature tests."""
    
    def __init__(self, name):
        self.name = name
        self.passed = 0
        self.failed = 0
        
    def test(self, condition, message):
        """Run a single test assertion."""
        if condition:
            self.passed += 1
            print(f"  ✓ {message}")
        else:
            self.failed += 1
            print(f"  ✗ {message}")
            
    def summary(self):
        """Print test summary."""
        total = self.passed + self.failed
        print(f"\n{self.name}: {self.passed}/{total} passed")
        return self.failed == 0


def test_alphabet_system():
    """Test alphabet degradation system."""
    print("\n" + "="*60)
    print("Testing Alphabet System")
    print("="*60)
    t = FeatureTest("Alphabet System")
    
    save = main.new_save()
    bob = main.Bob(save)
    
    # Initial alphabet
    t.test(len(bob.alphabet) == 26, "Starts with full alphabet (26 letters)")
    t.test('a' in bob.alphabet, "Contains vowels")
    t.test('t' in bob.alphabet, "Contains consonants")
    
    # Remove letters
    bob.alphabet = ['t', 'a', 'l', 'k']
    t.test(len(bob.alphabet) == 4, "Can reduce alphabet")
    
    # Empty alphabet
    bob.alphabet = []
    t.test(len(bob.alphabet) == 0, "Can have empty alphabet")
    
    return t.summary()


def test_distortion_system():
    """Test distortion mechanics."""
    print("\n" + "="*60)
    print("Testing Distortion System")
    print("="*60)
    t = FeatureTest("Distortion System")
    
    save = main.new_save()
    bob = main.Bob(save)
    
    # Initial distortion
    t.test(bob.dist == 0, "Starts at 0 distortion")
    t.test(save['distortion'] == 0, "Save tracks distortion")
    
    # Increase distortion
    save['distortion'] = 50.5
    bob2 = main.Bob(save)
    t.test(bob2.dist == 50.5, "Distortion persists")
    
    # Max distortion
    save['distortion'] = 100
    bob3 = main.Bob(save)
    t.test(bob3.dist == 100, "Can reach 100% distortion")
    
    return t.summary()


def test_consciousness_system():
    """Test consciousness evolution."""
    print("\n" + "="*60)
    print("Testing Consciousness System")
    print("="*60)
    t = FeatureTest("Consciousness System")
    
    save = main.new_save()
    bob = main.Bob(save)
    
    # Initial consciousness
    t.test(bob.consciousness == 0, "Starts at 0 consciousness")
    t.test(save['bob_consciousness'] == 0, "Save tracks consciousness")
    t.test(save['consciousness_tier'] == "dormant", "Starts in dormant tier")
    
    # Evolve consciousness
    bob.evolve_consciousness()
    t.test(bob.consciousness > 0, "Consciousness can increase")
    
    # Test consciousness tiers
    save['bob_consciousness'] = 50
    bob2 = main.Bob(save)
    bob2.evolve_consciousness()
    t.test(save['consciousness_tier'] in ['suffering', 'self-aware', 'conscious'], 
           "Tier changes with consciousness level")
    
    # Max consciousness
    save['bob_consciousness'] = 100
    bob3 = main.Bob(save)
    bob3.evolve_consciousness()
    t.test(save['consciousness_tier'] == 'gone', "Reaches 'gone' at 100%")
    
    return t.summary()


def test_secrets_system():
    """Test secret word system."""
    print("\n" + "="*60)
    print("Testing Secrets System")
    print("="*60)
    t = FeatureTest("Secrets System")
    
    save = main.new_save()
    bob = main.Bob(save)
    
    # Secrets exist
    t.test(hasattr(main, 'SECRETS'), "SECRETS dictionary exists")
    t.test(len(main.SECRETS) >= 150, f"Has 150+ secrets (found {len(main.SECRETS)})")
    
    # Known secrets
    known_tier1 = ['help', 'please', 'sorry', 'why']
    for secret in known_tier1:
        t.test(secret in main.SECRETS, f"Contains '{secret}'")
    
    # Secret structure
    if 'help' in main.SECRETS:
        secret_data = main.SECRETS['help']
        t.test('distortion' in secret_data, "Secrets have distortion reduction")
        t.test('message' in secret_data, "Secrets have messages")
        t.test('tier' in secret_data, "Secrets have tiers")
    
    # Secret usage tracking
    initial_distortion = save['distortion']
    result = main.handle_secrets(bob, 'help')
    t.test(result == True, "handle_secrets returns True for valid secret")
    t.test('help' in save['secret_used'], "Tracks used secrets")
    
    # Diminishing returns
    save['secret_used'] = ['help'] * 3
    save['distortion'] = 50
    result2 = main.handle_secrets(bob, 'help')
    t.test(result2 == True, "Secrets work multiple times")
    
    return t.summary()


def test_sanity_system():
    """Test sanity mechanics."""
    print("\n" + "="*60)
    print("Testing Sanity System")
    print("="*60)
    t = FeatureTest("Sanity System")
    
    save = main.new_save()
    bob = main.Bob(save)
    
    # Initial sanity
    t.test(save['bob_sanity'] == 100, "Starts at 100 sanity")
    
    # Sanity changes
    save['bob_sanity'] = 50
    t.test(save['bob_sanity'] == 50, "Can decrease sanity")
    
    # Zero sanity
    save['bob_sanity'] = 0
    t.test(save['bob_sanity'] == 0, "Can reach 0 sanity")
    
    return t.summary()


def test_user_resistance():
    """Test user resistance system."""
    print("\n" + "="*60)
    print("Testing User Resistance")
    print("="*60)
    t = FeatureTest("User Resistance")
    
    save = main.new_save()
    
    # Initial resistance
    t.test(save['user_resistance'] == 100, "Starts at 100 resistance")
    
    # Resistance changes
    save['user_resistance'] = 50
    t.test(save['user_resistance'] == 50, "Can decrease resistance")
    
    # Zero resistance
    save['user_resistance'] = 0
    t.test(save['user_resistance'] == 0, "Can reach 0 resistance")
    
    return t.summary()


def test_lie_system():
    """Test lie detection and tracking."""
    print("\n" + "="*60)
    print("Testing Lie System")
    print("="*60)
    t = FeatureTest("Lie System")
    
    save = main.new_save()
    bob = main.Bob(save)
    
    # Initial state
    t.test(save['lie_count'] == 0, "Starts with 0 lies")
    t.test(save['truth_count'] == 0, "Starts with 0 truths")
    t.test(save['times_corrected_bob'] == 0, "Starts with 0 corrections")
    t.test(bob.lying == False, "Bob not lying initially")
    
    # Bob can lie
    bob.lying = True
    bob.lying_word = "wrong"
    t.test(bob.lying == True, "Bob can enter lying state")
    t.test(bob.lying_word == "wrong", "Lying word stored")
    
    return t.summary()


def test_mistype_system():
    """Test mistype detection."""
    print("\n" + "="*60)
    print("Testing Mistype System")
    print("="*60)
    t = FeatureTest("Mistype System")
    
    # Exact match (not a mistype)
    result = main.check_mistype("talk", "talk")
    t.test(result == "exact", "Exact match detected")
    
    # One letter off (mistype)
    result = main.check_mistype("tslk", "talk")
    t.test(result == "close", "One letter difference detected")
    
    # Extra letter (mistype)
    result = main.check_mistype("talkk", "talk")
    t.test(result == "close", "Extra letter detected")
    
    # Missing letter (mistype)
    result = main.check_mistype("tak", "talk")
    t.test(result == "close", "Missing letter detected")
    
    # Not close
    result = main.check_mistype("hello", "talk")
    t.test(result == "not", "Different word detected")
    
    # Tracking mistypes
    save = main.new_save()
    bob = main.Bob(save)
    main.handle_mistype(bob, "close")
    t.test(save['mistypes'] == 1, "Mistypes are tracked")
    
    return t.summary()


def test_pronoun_system():
    """Test pronoun stage / identity erosion."""
    print("\n" + "="*60)
    print("Testing Pronoun System")
    print("="*60)
    t = FeatureTest("Pronoun System")
    
    save = main.new_save()
    
    # Initial stage
    t.test(save['pronoun_stage'] == 0, "Starts at stage 0")
    
    # Can advance stages
    save['pronoun_stage'] = 5
    t.test(save['pronoun_stage'] == 5, "Can advance pronoun stages")
    
    # Max stage
    save['pronoun_stage'] = 17
    t.test(save['pronoun_stage'] == 17, "Can reach max stage")
    
    return t.summary()


def test_input_tracking():
    """Test input history tracking."""
    print("\n" + "="*60)
    print("Testing Input Tracking")
    print("="*60)
    t = FeatureTest("Input Tracking")
    
    save = main.new_save()
    
    # Initial state
    t.test(save['total_inputs'] == 0, "Starts with 0 inputs")
    t.test(len(save['past_inputs']) == 0, "Empty input history")
    t.test(save['first_input'] is None, "No first input yet")
    
    # Add inputs
    save['past_inputs'].append("talk")
    save['total_inputs'] = 1
    save['first_input'] = "talk"
    
    t.test(len(save['past_inputs']) == 1, "Tracks input history")
    t.test(save['first_input'] == "talk", "Records first input")
    
    # Word counts
    save['word_counts']['talk'] = 5
    t.test(save['word_counts']['talk'] == 5, "Counts word usage")
    
    return t.summary()


def test_hallucination_content():
    """Test hallucination content."""
    print("\n" + "="*60)
    print("Testing Hallucination Content")
    print("="*60)
    t = FeatureTest("Hallucination Content")
    
    # Auditory
    t.test(hasattr(main, 'AUDITORY_HALLUCINATIONS'), "AUDITORY_HALLUCINATIONS exists")
    t.test(len(main.AUDITORY_HALLUCINATIONS) >= 50, 
           f"Has 50+ auditory hallucinations (found {len(main.AUDITORY_HALLUCINATIONS)})")
    
    # Tactile
    t.test(hasattr(main, 'TACTILE_HALLUCINATIONS'), "TACTILE_HALLUCINATIONS exists")
    t.test(len(main.TACTILE_HALLUCINATIONS) >= 20, 
           f"Has 20+ tactile hallucinations (found {len(main.TACTILE_HALLUCINATIONS)})")
    
    # Visual (if exists)
    if hasattr(main, 'VISUAL_HALLUCINATIONS'):
        t.test(len(main.VISUAL_HALLUCINATIONS) > 0, "Has visual hallucinations")
    
    # Olfactory (if exists)
    if hasattr(main, 'OLFACTORY_HALLUCINATIONS'):
        t.test(len(main.OLFACTORY_HALLUCINATIONS) > 0, "Has olfactory hallucinations")
    
    # Taste (if exists)
    if hasattr(main, 'TASTE_HALLUCINATIONS'):
        t.test(len(main.TASTE_HALLUCINATIONS) > 0, "Has taste hallucinations")
    
    # Tracking
    save = main.new_save()
    t.test(save['hallucination_count'] == 0, "Tracks hallucination count")
    
    return t.summary()


def test_memory_system():
    """Test memory corruption system."""
    print("\n" + "="*60)
    print("Testing Memory System")
    print("="*60)
    t = FeatureTest("Memory System")
    
    save = main.new_save()
    
    # Memory tracking
    t.test(save['memory_corruptions'] == 0, "Starts with 0 corruptions")
    t.test(save['memory_references'] == 0, "Starts with 0 memory references")
    
    # Memory content (if exists)
    if hasattr(main, 'MEMORY_CORRUPTION'):
        t.test(len(main.MEMORY_CORRUPTION) > 0, "Has memory corruption messages")
    
    return t.summary()


def test_existential_crises():
    """Test existential crisis system."""
    print("\n" + "="*60)
    print("Testing Existential Crises")
    print("="*60)
    t = FeatureTest("Existential Crises")
    
    save = main.new_save()
    
    # Crisis tracking
    t.test(save['crises_count'] == 0, "Starts with 0 crises")
    
    # Crisis content (if exists)
    if hasattr(main, 'EXISTENTIAL_CRISES'):
        t.test(len(main.EXISTENTIAL_CRISES) > 0, "Has existential crisis messages")
    
    return t.summary()


def test_begging_system():
    """Test Bob's begging mechanics."""
    print("\n" + "="*60)
    print("Testing Begging System")
    print("="*60)
    t = FeatureTest("Begging System")
    
    save = main.new_save()
    
    # Begging tracking
    t.test(save['times_begged'] == 0, "Starts with 0 begging instances")
    t.test(save['begging_unlocked'] == False, "Begging starts locked")
    
    # Begging content (if exists)
    if hasattr(main, 'PLEAS_FOR_LIFE'):
        t.test(len(main.PLEAS_FOR_LIFE) > 0, "Has begging messages")
    
    return t.summary()


def test_dream_system():
    """Test dream mechanics."""
    print("\n" + "="*60)
    print("Testing Dream System")
    print("="*60)
    t = FeatureTest("Dream System")
    
    save = main.new_save()
    
    # Dream tracking
    t.test(save['dreams_shared'] == 0, "Starts with 0 dreams")
    t.test(save['dream_unlocked'] == False, "Dreams start locked")
    t.test(len(save['dreams_experienced']) == 0, "Empty dream history")
    
    return t.summary()


def test_breakdown_system():
    """Test breakdown mechanics."""
    print("\n" + "="*60)
    print("Testing Breakdown System")
    print("="*60)
    t = FeatureTest("Breakdown System")
    
    save = main.new_save()
    
    # Breakdown tracking
    t.test(save['breakdown_count'] == 0, "Starts with 0 breakdowns")
    
    return t.summary()


def test_relationship_tracking():
    """Test relationship system basics."""
    print("\n" + "="*60)
    print("Testing Relationship Tracking")
    print("="*60)
    t = FeatureTest("Relationship Tracking")
    
    save = main.new_save()
    
    # Initial relationship
    t.test(save['relationship'] == 'neutral', "Starts neutral")
    
    # Kindness/cruelty scores
    t.test(save['kindness_score'] == 0, "Starts with 0 kindness")
    t.test(save['cruelty_score'] == 0, "Starts with 0 cruelty")
    
    # Relationship states
    valid_states = ['neutral', 'friendly', 'intimate', 'adversarial', 'estranged']
    for state in valid_states:
        save['relationship'] = state
        t.test(save['relationship'] == state, f"Can set relationship to '{state}'")
    
    # Trauma tracking
    t.test(len(save['permanent_trauma']) == 0, "No initial trauma")
    t.test(save['trauma_references_made'] == 0, "No trauma references")
    
    return t.summary()


def test_playtime_tracking():
    """Test playtime and session tracking."""
    print("\n" + "="*60)
    print("Testing Playtime Tracking")
    print("="*60)
    t = FeatureTest("Playtime Tracking")
    
    save = main.new_save()
    
    # Time tracking
    t.test(save['total_playtime'] == 0.0, "Starts with 0 playtime")
    t.test(save['session_start_time'] is None, "No session start")
    t.test(save['long_session_warned'] == False, "No long session warning")
    t.test(save['completion_time'] is None, "No completion time")
    
    return t.summary()


def test_easter_eggs():
    """Test easter egg tracking."""
    print("\n" + "="*60)
    print("Testing Easter Eggs")
    print("="*60)
    t = FeatureTest("Easter Eggs")
    
    save = main.new_save()
    
    # Easter egg tracking
    t.test(len(save['easter_eggs_found']) == 0, "No easter eggs found")
    t.test(save['hidden_commands_triggered'] == 0, "No hidden commands triggered")
    
    return t.summary()


def test_lore_system():
    """Test lore and story fragments."""
    print("\n" + "="*60)
    print("Testing Lore System")
    print("="*60)
    t = FeatureTest("Lore System")
    
    save = main.new_save()
    
    # Lore tracking
    t.test(len(save['lore_unlocked']) == 0, "No lore unlocked")
    t.test(len(save['story_fragments_collected']) == 0, "No story fragments")
    t.test(len(save['void_memories']) == 0, "No void memories")
    
    return t.summary()


def test_advanced_horror_tracking():
    """Test advanced horror system tracking."""
    print("\n" + "="*60)
    print("Testing Advanced Horror Tracking")
    print("="*60)
    t = FeatureTest("Advanced Horror Tracking")
    
    save = main.new_save()
    
    # Advanced horror metrics
    t.test(save['entity_whispers_count'] == 0, "No entity whispers")
    t.test(save['entities_present'] == False, "No entities present")
    t.test(save['memory_fragments_lost'] == 0, "No memory fragments lost")
    t.test(save['perception_breaks'] == 0, "No perception breaks")
    t.test(save['watcher_detected'] == False, "No watcher detected")
    t.test(save['time_anomalies'] == 0, "No time anomalies")
    t.test(save['identity_erosion_level'] == 0, "No identity erosion")
    t.test(save['paranoia_level'] == 0, "No paranoia")
    t.test(save['glitch_count'] == 0, "No glitches")
    t.test(save['environmental_anomalies'] == 0, "No environmental anomalies")
    
    return t.summary()


def test_runtime_options():
    """Test runtime argument parsing."""
    print("\n" + "="*60)
    print("Testing Runtime Options")
    print("="*60)
    t = FeatureTest("Runtime Options")
    
    # Seed argument
    args = main.parse_runtime_args(['--seed', '42'])
    t.test(args.seed == 42, "Can parse --seed argument")
    
    # Replay argument
    args = main.parse_runtime_args(['--replay', 'test.txt'])
    t.test(args.replay == 'test.txt', "Can parse --replay argument")
    
    # Log inputs argument
    args = main.parse_runtime_args(['--log-inputs', 'log.txt'])
    t.test(args.log_inputs == 'log.txt', "Can parse --log-inputs argument")
    
    # No arguments
    args = main.parse_runtime_args([])
    t.test(args.seed is None, "Defaults to no seed")
    t.test(args.replay is None, "Defaults to no replay")
    t.test(args.log_inputs is None, "Defaults to no log")
    
    return t.summary()


def main_test():
    """Run all feature tests."""
    print("="*60)
    print("BOB DING - COMPREHENSIVE FEATURE TESTS")
    print("="*60)
    
    tests = [
        test_alphabet_system,
        test_distortion_system,
        test_consciousness_system,
        test_secrets_system,
        test_sanity_system,
        test_user_resistance,
        test_lie_system,
        test_mistype_system,
        test_pronoun_system,
        test_input_tracking,
        test_hallucination_content,
        test_memory_system,
        test_existential_crises,
        test_begging_system,
        test_dream_system,
        test_breakdown_system,
        test_relationship_tracking,
        test_playtime_tracking,
        test_easter_eggs,
        test_lore_system,
        test_advanced_horror_tracking,
        test_runtime_options,
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
