"""
INTERVIEW PATTERNS - BUILT-IN FUNCTIONS
========================================

This file contains common interview patterns that use Python's built-in functions.
Master these patterns to write elegant, Pythonic solutions!

Each pattern includes:
- Problem description
- Brute force approach
- Optimized approach using built-ins
- Time/Space complexity
- When to use

Author: DSA Learning
"""

print("=" * 80)
print("INTERVIEW PATTERNS USING BUILT-IN FUNCTIONS")
print("=" * 80)

# ============================================================================
# PATTERN 1: FIND INDEX OF MAX/MIN ELEMENT
# ============================================================================

print("\n" + "=" * 80)
print("PATTERN 1: FIND INDEX OF MAX/MIN ELEMENT")
print("=" * 80)

def find_max_index_brute(arr):
    """Brute force - O(n) with manual tracking"""
    max_val = arr[0]
    max_idx = 0
    for i in range(1, len(arr)):
        if arr[i] > max_val:
            max_val = arr[i]
            max_idx = i
    return max_idx

def find_max_index_pythonic(arr):
    """Pythonic - using enumerate + max"""
    return max(enumerate(arr), key=lambda x: x[1])[0]

# Test
arr = [3, 1, 4, 1, 5, 9, 2, 6]
print(f"Array: {arr}")
print(f"Brute force: index of max = {find_max_index_brute(arr)}")
print(f"Pythonic: index of max = {find_max_index_pythonic(arr)}")

# Find index of min
min_idx = min(enumerate(arr), key=lambda x: x[1])[0]
print(f"Index of min: {min_idx}")


# ============================================================================
# PATTERN 2: PARALLEL ARRAY OPERATIONS
# ============================================================================

print("\n" + "=" * 80)
print("PATTERN 2: PARALLEL ARRAY OPERATIONS")
print("=" * 80)

def add_arrays_brute(arr1, arr2):
    """Brute force - manual indexing"""
    result = []
    for i in range(len(arr1)):
        result.append(arr1[i] + arr2[i])
    return result

def add_arrays_pythonic(arr1, arr2):
    """Pythonic - using zip"""
    return [a + b for a, b in zip(arr1, arr2)]

# Test
list1 = [1, 2, 3, 4]
list2 = [10, 20, 30, 40]
print(f"List 1: {list1}")
print(f"List 2: {list2}")
print(f"Brute force sum: {add_arrays_brute(list1, list2)}")
print(f"Pythonic sum: {add_arrays_pythonic(list1, list2)}")

# Other operations
print(f"Multiply: {[a * b for a, b in zip(list1, list2)]}")
print(f"Max of pairs: {[max(a, b) for a, b in zip(list1, list2)]}")


# ============================================================================
# PATTERN 3: CUSTOM SORTING
# ============================================================================

print("\n" + "=" * 80)
print("PATTERN 3: CUSTOM SORTING")
print("=" * 80)

# Sort by absolute value
nums = [-5, -1, 3, -2, 4]
sorted_abs = sorted(nums, key=abs)
print(f"Original: {nums}")
print(f"Sorted by abs: {sorted_abs}")

# Sort strings by length
words = ["python", "a", "code", "is", "fun"]
sorted_len = sorted(words, key=len)
print(f"\nWords: {words}")
print(f"Sorted by length: {sorted_len}")

# Sort by multiple criteria
students = [
    ("Alice", 20, 95),
    ("Bob", 25, 87),
    ("Alice", 22, 90),
    ("Charlie", 20, 95)
]
# Sort by name ASC, then age ASC, then score DESC
sorted_students = sorted(students, key=lambda x: (x[0], x[1], -x[2]))
print(f"\nStudents sorted (name ASC, age ASC, score DESC):")
for s in sorted_students:
    print(f"  {s}")

# Sort dictionary by value
scores = {'Alice': 95, 'Bob': 87, 'Charlie': 92}
sorted_by_score = sorted(scores.items(), key=lambda x: x[1], reverse=True)
print(f"\nScores sorted: {sorted_by_score}")


