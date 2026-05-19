# Reading a massive log file and extracting error messages
# Without generator comprehension, load entire file into memory is bad approch

# Simulating a large log file 
log_lines = [
    "INFO: User logged in",
    "ERROR: Database connection failed",
    "INFO: File uploaded", 
    "ERROR: Timeout occurred",
    "WARNING: Low disk space",
    "ERROR: Authentication failed"
]

# GENERATOR COMPREHENSION - Notice () instead of []
# This creates a GENERATOR, NOT a list. It yields values one at a time on demand.
error_messages = (line for line in log_lines if "ERROR" in line)

# WHY USE GENERATOR? 
# Memory efficiency: Doesn't store all results at once, yields one item at a time
# Performance: Lazy evaluation - only computes when you ask for next item
# Great for: Large files, API streams, infinite sequences, data pipelines

# HOW IT WORKS:
# 1. No list is created in memory
# 2. Each iteration asks the generator for the next value
# 3. Values are produced on-the-fly and forgotten after use

print("Generator object:", error_messages)  # <generator object at 0x...>

# USING THE GENERATOR (only consumes memory for one item at a time)
for error in error_messages:
    print("Found:", error)
    # After processing, this error is discarded from memory

# Output:
# Found: ERROR: Database connection failed
# Found: ERROR: Timeout occurred
# Found: ERROR: Authentication failed

import sys

# List comprehension ([] brackets) - creates everything at once
list_errors = [line for line in log_lines if "ERROR" in line]
print(f"List memory: {sys.getsizeof(list_errors)} bytes")  # Larger memory

# Generator comprehension (() parentheses) - creates nothing upfront
gen_errors = (line for line in log_lines if "ERROR" in line)
print(f"Generator memory: {sys.getsizeof(gen_errors)} bytes")  # Tiny memory

# Generators can only be used ONCE
# After iterating through all values, it's exhausted
second_pass = list(gen_errors)  # Empty list! Generator is already used up

# Processing large files:
def process_large_file():
    """
    #  (BAD for 10GB file):
    with open('huge_file.txt') as f:
        all_lines = f.readlines()  # LOADS EVERYTHING INTO MEMORY - CRASH!
        errors = [line for line in all_lines if 'ERROR' in line]
    
    # Real approch:
    with open('huge_file.txt') as f:
        errors = (line for line in f if 'ERROR' in line)  # Processes line by line
        for error in errors:
            write_to_database(error)  # Each error processed and discarded
    """
    pass

# SYNTAX RULES:
# () - Parentheses for generator comprehension
# [] - Square brackets for list comprehension
# {} - Curly braces for set/dict comprehension

# WHEN TO USE GENERATOR COMPREHENSION:
# ✓ Huge datasets (millions of items)
# ✓ Streaming data from APIs
# ✓ Reading massive files
# ✓ When you only need to iterate once
# ✗ When you need random access or multiple passes
# ✗ For small datasets where list is fine

print("\n--- Practical Pipeline Example ---")
numbers = range(1000000)  # 1 million numbers

# Pipeline: Even numbers -> Square -> Only keep those > 100
pipeline = (
    num**2 
    for num in numbers 
    if num % 2 == 0
)
pipeline_filtered = (
    squared for squared in pipeline 
    if squared > 100
)

# Only 10 items computed (lazy evaluation)
import itertools
first_10 = list(itertools.islice(pipeline_filtered, 10))
print(f"First 10 results: {first_10}")
#  Only computing values as needed