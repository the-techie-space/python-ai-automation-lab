"""
Strings - Palindromes & Character Frequency
============================================
Learn palindrome checking and frequency counting techniques
"""

# ============================================================================
# PALINDROME CHECKING
# ============================================================================
"""
Palindrome = A string that reads the same forwards and backwards
Examples: "racecar", "A man a plan a canal Panama", "madam"

Approach:
1. Clean the string (remove non-alphanumeric, convert to lowercase)
2. Use two pointers from both ends
3. Compare characters moving inward
"""

def is_palindrome_simple(s):
    """
    Simple palindrome check
    
    Args:
        s: Input string
    
    Returns:
        bool: True if palindrome
    
    Time: O(n), Space: O(1)
    """
    # Reverse and compare
    return s == s[::-1]

# Test simple method
print("="*60)
print("SIMPLE PALINDROME CHECK")
print("="*60)
test_words = ["racecar", "hello", "madam", "python"]
for word in test_words:
    result = is_palindrome_simple(word)
    print(f"'{word}': {result}")

# ============================================================================
# PALINDROME WITH CLEANING (Ignoring Spaces & Punctuation)
# ============================================================================

def is_palindrome_advanced(s):
    """
    Advanced palindrome check - ignores spaces, punctuation, case
    
    Args:
        s: Input string
    
    Returns:
        bool: True if palindrome
    
    Time: O(n), Space: O(n) for cleaned string
    
    Example:
        "A man, a plan, a canal: Panama"
        → Clean: "amanaplanacanalpanama"
        → Check: a m a n a p l a n a c a n a l p a n a m a
                 ↑                                       ↑
                 Match all the way through!
    """
    # Step 1: Clean the string
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    
    # Step 2: Use two pointers
    left, right = 0, len(cleaned) - 1
    
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    
    return True

# Test advanced method
print("\n" + "="*60)
print("ADVANCED PALINDROME CHECK (with cleaning)")
print("="*60)

test_sentences = [
    "A man a plan a canal Panama",
    "race a car",
    "Was it a car or a cat I saw?",
    "Madam",
    "Hello World"
]

for sentence in test_sentences:
    result = is_palindrome_advanced(sentence)
    print(f"'{sentence}'")
    print(f"  → {result}\n")

# ============================================================================
# STEP-BY-STEP VISUALIZATION
# ============================================================================

def palindrome_with_visualization(s):
    """Show step-by-step palindrome checking"""
    print(f"\nChecking: '{s}'")
    
    # Step 1: Clean
    cleaned = "".join(ch.lower() for ch in s if ch.isalnum())
    print(f"Cleaned: '{cleaned}'")
    
    # Step 2: Two pointer check
    left, right = 0, len(cleaned) - 1
    step = 1
    
    while left < right:
        print(f"Step {step}: cleaned[{left}]='{cleaned[left]}' vs cleaned[{right}]='{cleaned[right]}'", end="")
        
        if cleaned[left] != cleaned[right]:
            print(" → MISMATCH ✗")
            return False
        
        print(" → MATCH ✓")
        left += 1
        right -= 1
        step += 1
    
    print("All characters match → PALINDROME ✓")
    return True

# Visualize one example
print("\n" + "="*60)
print("PALINDROME VISUALIZATION")
print("="*60)
palindrome_with_visualization("A man a plan a canal Panama")

# ============================================================================
# CHARACTER FREQUENCY COUNTING
# ============================================================================
"""
Frequency Counting = Track how many times each character appears
Use: Dictionary with character as key, count as value
"""

def character_frequency(s):
    """
    Count frequency of each character
    
    Args:
        s: Input string
    
    Returns:
        dict: Character frequencies
    
    Time: O(n), Space: O(k) where k = unique characters
    """
    freq_dict = {}
    
    for ch in s:
        freq_dict[ch] = freq_dict.get(ch, 0) + 1
    
    return freq_dict

# Test
print("\n" + "="*60)
print("CHARACTER FREQUENCY")
print("="*60)

text = "programming"
freq = character_frequency(text)
print(f"String: '{text}'")
print("Frequencies:")
for char, count in sorted(freq.items()):
    print(f"  '{char}': {count}")

# ============================================================================
# FIRST NON-REPEATING CHARACTER
# ============================================================================
"""
Find the first character that appears only once
Approach:
1. Build frequency dictionary
2. Iterate through original string
3. Return first character with frequency 1
"""

def first_non_repeating_char(s):
    """
    Find first non-repeating character
    
    Args:
        s: Input string
    
    Returns:
        str/None: First non-repeating character or None
    
    Time: O(n), Space: O(k)
    
    Example:
        "aabbcddee" → 'c'
        "programming" → 'p'
    """
    # Step 1: Build frequency dictionary
    freq_dict = {}
    for ch in s:
        freq_dict[ch] = freq_dict.get(ch, 0) + 1
    
    # Step 2: Find first with count 1
    for ch in s:
        if freq_dict[ch] == 1:
            return ch
    
    return None

# Test
print("\n" + "="*60)
print("FIRST NON-REPEATING CHARACTER")
print("="*60)

test_strings = [
    "aabbcddee",
    "programming",
    "aabbcc",
    "abcdef"
]

for text in test_strings:
    result = first_non_repeating_char(text)
    freq = character_frequency(text)
    print(f"\nString: '{text}'")
    print(f"Frequencies: {freq}")
    print(f"First non-repeating: {result if result else 'None'}")

# ============================================================================
# FIND ALL DUPLICATE CHARACTERS
# ============================================================================

