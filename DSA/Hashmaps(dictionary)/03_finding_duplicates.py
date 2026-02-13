"""
Hash Maps - Finding Duplicates
===============================
Master duplicate detection using hash maps and sets
"""

# ============================================================================
# PATTERN: FINDING DUPLICATES
# ============================================================================
"""
Hash Maps excel at duplicate detection because:
- O(1) lookup to check if we've seen an element
- Can track first occurrence, all occurrences, etc.
"""

print("="*60)
print("DUPLICATE DETECTION PATTERNS")
print("="*60)

# ============================================================================
# PROBLEM 1: CONTAINS DUPLICATE
# ============================================================================
print("\n--- Problem 1: Contains Duplicate ---")
print("Return True if any value appears at least twice")

# Method 1: Using Dictionary with frequency count
def contains_duplicate_dict(nums):
    """
    Check if array contains duplicates
    
    Args:
        nums: List of numbers
    
    Returns:
        bool: True if duplicate exists
    
    Time: O(n), Space: O(n)
    """
    freq_dict = {}
    
    for num in nums:
        freq_dict[num] = freq_dict.get(num, 0) + 1
    
    # Check if any frequency > 1
    for count in freq_dict.values():
        if count > 1:
            return True
    return False

# Method 2: Using Dictionary (early return - better!)
def contains_duplicate_early_return(nums):
    """
    Early return as soon as duplicate is found
    More efficient!
    """
    seen = {}
    
    for num in nums:
        if num in seen:
            return True  # Found duplicate immediately!
        seen[num] = 1
    return False

# Method 3: Using Set (Most Efficient!)
def contains_duplicate_set(nums):
    """
    Set provides O(1) lookup
    Cleanest solution!
    """
    seen = set()
    
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    
    return False

# Method 4: One-liner (Pythonic)
def contains_duplicate_oneliner(nums):
    """
    Compare length of list vs set
    If duplicate exists, set will be smaller!
    """
    return len(nums) != len(set(nums))

# Test all methods
print("\nTesting all methods:")
test_cases = [
    [1, 2, 3, 1],
    [1, 2, 3, 4],
    [1, 1, 1, 3, 3, 4, 3, 2, 4, 2]
]

for nums in test_cases:
    print(f"\nInput: {nums}")
    print(f"  Method 1 (dict): {contains_duplicate_dict(nums)}")
    print(f"  Method 2 (early): {contains_duplicate_early_return(nums)}")
    print(f"  Method 3 (set): {contains_duplicate_set(nums)}")
    print(f"  Method 4 (one-liner): {contains_duplicate_oneliner(nums)}")

# ============================================================================
# PROBLEM 2: FIRST DUPLICATE
# ============================================================================
print("\n" + "="*60)
print("PROBLEM 2: FIND FIRST DUPLICATE")
print("="*60)

def first_duplicate(nums):
    """
    Find the first number that appears twice
    
    Args:
        nums: List of numbers
    
    Returns:
        int/None: First duplicate or None if no duplicate
    
    Time: O(n), Space: O(n)
    
    Example:
        [2, 1, 3, 5, 3, 2] → 3 (first to appear twice)
    """
    seen = set()  # Track what we've seen
    
    for num in nums:
        if num in seen:
            return num  # Found first duplicate!
        seen.add(num)
    
    return None  # No duplicate found

# Test
print("\nTest cases:")
test_cases = [
    [2, 1, 3, 5, 3, 2],
    [1, 2, 3, 4],
    [5, 5, 1, 2],
]

for nums in test_cases:
    result = first_duplicate(nums)
    print(f"{nums} → First duplicate: {result}")

# ============================================================================
# PROBLEM 3: FIND ALL DUPLICATES
# ============================================================================
print("\n" + "="*60)
print("PROBLEM 3: FIND ALL DUPLICATES")
print("="*60)

def find_all_duplicates(nums):
    """
    Find all numbers that appear more than once
    
    Args:
        nums: List of numbers
    
    Returns:
        list: All duplicate numbers
    
    Time: O(n), Space: O(n)
    
    Example:
        [1, 2, 3, 2, 4, 3, 5] → [2, 3]
    """
    count = {}
    
    # Count occurrences
    for num in nums:
        count[num] = count.get(num, 0) + 1
    
    # Find numbers with count > 1
    duplicates = [num for num, freq in count.items() if freq > 1]
    
    return duplicates

# Test
print("\nTest cases:")
test_cases = [
    [1, 2, 3, 2, 4, 3, 5],
    [1, 1, 2, 2, 3, 3],
    [1, 2, 3, 4, 5],
]

for nums in test_cases:
    result = find_all_duplicates(nums)
    print(f"{nums} → Duplicates: {result}")

# ============================================================================
# PROBLEM 4: FIRST UNIQUE (NON-DUPLICATE) ELEMENT
# ============================================================================
print("\n" + "="*60)
print("PROBLEM 4: FIRST UNIQUE ELEMENT")
print("="*60)

def first_unique_number(nums):
    """
    Find first number that appears only once
    
    Args:
        nums: List of numbers
    
    Returns:
        int/None: First unique number or None
    
    Time: O(n), Space: O(n)
    
    Example:
        [4, 5, 1, 2, 1, 4] → 5 (first unique)
    """
    count = {}
    
    # Count frequencies
    for num in nums:
        count[num] = count.get(num, 0) + 1
    
    # Find first with frequency 1 (maintain order!)
    for num in nums:
        if count[num] == 1:
            return num
    
    return None

# Test
print("\nTest cases:")
test_cases = [
    [4, 5, 1, 2, 1, 4],
    [1, 1, 2, 2, 3],
    [1, 2, 3, 4],
]