# ============================================================================
# PATTERN 4: FILTER + TRANSFORM (MAP + FILTER)
# ============================================================================

print("\n" + "=" * 80)
print("PATTERN 4: FILTER + TRANSFORM")
print("=" * 80)

# Get squares of even numbers
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
squares_of_evens = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))
print(f"Numbers: {nums}")
print(f"Squares of evens: {squares_of_evens}")

# Alternative with list comprehension (often more readable)
squares_of_evens_lc = [x**2 for x in nums if x % 2 == 0]
print(f"Using list comp: {squares_of_evens_lc}")

# Uppercase only alphas
text = "Hello123World456"
alphas_upper = list(map(str.upper, filter(str.isalpha, text)))
print(f"\nText: {text}")
print(f"Alpha chars uppercased: {''.join(alphas_upper)}")


# ============================================================================
# PATTERN 5: BOOLEAN CHECKS (ANY/ALL)
# ============================================================================

print("\n" + "=" * 80)
print("PATTERN 5: BOOLEAN CHECKS (ANY/ALL)")
print("=" * 80)

# Check if all elements satisfy condition
nums = [2, 4, 6, 8, 10]
all_even = all(x % 2 == 0 for x in nums)
print(f"All even in {nums}? {all_even}")

# Check if any element satisfies condition
nums = [1, 3, 5, 6, 7]
any_even = any(x % 2 == 0 for x in nums)
print(f"Any even in {nums}? {any_even}")

# Check if all strings are uppercase
words = ["HELLO", "WORLD", "PYTHON"]
all_upper = all(word.isupper() for word in words)
print(f"All uppercase in {words}? {all_upper}")

# Check if any string starts with 'P'
any_starts_p = any(word.startswith('P') for word in words)
print(f"Any starts with 'P'? {any_starts_p}")

# Validate password (all conditions must be True)
password = "Pass123!"
is_valid = all([
    len(password) >= 8,
    any(c.isupper() for c in password),
    any(c.islower() for c in password),
    any(c.isdigit() for c in password)
])
print(f"\nPassword '{password}' valid? {is_valid}")


# ============================================================================
# PATTERN 6: CREATE DICTIONARY FROM LISTS
# ============================================================================

print("\n" + "=" * 80)
print("PATTERN 6: CREATE DICTIONARY FROM LISTS")
print("=" * 80)

# Method 1: zip
keys = ['name', 'age', 'city', 'country']
values = ['Alice', 25, 'NYC', 'USA']
person = dict(zip(keys, values))
print(f"Using zip: {person}")

# Method 2: enumerate (index as key)
fruits = ['apple', 'banana', 'cherry']
fruit_dict = dict(enumerate(fruits))
print(f"Using enumerate: {fruit_dict}")

# Method 3: Custom key-value from single list
numbers = [1, 2, 3, 4, 5]
squares_dict = {x: x**2 for x in numbers}
print(f"Squares dict: {squares_dict}")


# ============================================================================
# PATTERN 7: UNZIP PAIRS
# ============================================================================

print("\n" + "=" * 80)
print("PATTERN 7: UNZIP PAIRS")
print("=" * 80)

# Unzip list of tuples
pairs = [(1, 'a'), (2, 'b'), (3, 'c'), (4, 'd')]
numbers, letters = zip(*pairs)
print(f"Pairs: {pairs}")
print(f"Numbers: {list(numbers)}")
print(f"Letters: {list(letters)}")

# Separate coordinates
points = [(1, 2), (3, 4), (5, 6)]
x_coords, y_coords = zip(*points)
print(f"\nPoints: {points}")
print(f"X coords: {list(x_coords)}")
print(f"Y coords: {list(y_coords)}")


# ============================================================================
# PATTERN 8: CHECK IF ALL ELEMENTS ARE UNIQUE
# ============================================================================

print("\n" + "=" * 80)
print("PATTERN 8: CHECK IF ALL ELEMENTS ARE UNIQUE")
print("=" * 80)

def all_unique(items):
    """Check if all elements are unique using set"""
    return len(items) == len(set(items))

