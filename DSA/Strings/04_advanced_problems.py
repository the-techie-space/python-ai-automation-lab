"""
Strings - Advanced Problems
============================
Master challenging string algorithms and patterns
"""

from collections import Counter

# ============================================================================
# ANAGRAM DETECTION
# ============================================================================
"""
Anagrams = Words with same characters, different order
Examples: "listen" & "silent", "evil" & "live"
"""

def are_anagrams(s1, s2):
    """
    Check if two strings are anagrams
    
    Args:
        s1, s2: Strings to compare
    
    Returns:
        bool: True if anagrams
    
    Time: O(n), Space: O(k) where k = unique characters
    """
    # Quick check: different lengths can't be anagrams
    if len(s1) != len(s2):
        return False
    
    # Method 1: Using sorted
    return sorted(s1) == sorted(s2)

def are_anagrams_frequency(s1, s2):
    """Anagram check using frequency counting (more efficient)"""
    if len(s1) != len(s2):
        return False
    
    freq1 = {}
    freq2 = {}
    
    for ch in s1:
        freq1[ch] = freq1.get(ch, 0) + 1
    
    for ch in s2:
        freq2[ch] = freq2.get(ch, 0) + 1
    
    return freq1 == freq2

# Test
print("="*60)
print("ANAGRAM DETECTION")
print("="*60)

anagram_pairs = [
    ("listen", "silent"),
    ("evil", "live"),
    ("hello", "world"),
    ("python", "typhon")
]

for s1, s2 in anagram_pairs:
    result1 = are_anagrams(s1, s2)
    result2 = are_anagrams_frequency(s1, s2)
    print(f"'{s1}' & '{s2}': {result1} (verified: {result2})")

# ============================================================================
# GROUP ANAGRAMS
# ============================================================================

def group_anagrams(words):
    """
    Group anagrams together
    
    Args:
        words: List of strings
    
    Returns:
        list: List of grouped anagrams
    
    Time: O(n * k log k) where n = words, k = avg word length
    """
    groups = {}
    
    for word in words:
        # Use sorted word as key
        key = "".join(sorted(word))
        if key not in groups:
            groups[key] = []
        groups[key].append(word)
    
    return list(groups.values())

# Test
print("\n" + "="*60)
print("GROUP ANAGRAMS")
print("="*60)

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
groups = group_anagrams(words)
print(f"Words: {words}")
print("Grouped:")
for i, group in enumerate(groups, 1):
    print(f"  Group {i}: {group}")

# ============================================================================
# LONGEST COMMON PREFIX
# ============================================================================

def longest_common_prefix(strings):
    """
    Find longest common prefix among strings
    
    Args:
        strings: List of strings
    
    Returns:
        str: Longest common prefix
    
    Time: O(n * m) where n = strings, m = min length
    
    Example:
        ["flower", "flow", "flight"] → "fl"
    """
    if not strings:
        return ""
    
    # Start with first string
    prefix = strings[0]
    
    for s in strings[1:]:
        # Reduce prefix until it matches
        while not s.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
    
    return prefix

# Alternative: Character-by-character
def longest_common_prefix_vertical(strings):
    """Vertical scanning approach"""
    if not strings:
        return ""
    
    for i in range(len(strings[0])):
        char = strings[0][i]
        
        # Check if all strings have this character at position i
        for s in strings[1:]:
            if i >= len(s) or s[i] != char:
                return strings[0][:i]
    
    return strings[0]

# Test
print("\n" + "="*60)
print("LONGEST COMMON PREFIX")
print("="*60)

test_cases = [
    ["flower", "flow", "flight"],
    ["dog", "racecar", "car"],
    ["interspecies", "interstellar", "interstate"],
    ["prefix", "pre", "prep"]
]

for strings in test_cases:
    result1 = longest_common_prefix(strings)
    result2 = longest_common_prefix_vertical(strings)
    print(f"\nStrings: {strings}")
    print(f"Prefix: '{result1}' (verified: '{result2}')")

# ============================================================================
# LONGEST PALINDROMIC SUBSTRING
# ============================================================================