def find_duplicates(s):
    """
    Find all characters that appear more than once
    
    Args:
        s: Input string
    
    Returns:
        list: List of duplicate characters (in order of first duplicate)
    
    Time: O(n), Space: O(k)
    """
    freq_dict = {}
    
    # Count frequencies
    for ch in s:
        freq_dict[ch] = freq_dict.get(ch, 0) + 1
    
    # Find duplicates (preserve order)
    seen = set()
    duplicates = []
    
    for ch in s:
        if freq_dict[ch] > 1 and ch not in seen:
            duplicates.append(ch)
            seen.add(ch)
    
    return duplicates

# Test
print("\n" + "="*60)
print("FIND DUPLICATE CHARACTERS")
print("="*60)

test_strings = [
    "programming",
    "hello",
    "banana",
    "abcdef"
]

for text in test_strings:
    duplicates = find_duplicates(text)
    print(f"\nString: '{text}'")
    print(f"Duplicates: {duplicates if duplicates else 'None'}")

# ============================================================================
# MAXIMUM OCCURRING CHARACTER
# ============================================================================

def max_occurring_char(s):
    """
    Find the character that appears most frequently
    
    Args:
        s: Input string
    
    Returns:
        tuple: (character, count) or (None, 0) if empty
    
    Time: O(n), Space: O(k)
    """
    if not s:
        return None, 0
    
    # Build frequency dictionary
    freq_dict = {}
    for ch in s:
        freq_dict[ch] = freq_dict.get(ch, 0) + 1
    
    # Find maximum
    max_char = s[0]
    for ch in s:
        if freq_dict[ch] > freq_dict[max_char]:
            max_char = ch
    
    return max_char, freq_dict[max_char]

# Alternative using max() function
def max_occurring_char_pythonic(s):
    """Pythonic way using max()"""
    if not s:
        return None, 0
    
    freq_dict = {}
    for ch in s:
        freq_dict[ch] = freq_dict.get(ch, 0) + 1
    
    max_char = max(freq_dict, key=freq_dict.get)
    return max_char, freq_dict[max_char]

# Test
print("\n" + "="*60)
print("MAXIMUM OCCURRING CHARACTER")
print("="*60)

test_strings = [
    "abbccc",
    "programming",
    "aabbccdd",
    "hello world"
]

for text in test_strings:
    char, count = max_occurring_char(text)
    char2, count2 = max_occurring_char_pythonic(text)
    
    print(f"\nString: '{text}'")
    print(f"Most frequent: '{char}' appears {count} times")
    print(f"Verification: '{char2}' appears {count2} times")

# ============================================================================
# COUNT VOWELS & CONSONANTS
# ============================================================================

def count_vowels_consonants(s):
    """
    Count vowels and consonants in string
    
    Args:
        s: Input string
    
    Returns:
        tuple: (vowel_count, consonant_count)
    
    Time: O(n), Space: O(1)
    """
    s = s.lower()
    vowels = set('aeiou')
    
    vowel_count = 0
    consonant_count = 0
    
    for ch in s:
        if ch.isalpha():
            if ch in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    return vowel_count, consonant_count

# Test
print("\n" + "="*60)
print("COUNT VOWELS & CONSONANTS")
print("="*60)

test_strings = [
    "Interview",
    "Programming",
    "Python is awesome",
    "aeiou"
]

for text in test_strings:
    vowels, consonants = count_vowels_consonants(text)
    print(f"\nString: '{text}'")
    print(f"Vowels: {vowels}, Consonants: {consonants}")

# ============================================================================
# COMPREHENSIVE EXAMPLE
# ============================================================================

def analyze_string(s):
    """Comprehensive string analysis"""
    print(f"\n{'='*60}")
    print(f"ANALYZING: '{s}'")
    print('='*60)
    
    # Basic info
    print(f"Length: {len(s)}")
    print(f"Palindrome: {is_palindrome_advanced(s)}")
    
    # Character frequency
    freq = character_frequency(s)
    print(f"\nCharacter frequencies:")
    for char, count in sorted(freq.items(), key=lambda x: -x[1])[:5]:
        print(f"  '{char}': {count}")
    
    # First non-repeating
    first_non_rep = first_non_repeating_char(s)
    print(f"\nFirst non-repeating: {first_non_rep if first_non_rep else 'None'}")
    
    # Duplicates
    dups = find_duplicates(s)
    print(f"Duplicates: {dups if dups else 'None'}")
    
    # Max occurring
    max_char, max_count = max_occurring_char(s)
    print(f"Most frequent: '{max_char}' ({max_count} times)")
    
    # Vowels & consonants
    vowels, consonants = count_vowels_consonants(s)
    print(f"Vowels: {vowels}, Consonants: {consonants}")

# Analyze example string
analyze_string("programming")
analyze_string("A man a plan a canal Panama")

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================
"""
PALINDROME CHECKING:
✓ Simple: s == s[::-1]
✓ Advanced: Clean first, use two pointers
✓ Time: O(n), Space: O(1) or O(n) if cleaning

FREQUENCY COUNTING:
✓ Use dictionary: freq[ch] = freq.get(ch, 0) + 1
✓ Time: O(n), Space: O(k) where k = unique chars
✓ Foundation for many string problems

FIRST NON-REPEATING:
✓ Build frequency dict first
✓ Then scan original string
✓ Order matters! Use original string order

FINDING DUPLICATES:
✓ Frequency > 1
✓ Preserve order using seen set
✓ Return list in order of first occurrence

MAX OCCURRING:
✓ Find character with highest frequency
✓ Can use max(dict, key=dict.get)
✓ Track as you count for efficiency

PATTERN:
✓ Most string problems use frequency counting
✓ Dictionary is your best friend
✓ Consider order of operations
"""