# Test
arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 2, 3, 2, 5]
print(f"{arr1} all unique? {all_unique(arr1)}")
print(f"{arr2} all unique? {all_unique(arr2)}")


# ============================================================================
# PATTERN 9: FIND DUPLICATES
# ============================================================================

print("\n" + "=" * 80)
print("PATTERN 9: FIND DUPLICATES")
print("=" * 80)

def find_duplicates(arr):
    """Find all duplicate elements"""
    seen = set()
    duplicates = set()
    for item in arr:
        if item in seen:
            duplicates.add(item)
        else:
            seen.add(item)
    return list(duplicates)

# Alternative using filter + set
def find_duplicates_v2(arr):
    seen = set()
    return [x for x in arr if x in seen or seen.add(x) is None][1::2]

arr = [1, 2, 3, 2, 4, 3, 5, 6, 3]
print(f"Array: {arr}")
print(f"Duplicates: {find_duplicates(arr)}")


# ============================================================================
# PATTERN 10: FLATTEN NESTED LIST
# ============================================================================

print("\n" + "=" * 80)
print("PATTERN 10: FLATTEN NESTED LIST")
print("=" * 80)

# Method 1: List comprehension
nested = [[1, 2], [3, 4], [5, 6]]
flattened = [item for sublist in nested for item in sublist]
print(f"Nested: {nested}")
print(f"Flattened: {flattened}")

# Method 2: Using sum with empty list as start
flattened2 = sum(nested, [])
print(f"Using sum: {flattened2}")

# Method 3: Using reduce
from functools import reduce
flattened3 = reduce(lambda x, y: x + y, nested)
print(f"Using reduce: {flattened3}")


# ============================================================================
# PATTERN 11: GROUP ELEMENTS BY CRITERIA
# ============================================================================

print("\n" + "=" * 80)
print("PATTERN 11: GROUP ELEMENTS BY CRITERIA")
print("=" * 80)

# Group numbers by even/odd
nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
evens = list(filter(lambda x: x % 2 == 0, nums))
odds = list(filter(lambda x: x % 2 != 0, nums))
print(f"Numbers: {nums}")
print(f"Evens: {evens}")
print(f"Odds: {odds}")

# Group words by first letter
words = ['apple', 'apricot', 'banana', 'blueberry', 'cherry']
from collections import defaultdict
grouped = defaultdict(list)
for word in words:
    grouped[word[0]].append(word)
print(f"\nWords grouped by first letter: {dict(grouped)}")


# ============================================================================
# PATTERN 12: TOP K ELEMENTS
# ============================================================================

print("\n" + "=" * 80)
print("PATTERN 12: TOP K ELEMENTS")
print("=" * 80)

# Find top 3 largest numbers
nums = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
top_3 = sorted(nums, reverse=True)[:3]
print(f"Numbers: {nums}")
print(f"Top 3: {top_3}")

# Alternative using sorted with key
students = [
    ('Alice', 95),
    ('Bob', 87),
    ('Charlie', 92),
    ('David', 88),
    ('Eve', 96)
]
top_2_students = sorted(students, key=lambda x: x[1], reverse=True)[:2]
print(f"\nTop 2 students: {top_2_students}")


# ============================================================================
# PATTERN 13: REMOVE NONE/EMPTY VALUES
# ============================================================================

print("\n" + "=" * 80)
print("PATTERN 13: REMOVE NONE/EMPTY VALUES")
print("=" * 80)

# Filter out falsy values
mixed = [0, 1, None, 2, False, 3, '', 'hello', [], [1, 2]]
filtered = list(filter(None, mixed))
print(f"Mixed: {mixed}")
print(f"Filtered: {filtered}")

# Keep only non-empty strings
strings = ['', 'hello', '', 'world', '', 'python']
non_empty = list(filter(bool, strings))
print(f"\nStrings: {strings}")
print(f"Non-empty: {non_empty}")


# ============================================================================
# PATTERN 14: ENUMERATE WITH CUSTOM START
# ============================================================================