def longest_palindrome_substring(s):
    """
    Find longest palindromic substring
    
    Args:
        s: Input string
    
    Returns:
        str: Longest palindrome substring
    
    Time: O(n²), Space: O(1)
    
    Strategy: Expand around center for each position
    """
    def expand_around_center(left, right):
        """Expand while characters match"""
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return s[left + 1:right]
    
    if len(s) < 2:
        return s
    
    longest = ""
    
    for i in range(len(s)):
        # Odd length palindrome (center is one character)
        palindrome1 = expand_around_center(i, i)
        # Even length palindrome (center is between two characters)
        palindrome2 = expand_around_center(i, i + 1)
        
        # Update longest
        current = palindrome1 if len(palindrome1) > len(palindrome2) else palindrome2
        if len(current) > len(longest):
            longest = current
    
    return longest

# Test
print("\n" + "="*60)
print("LONGEST PALINDROMIC SUBSTRING")
print("="*60)

test_strings = [
    "babad",
    "cbbd",
    "racecar",
    "abacabad"
]

for text in test_strings:
    result = longest_palindrome_substring(text)
    print(f"'{text}' → '{result}'")

# ============================================================================
# VALID PARENTHESES
# ============================================================================

def is_valid_parentheses(s):
    """
    Check if parentheses are balanced
    
    Args:
        s: String with (, ), {, }, [, ]
    
    Returns:
        bool: True if valid
    
    Time: O(n), Space: O(n)
    
    Example:
        "({[]})" → True
        "({[}])" → False
    """
    stack = []
    pairs = {'(': ')', '{': '}', '[': ']'}
    
    for ch in s:
        if ch in pairs:  # Opening bracket
            stack.append(ch)
        elif ch in pairs.values():  # Closing bracket
            if not stack or pairs[stack.pop()] != ch:
                return False
    
    return len(stack) == 0

# Test
print("\n" + "="*60)
print("VALID PARENTHESES")
print("="*60)

test_cases = [
    "()",
    "()[]{}",
    "(]",
    "([)]",
    "{[]}",
    "((()))"
]

for brackets in test_cases:
    result = is_valid_parentheses(brackets)
    print(f"'{brackets}': {result}")

# ============================================================================
# STRING TO INTEGER (atoi)
# ============================================================================

def string_to_int(s):
    """
    Convert string to integer (like atoi in C)
    
    Args:
        s: String representation of integer
    
    Returns:
        int: Converted integer
    
    Handles:
        - Leading/trailing whitespace
        - +/- signs
        - Invalid characters
    """
    s = s.strip()
    
    if not s:
        return 0
    
    sign = 1
    start = 0
    
    # Handle sign
    if s[0] in ['+', '-']:
        sign = -1 if s[0] == '-' else 1
        start = 1
    
    # Extract digits
    result = 0
    for i in range(start, len(s)):
        if not s[i].isdigit():
            break
        result = result * 10 + int(s[i])
    
    return sign * result

# Test
print("\n" + "="*60)
print("STRING TO INTEGER (atoi)")
print("="*60)

test_strings = [
    "42",
    "   -42",
    "4193 with words",
    "+123",
    "words and 987"
]

for text in test_strings:
    result = string_to_int(text)
    print(f"'{text}' → {result}")

# ============================================================================
# LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS
# ============================================================================

def longest_unique_substring(s):
    """
    Find length of longest substring without repeating characters
    
    Args:
        s: Input string
    
    Returns:
        tuple: (length, substring)
    
    Time: O(n), Space: O(k) where k = unique characters
    
    Strategy: Sliding window with hash set
    
    Example:
        "abcabcbb"
        
        Window [a,b,c] → length 3
        Window [b,c,a] → length 3
        Window [c,a,b] → length 3
        Max = 3
    """
    char_set = set()
    left = 0
    max_length = 0
    max_start = 0
    
    for right in range(len(s)):
        # Remove characters until no duplicate
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        
        # Update max
        if right - left + 1 > max_length:
            max_length = right - left + 1
            max_start = left
    
    return max_length, s[max_start:max_start + max_length]