for nums in test_cases:
    result = first_unique_number(nums)
    print(f"{nums} → First unique: {result}")

# ============================================================================
# PROBLEM 5: FIRST UNIQUE CHARACTER IN STRING
# ============================================================================
print("\n" + "="*60)
print("PROBLEM 5: FIRST UNIQUE CHARACTER IN STRING")
print("="*60)

def first_unique_char(s):
    """
    Find the first non-repeating character in a string
    Return its index. If doesn't exist, return -1
    
    Args:
        s: Input string
    
    Returns:
        int: Index of first unique character or -1
    
    Time: O(n), Space: O(k) where k = unique characters
    
    Example:
        "leetcode" → 0 (because 'l' appears only once)
        "loveleetcode" → 2 (because 'v' is first unique)
        "aabb" → -1 (no unique character)
    """
    # Step 1: Count frequency
    freq_dict = {}
    for ch in s:
        freq_dict[ch] = freq_dict.get(ch, 0) + 1
    
    # Step 2: Find first character with frequency 1
    for index, char in enumerate(s):
        if freq_dict[char] == 1:
            return index
    
    return -1

# Using Counter for cleaner code
from collections import Counter

def first_unique_char_counter(s):
    """Using Counter for cleaner implementation"""
    freq = Counter(s)
    
    for i, char in enumerate(s):
        if freq[char] == 1:
            return i
    
    return -1

# Test
print("\nTest cases:")
test_cases = [
    "leetcode",
    "loveleetcode",
    "aabb",
    "z"
]

for text in test_cases:
    result1 = first_unique_char(text)
    result2 = first_unique_char_counter(text)
    print(f"'{text}' → Index: {result1} (verified: {result2})")

# ============================================================================
# PROBLEM 6: DUPLICATE WITHIN K DISTANCE
# ============================================================================
print("\n" + "="*60)
print("PROBLEM 6: DUPLICATE WITHIN K DISTANCE")
print("="*60)

def contains_nearby_duplicate(nums, k):
    """
    Check if there are duplicates within k distance
    
    Args:
        nums: List of numbers
        k: Maximum distance
    
    Returns:
        bool: True if duplicate exists within k distance
    
    Time: O(n), Space: O(min(n, k))
    
    Example:
        nums = [1,2,3,1], k = 3 → True (1 appears at index 0 and 3)
        nums = [1,2,3,1,2,3], k = 2 → False
    """
    seen = {}  # num → last seen index
    
    for i, num in enumerate(nums):
        if num in seen and i - seen[num] <= k:
            return True
        seen[num] = i
    
    return False

# Test
print("\nTest cases:")
test_cases = [
    ([1, 2, 3, 1], 3),
    ([1, 0, 1, 1], 1),
    ([1, 2, 3, 1, 2, 3], 2),
]

for nums, k in test_cases:
    result = contains_nearby_duplicate(nums, k)
    print(f"{nums}, k={k} → {result}")

# ============================================================================
# PROBLEM 7: COUNT DISTINCT ELEMENTS
# ============================================================================
print("\n" + "="*60)
print("PROBLEM 7: COUNT DISTINCT ELEMENTS")
print("="*60)

def count_distinct(nums):
    """
    Count number of unique elements
    
    Args:
        nums: List of numbers
    
    Returns:
        int: Count of distinct elements
    
    Time: O(n), Space: O(k)
    """
    return len(set(nums))

# Alternative with dictionary
def count_distinct_dict(nums):
    """Using dictionary"""
    seen = {}
    for num in nums:
        seen[num] = True
    return len(seen)

# Test
print("\nTest cases:")
test_cases = [
    [1, 2, 3, 2, 1],
    [1, 1, 1, 1],
    [1, 2, 3, 4, 5],
]

for nums in test_cases:
    result1 = count_distinct(nums)
    result2 = count_distinct_dict(nums)
    print(f"{nums} → Distinct: {result1} (verified: {result2})")

# ============================================================================
# COMPARISON: DICTIONARY vs SET
# ============================================================================
print("\n" + "="*60)
print("WHEN TO USE DICTIONARY vs SET")
print("="*60)

comparison = """
USE SET WHEN:
✓ Only need to track existence (seen/not seen)
✓ Don't need to store additional information
✓ Simpler and more memory efficient
Example: Contains duplicate, First duplicate

USE DICTIONARY WHEN:
✓ Need to store associated data (index, count, etc.)
✓ Need to track frequency
✓ Need to access/update values
Example: First unique character, Nearby duplicate
"""
print(comparison)

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================
"""
DUPLICATE DETECTION:
✓ Use set for simple existence check: O(n) time, O(n) space
✓ Use dict when need to track additional info
✓ Early return optimization: return as soon as found

PATTERNS:
1. Contains duplicate: if num in seen
2. First duplicate: seen.add(), return on duplicate
3. All duplicates: count[num] > 1
4. First unique: count[num] == 1 (maintain order!)
5. Nearby duplicate: track indices in dict

OPTIMIZATION:
✓ Set is faster than dict for simple checks
✓ Early return saves time
✓ len(set(nums)) != len(nums) for quick check

COMMON VARIATIONS:
✓ Character vs number duplicates (same logic)
✓ Case-insensitive: text.lower() first
✓ Within K distance: track indices
✓ Count distinct: len(set())

INTERVIEW TIPS:
✓ Always consider early return
✓ Choose set vs dict based on what you need
✓ Remember to maintain order for "first" problems
✓ Handle edge cases: empty array, single element
"""

print("\n" + "="*60)
print("✓ Duplicate detection patterns mastered!")
print("="*60)