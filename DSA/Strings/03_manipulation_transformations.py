"""
Strings - Manipulation & Transformations
=========================================
Learn string compression, deduplication, and transformations
"""

# ============================================================================
# REMOVE DUPLICATE CHARACTERS (Preserve Order)
# ============================================================================
"""
Remove duplicates while maintaining first occurrence order
Example: "banana" → "ban"
"""

def remove_duplicates(s):
    """
    Remove duplicate characters, keep first occurrence
    
    Args:
        s: Input string
    
    Returns:
        str: String without duplicates
    
    Time: O(n), Space: O(n)
    
    Strategy:
        Use a set to track seen characters
        Append to result only if not seen
    """
    seen = set()
    result = []
    
    for ch in s:
        if ch not in seen:
            seen.add(ch)
            result.append(ch)
    
    return "".join(result)

# Test
print("="*60)
print("REMOVE DUPLICATE CHARACTERS")
print("="*60)

test_strings = [
    "banana",
    "programming",
    "hello",
    "aabbcc",
    "abcabc"
]

for text in test_strings:
    result = remove_duplicates(text)
    print(f"'{text}' → '{result}'")

# ============================================================================
# STRING COMPRESSION
# ============================================================================
"""
Compress string by replacing consecutive characters with count
Example: "aaabbc" → "a3b2c1"
"""

def compress_string(s):
    """
    Compress consecutive characters
    
    Args:
        s: Input string
    
    Returns:
        str: Compressed string
    
    Time: O(n), Space: O(n)
    
    Example:
        "aaabbc"
        
        i=1: 'a' == 'a' → count=2
        i=2: 'a' == 'a' → count=3
        i=3: 'b' != 'a' → append "a3", reset count=1
        i=4: 'b' == 'b' → count=2
        i=5: 'c' != 'b' → append "b2", reset count=1
        End: append "c1"
        
        Result: "a3b2c1"
    """
    if not s:
        return ""
    
    result = []
    count = 1
    
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result.append(s[i - 1] + str(count))
            count = 1
    
    # Don't forget the last character!
    result.append(s[-1] + str(count))
    
    return "".join(result)

# Test
print("\n" + "="*60)
print("STRING COMPRESSION")
print("="*60)

test_strings = [
    "aaabbc",
    "aabbccdd",
    "abc",
    "aaaa",
    "aabbbcccc"
]

for text in test_strings:
    compressed = compress_string(text)
    print(f"'{text}' → '{compressed}'")

# ============================================================================
# IMPROVED COMPRESSION (Only if shorter)
# ============================================================================

def compress_string_smart(s):
    """
    Compress only if result is shorter than original
    
    Args:
        s: Input string
    
    Returns:
        str: Compressed or original string (whichever is shorter)
    """
    compressed = compress_string(s)
    return compressed if len(compressed) < len(s) else s

# Test
print("\n" + "="*60)
print("SMART COMPRESSION (only if shorter)")
print("="*60)

test_strings = [
    "aaabbc",     # Will compress
    "abc",        # Won't compress (longer)
    "aabbccdd",   # Won't compress (same length)
    "aaaa"        # Will compress
]

for text in test_strings:
    result = compress_string_smart(text)
    print(f"'{text}' → '{result}'")

# ============================================================================
# STRING DECOMPRESSION
# ============================================================================

def decompress_string(s):
    """
    Decompress a compressed string
    
    Args:
        s: Compressed string (e.g., "a3b2c1")
    
    Returns:
        str: Decompressed string
    
    Time: O(n), Space: O(n)
    
    Example:
        "a3b2c1" → "aaabbc"
    """
    result = []
    i = 0
    
    while i < len(s):
        char = s[i]
        i += 1
        
        # Extract the count (could be multi-digit)
        count_str = ""
        while i < len(s) and s[i].isdigit():
            count_str += s[i]
            i += 1
        
        count = int(count_str) if count_str else 1
        result.append(char * count)
    
    return "".join(result)

# Test
print("\n" + "="*60)
print("STRING DECOMPRESSION")
print("="*60)

compressed_strings = [
    "a3b2c1",
    "a4",
    "a1b1c1",
    "a10b2"
]

for compressed in compressed_strings:
    decompressed = decompress_string(compressed)
    print(f"'{compressed}' → '{decompressed}'")

# Round-trip test
print("\n--- Round-Trip Test ---")
original = "aaabbc"
compressed = compress_string(original)
decompressed = decompress_string(compressed)
print(f"Original: '{original}'")
print(f"Compressed: '{compressed}'")
print(f"Decompressed: '{decompressed}'")
print(f"Match: {original == decompressed}")

# ============================================================================
# REVERSE WORDS IN STRING
# ============================================================================

def reverse_words(s):
    """
    Reverse the order of words
    
    Args:
        s: Input string
    
    Returns:
        str: String with words in reverse order
    
    Example:
        "Hello World" → "World Hello"
    """
    words = s.split()
    return " ".join(reversed(words))

# Alternative without reversed()
def reverse_words_manual(s):
    """Manual reversal"""
    words = s.split()
    return " ".join(words[::-1])

# Test
print("\n" + "="*60)
print("REVERSE WORDS")
print("="*60)

test_strings = [
    "Hello World",
    "Python is awesome",
    "One",
    "The quick brown fox"
]

for text in test_strings:
    reversed_text = reverse_words(text)
    print(f"'{text}' → '{reversed_text}'")

# ============================================================================
# REVERSE EACH WORD
# ============================================================================

def reverse_each_word(s):
    """
    Reverse each word individually
    
    Args:
        s: Input string
    
    Returns:
        str: String with each word reversed
    
    Example:
        "Hello World" → "olleH dlroW"
    """
    words = s.split()
    reversed_words = [word[::-1] for word in words]
    return " ".join(reversed_words)

