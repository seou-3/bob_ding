#!/usr/bin/env python3
"""
Bob Ding - Master Test Runner
Runs all test suites and provides comprehensive report
"""

import sys
import subprocess
import time


def run_test_file(filename, description):
    """Run a single test file and return result."""
    print(f"\n{'='*70}")
    print(f"Running: {description}")
    print(f"File: {filename}")
    print(f"{'='*70}")
    
    start_time = time.time()
    
    try:
        result = subprocess.run(
            [sys.executable, filename],
            capture_output=True,
            text=True,
            timeout=120
        )
        
        elapsed = time.time() - start_time
        
        # Print output
        print(result.stdout)
        if result.stderr:
            print("STDERR:", result.stderr)
        
        success = result.returncode == 0
        
        print(f"\n{description}: {'✓ PASSED' if success else '✗ FAILED'} ({elapsed:.2f}s)")
        
        return success, elapsed
        
    except subprocess.TimeoutExpired:
        elapsed = time.time() - start_time
        print(f"\n{description}: ✗ TIMEOUT ({elapsed:.2f}s)")
        return False, elapsed
    except Exception as e:
        elapsed = time.time() - start_time
        print(f"\n{description}: ✗ ERROR - {e} ({elapsed:.2f}s)")
        return False, elapsed


def main():
    """Run all test suites."""
    print("="*70)
    print("BOB DING - COMPREHENSIVE TEST SUITE")
    print("="*70)
    print(f"Python: {sys.version}")
    print(f"Started: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*70)
    
    # Define all test files
    test_suites = [
        ("test.py", "Core Smoke Tests"),
        ("test_features.py", "Feature Tests"),
        ("test_commands.py", "Command System Tests"),
        ("test_game_modes.py", "Game Mode Tests"),
        ("test_relationships.py", "Relationship System Tests"),
        ("test_horror_systems.py", "Horror Mechanics Tests"),
        ("test_endings.py", "Ending Tests"),
        ("test_secrets.py", "Secrets Catalog"),
    ]
    
    results = []
    total_time = 0
    
    for filename, description in test_suites:
        success, elapsed = run_test_file(filename, description)
        results.append((description, success, elapsed))
        total_time += elapsed
    
    # Final summary
    print("\n" + "="*70)
    print("FINAL SUMMARY")
    print("="*70)
    
    passed = sum(1 for _, success, _ in results if success)
    failed = len(results) - passed
    
    for description, success, elapsed in results:
        status = "✓ PASS" if success else "✗ FAIL"
        print(f"{status:8} {description:40} ({elapsed:6.2f}s)")
    
    print("="*70)
    print(f"Total: {passed}/{len(results)} test suites passed")
    print(f"Time:  {total_time:.2f}s")
    print(f"Ended: {time.strftime('%Y-%m-%d %H:%M:%S')}")
    print("="*70)
    
    if failed > 0:
        print(f"\n⚠️  {failed} test suite(s) failed!")
        return 1
    else:
        print(f"\n✅ All test suites passed!")
        return 0


if __name__ == "__main__":
    sys.exit(main())