print("\n" + "=" * 80)
print("PATTERN 14: ENUMERATE WITH CUSTOM START")
print("=" * 80)

# Print numbered list starting from 1
items = ['First item', 'Second item', 'Third item']
print("Numbered list:")
for num, item in enumerate(items, start=1):
    print(f"{num}. {item}")

# Create rank dictionary
scores = [95, 87, 92, 88]
ranks = dict(enumerate(sorted(scores, reverse=True), start=1))
print(f"\nRanks: {ranks}")


# ============================================================================
# PATTERN 15: MATRIX TRANSPOSE
# ============================================================================

print("\n" + "=" * 80)
print("PATTERN 15: MATRIX TRANSPOSE")
print("=" * 80)

# Transpose matrix using zip
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
transposed = [list(row) for row in zip(*matrix)]
print(f"Original matrix:")
for row in matrix:
    print(f"  {row}")
print(f"Transposed:")
for row in transposed:
    print(f"  {row}")


# ============================================================================
# PATTERN 16: PAIRWISE ITERATION
# ============================================================================

print("\n" + "=" * 80)
print("PATTERN 16: PAIRWISE ITERATION")
print("=" * 80)

# Iterate over consecutive pairs
nums = [1, 2, 3, 4, 5]
pairs = list(zip(nums, nums[1:]))
print(f"Numbers: {nums}")
print(f"Consecutive pairs: {pairs}")

# Calculate differences
differences = [b - a for a, b in zip(nums, nums[1:])]
print(f"Differences: {differences}")


# ============================================================================
# PATTERN 17: MERGE DICTIONARIES
# ============================================================================

print("\n" + "=" * 80)
print("PATTERN 17: MERGE DICTIONARIES")
print("=" * 80)

dict1 = {'a': 1, 'b': 2}
dict2 = {'c': 3, 'd': 4}
dict3 = {'e': 5}

# Method 1: Using ** unpacking
merged = {**dict1, **dict2, **dict3}
print(f"Merged: {merged}")

# Method 2: Using dict() with zip for overlapping keys
keys = list(dict1.keys()) + list(dict2.keys())
values = list(dict1.values()) + list(dict2.values())
merged2 = dict(zip(keys, values))
print(f"Merged (zip): {merged2}")


# ============================================================================
# PATTERN 18: FREQUENCY COUNT
# ============================================================================

print("\n" + "=" * 80)
print("PATTERN 18: FREQUENCY COUNT")
print("=" * 80)

# Count character frequency
text = "hello world"
freq = {}
for char in text:
    freq[char] = freq.get(char, 0) + 1
print(f"Text: '{text}'")
print(f"Frequency: {freq}")

# Using Counter
from collections import Counter
freq2 = Counter(text)
print(f"Using Counter: {freq2}")

# Most common elements
print(f"Most common 3: {freq2.most_common(3)}")


# ============================================================================
# SUMMARY OF PATTERNS
# ============================================================================

print("\n" + "=" * 80)
print("SUMMARY - WHEN TO USE WHAT")
print("=" * 80)

summary = """
1. enumerate() - When you need index while iterating
2. zip() - When working with parallel arrays/lists
3. sorted(key=...) - When custom sorting is needed
4. map() - When transforming all elements
5. filter() - When selecting subset of elements
6. any()/all() - When checking boolean conditions
7. max()/min() with key - When finding extremes by criteria
8. reversed() - When iterating in reverse
9. isinstance() - When checking types
10. dict(zip()) - When creating dict from two lists
11. zip(*list) - When unzipping pairs
12. len(set()) - When checking uniqueness
13. filter(None) - When removing falsy values
14. reduce() - When reducing to single value
15. list comprehension - Often clearer than map/filter

Performance Tips:
- Use 'in' with sets/dicts for O(1) lookup
- Use any() for short-circuit evaluation
- Use enumerate() instead of range(len())
- Use sorted() for one-time sort, .sort() for in-place
"""

print(summary)

print("=" * 80)
print("🎯 MASTER THESE PATTERNS FOR INTERVIEWS!")
print("=" * 80)