# Test
print("\n" + "="*60)
print("REVERSE EACH WORD")
print("="*60)

for text in test_strings:
    reversed_text = reverse_each_word(text)
    print(f"'{text}' → '{reversed_text}'")

# ============================================================================
# REMOVE SPACES
# ============================================================================

def remove_spaces(s):
    """
    Remove all spaces from string
    
    Args:
        s: Input string
    
    Returns:
        str: String without spaces
    """
    return "".join(s.split())

# Alternative methods
def remove_spaces_replace(s):
    """Using replace()"""
    return s.replace(" ", "")

def remove_spaces_filter(s):
    """Using filter()"""
    return "".join(ch for ch in s if ch != " ")

# Test
print("\n" + "="*60)
print("REMOVE SPACES")
print("="*60)

test_strings = [
    "Hello World",
    "  Python  is  awesome  ",
    "NoSpacesHere"
]

for text in test_strings:
    result1 = remove_spaces(text)
    result2 = remove_spaces_replace(text)
    result3 = remove_spaces_filter(text)
    print(f"'{text}'")
    print(f"  Method 1: '{result1}'")
    print(f"  Method 2: '{result2}'")
    print(f"  Method 3: '{result3}'")

# ============================================================================
# TITLE CASE CONVERSION
# ============================================================================

def to_title_case(s):
    """
    Convert to title case (first letter of each word capitalized)
    
    Args:
        s: Input string
    
    Returns:
        str: Title case string
    """
    return s.title()

# Manual implementation
def to_title_case_manual(s):
    """Manual title case conversion"""
    words = s.split()
    title_words = [word.capitalize() for word in words]
    return " ".join(title_words)

# Test
print("\n" + "="*60)
print("TITLE CASE CONVERSION")
print("="*60)

test_strings = [
    "hello world",
    "python programming",
    "THE QUICK BROWN FOX"
]

for text in test_strings:
    result1 = to_title_case(text)
    result2 = to_title_case_manual(text)
    print(f"'{text}'")
    print(f"  Built-in: '{result1}'")
    print(f"  Manual: '{result2}'")

# ============================================================================
# TOGGLE CASE
# ============================================================================

def toggle_case(s):
    """
    Toggle case of each character (upper ↔ lower)
    
    Args:
        s: Input string
    
    Returns:
        str: String with toggled case
    """
    return s.swapcase()

# Manual implementation
def toggle_case_manual(s):
    """Manual toggle"""
    result = []
    for ch in s:
        if ch.isupper():
            result.append(ch.lower())
        elif ch.islower():
            result.append(ch.upper())
        else:
            result.append(ch)
    return "".join(result)

# Test
print("\n" + "="*60)
print("TOGGLE CASE")
print("="*60)

test_strings = [
    "Hello World",
    "PyThOn",
    "ABC123xyz"
]

for text in test_strings:
    result1 = toggle_case(text)
    result2 = toggle_case_manual(text)
    print(f"'{text}'")
    print(f"  Built-in: '{result1}'")
    print(f"  Manual: '{result2}'")

# ============================================================================
# REPLACE SPACES WITH CHARACTER
# ============================================================================

def replace_spaces(s, replacement='_'):
    """
    Replace all spaces with a character
    
    Args:
        s: Input string
        replacement: Character to replace spaces with
    
    Returns:
        str: String with spaces replaced
    """
    return s.replace(' ', replacement)

# Test
print("\n" + "="*60)
print("REPLACE SPACES")
print("="*60)

text = "Hello World Python"
replacements = ['_', '-', '%20']

for rep in replacements:
    result = replace_spaces(text, rep)
    print(f"Replace with '{rep}': '{result}'")

# ============================================================================
# COMPREHENSIVE TRANSFORMATION EXAMPLE
# ============================================================================

def transform_string(s, operations):
    """
    Apply multiple transformations
    
    Args:
        s: Input string
        operations: List of operation names
    
    Returns:
        str: Transformed string
    """
    result = s
    
    for op in operations:
        if op == "remove_duplicates":
            result = remove_duplicates(result)
        elif op == "compress":
            result = compress_string(result)
        elif op == "reverse":
            result = result[::-1]
        elif op == "upper":
            result = result.upper()
        elif op == "lower":
            result = result.lower()
        elif op == "remove_spaces":
            result = remove_spaces(result)
        
        print(f"  After {op}: '{result}'")
    
    return result

# Test
print("\n" + "="*60)
print("MULTI-STEP TRANSFORMATION")
print("="*60)

text = "Hello World"
operations = ["lower", "remove_spaces", "remove_duplicates", "compress"]

print(f"Original: '{text}'")
final = transform_string(text, operations)
print(f"Final: '{final}'")

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================
"""
REMOVE DUPLICATES:
✓ Use set to track seen characters
✓ Preserve first occurrence order
✓ Time: O(n), Space: O(n)

STRING COMPRESSION:
✓ Count consecutive characters
✓ Don't forget last character!
✓ Consider if compression saves space

DECOMPRESSION:
✓ Parse character and count pairs
✓ Handle multi-digit counts
✓ Expand each character × count

WORD MANIPULATION:
✓ split() to get words
✓ join() to reconstruct
✓ [::-1] for reversal

SPACE HANDLING:
✓ replace(' ', '') to remove
✓ split() automatically handles multiple spaces
✓ join(split()) normalizes spacing

CASE TRANSFORMATIONS:
✓ swapcase() for toggle
✓ title() for title case
✓ Manual loops give more control

PATTERN:
✓ String → List → Process → Join back
✓ Most transformations preserve order
✓ Consider in-place vs new string
"""