# Test
print("\n" + "="*60)
print("LONGEST SUBSTRING WITHOUT REPEATING")
print("="*60)

test_strings = [
    "abcabcbb",
    "bbbbb",
    "pwwkew",
    "dvdf"
]

for text in test_strings:
    length, substring = longest_unique_substring(text)
    print(f"'{text}'")
    print(f"  Length: {length}, Substring: '{substring}'")

# ============================================================================
# ZIGZAG CONVERSION
# ============================================================================

def zigzag_convert(s, num_rows):
    """
    Convert string to zigzag pattern
    
    Args:
        s: Input string
        num_rows: Number of rows in zigzag
    
    Returns:
        str: String read row by row
    
    Example:
        "PAYPALISHIRING", numRows=3
        
        P   A   H   N
        A P L S I I G
        Y   I   R
        
        Result: "PAHNAPLSIIGYIR"
    """
    if num_rows == 1 or num_rows >= len(s):
        return s
    
    rows = [''] * num_rows
    current_row = 0
    going_down = False
    
    for char in s:
        rows[current_row] += char
        
        # Change direction at top or bottom
        if current_row == 0 or current_row == num_rows - 1:
            going_down = not going_down
        
        current_row += 1 if going_down else -1
    
    return ''.join(rows)

# Test
print("\n" + "="*60)
print("ZIGZAG CONVERSION")
print("="*60)

text = "PAYPALISHIRING"
for rows in [3, 4]:
    result = zigzag_convert(text, rows)
    print(f"'{text}' with {rows} rows:")
    print(f"  Result: '{result}'")

# ============================================================================
# STRING MATCHING (KMP Algorithm - Advanced)
# ============================================================================

def kmp_search(text, pattern):
    """
    Find all occurrences of pattern in text using KMP algorithm
    
    Args:
        text: Text to search in
        pattern: Pattern to search for
    
    Returns:
        list: Starting indices of all occurrences
    
    Time: O(n + m), Space: O(m)
    """
    def compute_lps(pattern):
        """Compute Longest Prefix Suffix array"""
        lps = [0] * len(pattern)
        length = 0
        i = 1
        
        while i < len(pattern):
            if pattern[i] == pattern[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1
        
        return lps
    
    if not pattern:
        return []
    
    lps = compute_lps(pattern)
    occurrences = []
    
    i = j = 0
    while i < len(text):
        if pattern[j] == text[i]:
            i += 1
            j += 1
        
        if j == len(pattern):
            occurrences.append(i - j)
            j = lps[j - 1]
        elif i < len(text) and pattern[j] != text[i]:
            if j != 0:
                j = lps[j - 1]
            else:
                i += 1
    
    return occurrences

# Test
print("\n" + "="*60)
print("STRING MATCHING (KMP)")
print("="*60)

text = "ababcabcabababd"
pattern = "ababd"
occurrences = kmp_search(text, pattern)
print(f"Text: '{text}'")
print(f"Pattern: '{pattern}'")
print(f"Occurrences at indices: {occurrences}")

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================
"""
ANAGRAMS:
✓ Same characters, different order
✓ Use sorted() or frequency counting
✓ Time: O(n log n) sorting, O(n) frequency

PALINDROMES:
✓ Expand around center for substrings
✓ Consider odd and even lengths
✓ Time: O(n²) for substring search

PARENTHESES:
✓ Use stack for matching
✓ Track opening/closing pairs
✓ Time: O(n), Space: O(n)

SLIDING WINDOW:
✓ For substring problems
✓ Use two pointers (left, right)
✓ Track characters in window with set/dict

KMP ALGORITHM:
✓ Efficient pattern matching
✓ Preprocessing with LPS array
✓ Time: O(n + m) vs naive O(n*m)

COMMON PATTERNS:
✓ Frequency counting: dict/Counter
✓ Two pointers: left/right or slow/fast
✓ Stack: matching/nesting problems
✓ Sliding window: substring problems
"""