"""
Hash Maps - Grouping & Anagram Patterns
========================================
Master grouping elements by keys and anagram detection
"""

from collections import defaultdict

# ============================================================================
# GROUPING PATTERN - Core Concept
# ============================================================================
"""
Grouping Pattern:
- Group elements that share a common property
- Use that property as the KEY
- Store related elements in a list as VALUE
- Pattern: dict[key] = list of items

Common applications:
- Group anagrams
- Group by sum of digits
- Group by length
- Group by any computed property
"""

print("="*60)
print("GROUPING PATTERN - Core Concept")
print("="*60)

# ============================================================================
# PROBLEM 1: GROUP ANAGRAMS ⭐⭐⭐
# ============================================================================
"""
This is a TOP interview question!

Problem:
Group strings that are anagrams of each other

Example:
    Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
    Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]]

Explanation:
    "eat", "tea", "ate" are anagrams (same letters, different order)
    "tan", "nat" are anagrams
    "bat" is alone
"""

print("\n--- Problem 1: Group Anagrams ---")

# Method 1: Using sorted string as key
def group_anagrams(strs):
    """
    Group anagrams using sorted string as key
    
    Args:
        strs: List of strings
    
    Returns:
        list: Grouped anagrams
    
    Time: O(n * k log k) where n=words, k=max word length
    Space: O(n * k)
    
    Strategy:
        Anagrams have same sorted form!
        "eat" → sorted → "aet"
        "tea" → sorted → "aet"  (same key!)
        "ate" → sorted → "aet"  (same key!)
    """
    groups = defaultdict(list)
    
    for word in strs:
        # Sort the word to get the key
        key = ''.join(sorted(word))
        
        # Add original word to the group
        groups[key].append(word)
    
    # Return all groups as a list
    return list(groups.values())

# Test
print("\nTest case:")
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(words)
print(f"Input: {words}")
print(f"Output: {result}")

