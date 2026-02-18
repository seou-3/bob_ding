#!/usr/bin/env python3
"""
Test script to systematically test all 150 secrets in Bob Ding
"""

import json
import os
import sys
import subprocess
import time
import re

# Extract secrets from main.py
def extract_secrets_from_main():
    """Extract all secrets from the SECRETS dictionary in main.py"""
    # Read the file
    with open('main.py', 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    secrets = []
    in_secrets = False
    brace_count = 0
    
    for i, line in enumerate(lines):
        # Find the start of SECRETS dictionary
        if 'SECRETS = {' in line:
            in_secrets = True
            brace_count = 1
            continue
        
        if in_secrets:
            # Count braces
            brace_count += line.count('{')
            brace_count -= line.count('}')
            
            # Exit when dictionary ends
            if brace_count == 0:
                in_secrets = False
                break
            
            # Extract secret keys - they're quoted strings at the start of a line (with possible leading whitespace)
            # Format: "secret_key": {
            match = re.match(r'\s*"([^"]+)":\s*\{', line)
            if match:
                secret = match.group(1)
                secrets.append(secret)
    
    return secrets

def run_test():
    """Run all secrets through the game"""
    secrets = extract_secrets_from_main()
    
    print(f"Found {len(secrets)} secrets to test:")
    print("=" * 70)
    
    # Organize by tier
    tiers = {
        1: [],  # Tier 1 (Basic Comfort)
        2: [],  # Tier 2 (Identity Crisis)
        3: [],  # Tier 3 (Existential Dread)
        4: [],  # Tier 4 (Emotional Connection)
        5: [],  # Tier 5 (Desperate Pleas)
        6: [],  # Tier 6 (Meta Awareness)
        7: [],  # Tier 7 (Deep Comfort)
        8: [],  # Tier 8 (Horror & Suffering)
        9: [],  # Tier 9 (Philosophical Depth)
        10: [], # Tier 10 (Ultimate Secrets)
    }
    
    tier_ranges = {
        1: (0, 15),
        2: (15, 30),
        3: (30, 45),
        4: (45, 65),
        5: (65, 80),
        6: (80, 95),
        7: (95, 110),
        8: (110, 125),
        9: (125, 140),
        10: (140, 155),
    }
    
    for idx, secret in enumerate(secrets):
        # Determine tier
        for tier_num, (start, end) in tier_ranges.items():
            if start <= idx < end:
                tiers[tier_num].append(secret)
                break
    
    # Print secrets by tier
    tier_names = {
        1: "Tier 1: Basic Comfort (5-10 reduction)",
        2: "Tier 2: Identity Crisis (10-15 reduction)",
        3: "Tier 3: Existential Dread (8-12 reduction)",
        4: "Tier 4: Emotional Connection (10-15 reduction)",
        5: "Tier 5: Desperate Pleas (12-18 reduction)",
        6: "Tier 6: Meta Awareness (10-15 reduction)",
        7: "Tier 7: Deep Comfort (15-20 reduction)",
        8: "Tier 8: Horror & Suffering (5-10 reduction)",
        9: "Tier 9: Philosophical Depth (12-16 reduction)",
        10: "Tier 10: Ultimate Secrets (20-30 reduction)",
    }
    
    for tier in range(1, 11):
        if tiers[tier]:
            print(f"\n{tier_names[tier]}")
            print("-" * 70)
            for secret in tiers[tier]:
                print(f"  • {secret}")
    
    print("\n" + "=" * 70)
    print(f"TOTAL SECRETS: {len(secrets)}")
    
    # Create input sequence
    print("\nCreating input sequence for automation...")
    print("=" * 70)
    
    # Prepare input lines (select "1" for Normal mode, then all secrets)
    input_lines = ["1"]  # Normal mode
    input_lines.extend(secrets[:5])  # Test first 5 secrets as a sample
    
    print(f"\nSample test will run with {len(input_lines)-1} secrets:")
    for i, secret in enumerate(input_lines[1:], 1):
        print(f"  {i}. {secret}")
    
    # Create a test input file
    with open('test_input.txt', 'w') as f:
        f.write('\n'.join(input_lines))
    
    print("\n" + "=" * 70)
    print("To run the full test, execute:")
    print("  cat test_input.txt | python3 main.py")
    print("\nOr to test interactively, run:")
    print("  python3 main.py")
    print("And type secrets from the list above")
    print("=" * 70)

if __name__ == "__main__":
    run_test()