# Step-by-step visualization
def group_anagrams_visual(strs):
    """Show the grouping process step by step"""
    groups = {}
    
    print("\nStep-by-step grouping:")
    print("-" * 60)
    
    for i, word in enumerate(strs):
        key = ''.join(sorted(word))
        
        print(f"\nStep {i+1}: word='{word}'")
        print(f"  Sorted key: '{key}'")
        
        if key in groups:
            groups[key].append(word)
            print(f"  Added to existing group: {groups[key]}")
        else:
            groups[key] = [word]
            print(f"  Created new group: {groups[key]}")
    
    print("\n" + "="*60)
    print("Final groups:")
    for key, group in groups.items():
        print(f"  Key '{key}': {group}")
    
    return list(groups.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams_visual(words)

# ============================================================================
# PROBLEM 2: GROUP BY DIGIT SUM
# ============================================================================
print("\n" + "="*60)
print("PROBLEM 2: Group by Digit Sum")
print("="*60)

def group_by_digit_sum(nums):
    """
    Group numbers with same digit sum
    
    Args:
        nums: List of integers
    
    Returns:
        list: Grouped numbers
    
    Example:
        Input: [12, 21, 30, 11, 102]
        Output: [[12, 21, 30, 102], [11]]
        
        Explanation:
        12 → 1+2=3
        21 → 2+1=3  (same as 12!)
        30 → 3+0=3  (same as 12!)
        11 → 1+1=2
        102 → 1+0+2=3 (same as 12!)
    """
    groups = defaultdict(list)
    
    for num in nums:
        # Calculate digit sum
        digit_sum = sum(int(d) for d in str(num))
        
        # Add to group
        groups[digit_sum].append(num)
    
    return list(groups.values())

# Test
print("\nTest case:")
nums = [12, 21, 30, 11, 102, 20]
result = group_by_digit_sum(nums)
print(f"Input: {nums}")
print(f"Grouped by digit sum: {result}")

# Show digit sums
print("\nDigit sums:")
for num in nums:
    digit_sum = sum(int(d) for d in str(num))
    print(f"  {num} → {digit_sum}")

# ============================================================================
# PROBLEM 3: GROUP BY LENGTH
# ============================================================================
print("\n" + "="*60)
print("PROBLEM 3: Group by Length")
print("="*60)

def group_by_length(words):
    """
    Group words by their length
    
    Args:
        words: List of strings
    
    Returns:
        dict: Length → list of words
    """
    groups = defaultdict(list)
    
    for word in words:
        length = len(word)
        groups[length].append(word)
    
    return dict(groups)

# Test
print("\nTest case:")
words = ["a", "bb", "ccc", "dd", "e", "fff", "g"]
result = group_by_length(words)
print(f"Input: {words}")
print(f"Grouped by length:")
for length, group in sorted(result.items()):
    print(f"  Length {length}: {group}")

# ============================================================================
# PROBLEM 4: GROUP BY FIRST CHARACTER
# ============================================================================
print("\n" + "="*60)
print("PROBLEM 4: Group by First Character")
print("="*60)

def group_by_first_char(words):
    """
    Group words by their first character
    
    Args:
        words: List of strings
    
    Returns:
        dict: First char → list of words
    """
    groups = defaultdict(list)
    
    for word in words:
        if word:  # Check not empty
            first_char = word[0].lower()
            groups[first_char].append(word)
    
    return dict(groups)

# Test
print("\nTest case:")
words = ["apple", "ant", "banana", "bear", "cat", "ant", "apple"]
result = group_by_first_char(words)
print(f"Input: {words}")
print(f"Grouped by first character:")
for char, group in sorted(result.items()):
    print(f"  '{char}': {group}")

# ============================================================================
# PROBLEM 5: VALID ANAGRAM (Simple Check)
# ============================================================================
print("\n" + "="*60)
print("PROBLEM 5: Valid Anagram (Simple Check)")
print("="*60)

def is_anagram(s1, s2):
    """
    Check if two strings are anagrams
    
    Args:
        s1, s2: Strings to compare
    
    Returns:
        bool: True if anagrams
    
    Time: O(n log n) for sorting, or O(n) for frequency
    """
    # Quick check: different lengths can't be anagrams
    if len(s1) != len(s2):
        return False
    
    # Method 1: Using sorted
    return sorted(s1) == sorted(s2)

def is_anagram_frequency(s1, s2):
    """
    Using frequency counting (more efficient)
    
    Time: O(n), Space: O(k) where k = unique chars
    """
    if len(s1) != len(s2):
        return False
    
    freq1 = {}
    freq2 = {}
    
    for ch in s1:
        freq1[ch] = freq1.get(ch, 0) + 1
    
    for ch in s2:
        freq2[ch] = freq2.get(ch, 0) + 1
    
    return freq1 == freq2

# Using Counter (cleanest)
from collections import Counter

def is_anagram_counter(s1, s2):
    """Using Counter - most Pythonic"""
    return Counter(s1) == Counter(s2)

# Test
print("\nTest cases:")
test_pairs = [
    ("listen", "silent"),
    ("evil", "vile"),
    ("hello", "world"),
    ("python", "typhon")
]

for s1, s2 in test_pairs:
    result1 = is_anagram(s1, s2)
    result2 = is_anagram_frequency(s1, s2)
    result3 = is_anagram_counter(s1, s2)
    print(f"\n'{s1}' & '{s2}':")
    print(f"  Sorted method: {result1}")
    print(f"  Frequency method: {result2}")
    print(f"  Counter method: {result3}")

# ============================================================================
# PROBLEM 6: GROUP SHIFTED STRINGS
# ============================================================================
print("\n" + "="*60)
print("PROBLEM 6: Group Shifted Strings (Advanced)")
print("="*60)

def group_shifted_strings(words):
    """
    Group strings that can be shifted to match each other
    
    Example:
        "abc" shifted by 1 → "bcd"
        "xyz" shifted by 1 → "yza"
    
    Strategy:
        Convert each string to a pattern based on differences
        "abc" → (1,1) because b-a=1, c-b=1
        "bcd" → (1,1) same pattern!
    """
    groups = defaultdict(list)
    
    for word in words:
        # Create pattern based on character differences
        if len(word) == 0:
            key = ()
        else:
            key = tuple((ord(word[i]) - ord(word[i-1])) % 26 
                       for i in range(1, len(word)))
        
        groups[key].append(word)
    
    return list(groups.values())

# Test
print("\nTest case:")
words = ["abc", "bcd", "xyz", "yza", "ace"]
result = group_shifted_strings(words)
print(f"Input: {words}")
print(f"Grouped shifted strings: {result}")

# ============================================================================
# GENERIC GROUPING TEMPLATE
# ============================================================================
print("\n" + "="*60)
print("GENERIC GROUPING TEMPLATE")
print("="*60)

template = """
GROUPING PATTERN TEMPLATE:

def group_by_property(items):
    '''
    Generic template for grouping
    '''
    groups = defaultdict(list)  # or {}
    
    for item in items:
        # 1. Calculate the KEY (property to group by)
        key = calculate_key(item)
        
        # 2. Add item to group
        groups[key].append(item)
    
    # 3. Return groups (as list or dict)
    return list(groups.values())  # or dict(groups)


COMMON KEY CALCULATIONS:
✓ Sorted string: ''.join(sorted(word))
✓ Digit sum: sum(int(d) for d in str(num))
✓ Length: len(item)
✓ First character: item[0]
✓ Custom function: any calculation!

WHEN TO USE:
✓ "Group items that..."
✓ "Find all items with same..."
✓ "Categorize by..."
✓ Anagram problems
"""
print(template)

# ============================================================================
# PRACTICE PROBLEMS
# ============================================================================
print("\n" + "="*60)
print("PRACTICE PROBLEMS")
print("="*60)

practice = """
EASY:
✓ Valid Anagram
✓ Group words by length
✓ Group numbers by last digit

MEDIUM:
✓ Group Anagrams ⭐
✓ Group by digit sum
✓ Group strings by first/last character
✓ Find common characters in strings

HARD:
✓ Group shifted strings
✓ Group by custom pattern
✓ Longest anagram chain
"""
print(practice)

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================
"""
GROUPING PATTERN:
✓ Use hash map where key = common property
✓ Value = list of items with that property
✓ Use defaultdict(list) for automatic initialization

ANAGRAM DETECTION:
✓ Sorted string as key: O(n log n)
✓ Frequency count: O(n)
✓ Anagrams have identical sorted form

GROUPING STRATEGIES:
1. Calculate KEY (the grouping property)
2. Add item to groups[key]
3. Return list(groups.values())

COMMON KEYS:
✓ Sorted string (anagrams)
✓ Sum of digits
✓ Length
✓ First/last character
✓ Custom calculation

DEFAULTDICT BENEFIT:
✓ Automatically creates empty list for new keys
✓ No need for "if key not in dict" checks
✓ Cleaner code

INTERVIEW TIPS:
✓ Identify the grouping property first
✓ Decide on key calculation
✓ Consider time complexity of key calculation
✓ Use defaultdict for cleaner code
✓ Return appropriate format (list vs dict)
"""

print("\n" + "="*60)
print("✓ Grouping and anagram patterns mastered!")
print("="*60)