"""
Hash Maps - Counting Patterns
==============================
Master the most common hash map pattern: frequency counting
"""

from collections import defaultdict, Counter

# ============================================================================
# PATTERN 1: CHARACTER FREQUENCY COUNTING
# ============================================================================
"""
Problem: Count how many times each element appears
This is THE fundamental hash map pattern!
"""

print("="*60)
print("CHARACTER FREQUENCY COUNTING")
print("="*60)

# Method 1: Using if-else (Beginner)
def count_characters_basic(s):
    """
    Count frequency of each character
    
    Args:
        s: Input string
    
    Returns:
        dict: Character frequencies
    
    Time: O(n), Space: O(k) where k = unique characters
    """
    count = {}
    
    for char in s:
        # Check if character already in dictionary
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    
    return count

# Test
result = count_characters_basic("hello")
print(f"\nMethod 1 (if-else): {result}")
# Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# Method 2: Using .get() (Better!)
def count_characters_get(s):
    """
    Using .get() for cleaner code
    
    .get(char, 0) returns 0 if char not in dict
    """
    count = {}
    
    for char in s:
        count[char] = count.get(char, 0) + 1
    
    return count

result = count_characters_get("hello")
print(f"Method 2 (.get()): {result}")

# Method 3: Using defaultdict (Advanced)
def count_characters_defaultdict(s):
    """
    defaultdict automatically initializes missing keys
    No need to check if key exists!
    """
    count = defaultdict(int)  # Default value is 0
    
    for char in s:
        count[char] += 1  # No need to check if exists!
    
    return dict(count)

result = count_characters_defaultdict("hello")
print(f"Method 3 (defaultdict): {result}")

# Method 4: Using Counter (Best!)
def count_characters_counter(s):
    """
    Counter is built specifically for counting!
    One line solution
    """
    return dict(Counter(s))

result = count_characters_counter("hello")
print(f"Method 4 (Counter): {result}")

# ============================================================================
# VISUAL EXPLANATION OF COUNTING PROCESS
# ============================================================================
print("\n" + "="*60)
print("HOW COUNTING WORKS - Step by Step")
print("="*60)

def count_with_visualization(s):
    """Show the counting process step by step"""
    count = {}
    print(f"\nCounting characters in: '{s}'")
    print("-" * 40)
    
    for i, char in enumerate(s):
        # Get current count
        current_count = count.get(char, 0)
        count[char] = current_count + 1
        
        print(f"Step {i+1}: char='{char}', count before: {current_count}, count after: {count[char]}")
        print(f"         Dictionary now: {count}")
    
    return count

result = count_with_visualization("hello")
print(f"\nFinal result: {result}")

# ============================================================================
# PATTERN 2: WORD FREQUENCY COUNTING
# ============================================================================
print("\n" + "="*60)
print("WORD FREQUENCY COUNTING")
print("="*60)

def count_words(text):
    """
    Count how many times each word appears
    
    Args:
        text: String with words
    
    Returns:
        dict: Word frequencies
    
    Time: O(n), Space: O(k)
    
    Example:
        "hello world hello" → {'hello': 2, 'world': 1}
    """
    count = {}
    words = text.split()  # Split by spaces
    
    for word in words:
        count[word] = count.get(word, 0) + 1
    
    return count

# Test
sentence = "apple banana apple orange banana apple"
result = count_words(sentence)
print(f"\nText: '{sentence}'")
print(f"Word count: {result}")
# Output: {'apple': 3, 'banana': 2, 'orange': 1}

# ============================================================================
# PATTERN 3: NUMBER FREQUENCY COUNTING
# ============================================================================
print("\n" + "="*60)
print("NUMBER FREQUENCY COUNTING")
print("="*60)

def count_numbers(nums):
    """
    Count frequency of numbers in a list
    
    Args:
        nums: List of numbers
    
    Returns:
        dict: Number frequencies
    """
    count = {}
    
    for num in nums:
        count[num] = count.get(num, 0) + 1
    
    return count

# Test
numbers = [1, 2, 3, 2, 1, 4, 1, 2]
result = count_numbers(numbers)
print(f"\nNumbers: {numbers}")
print(f"Frequency: {result}")
# Output: {1: 3, 2: 3, 3: 1, 4: 1}

# ============================================================================
# FINDING ELEMENTS BY FREQUENCY
# ============================================================================
print("\n" + "="*60)
print("FINDING ELEMENTS BY FREQUENCY")
print("="*60)

# Find most frequent element
def most_frequent(items):
    """
    Find the most frequently occurring element
    
    Args:
        items: List of items
    
    Returns:
        tuple: (element, frequency)
    """
    count = {}
    
    for item in items:
        count[item] = count.get(item, 0) + 1
    
    # Find max frequency
    max_item = None
    max_count = 0
    
    for item, freq in count.items():
        if freq > max_count:
            max_count = freq
            max_item = item
    
    return max_item, max_count

# Alternative using max()
def most_frequent_pythonic(items):
    """Using max() with key parameter"""
    count = Counter(items)
    most_common = count.most_common(1)[0]  # Returns (element, count)
    return most_common

# Test
numbers = [1, 2, 3, 2, 1, 4, 1, 2, 1]
element, freq = most_frequent(numbers)
print(f"\nNumbers: {numbers}")
print(f"Most frequent: {element} appears {freq} times")

element2, freq2 = most_frequent_pythonic(numbers)
print(f"Verification: {element2} appears {freq2} times")

# Find least frequent element
def least_frequent(items):
    """Find the least frequently occurring element"""
    count = Counter(items)
    least_common = count.most_common()[-1]  # Last one
    return least_common

# Test
element, freq = least_frequent(numbers)
print(f"Least frequent: {element} appears {freq} times")

# ============================================================================
# FILTERING BY FREQUENCY
# ============================================================================
print("\n" + "="*60)
print("FILTERING BY FREQUENCY")
print("="*60)

def elements_appearing_n_times(items, n):
    """
    Find all elements that appear exactly n times
    
    Args:
        items: List of items
        n: Target frequency
    
    Returns:
        list: Elements appearing n times
    """
    count = {}
    
    for item in items:
        count[item] = count.get(item, 0) + 1
    
    result = [item for item, freq in count.items() if freq == n]
    return result

# Test
numbers = [1, 2, 3, 2, 1, 4, 1, 2, 5]
print(f"\nNumbers: {numbers}")
print(f"Appear 1 time: {elements_appearing_n_times(numbers, 1)}")
print(f"Appear 2 times: {elements_appearing_n_times(numbers, 2)}")
print(f"Appear 3 times: {elements_appearing_n_times(numbers, 3)}")

# Elements appearing more than n times
def elements_appearing_more_than_n(items, n):
    """Find elements appearing MORE than n times"""
    count = {}
    
    for item in items:
        count[item] = count.get(item, 0) + 1
    
    return [item for item, freq in count.items() if freq > n]

print(f"\nAppear MORE than 2 times: {elements_appearing_more_than_n(numbers, 2)}")

# ============================================================================
# CASE-INSENSITIVE COUNTING
# ============================================================================
print("\n" + "="*60)
print("CASE-INSENSITIVE COUNTING")
print("="*60)

def count_words_case_insensitive(text):
    """
    Count words ignoring case
    
    "Hello hello HELLO" → {'hello': 3}
    """
    count = {}
    words = text.lower().split()  # Convert to lowercase first
    
    for word in words:
        count[word] = count.get(word, 0) + 1
    
    return count

# Test
text = "Hello World hello WORLD Hello"
result = count_words_case_insensitive(text)
print(f"\nText: '{text}'")
print(f"Case-insensitive count: {result}")
# Output: {'hello': 3, 'world': 2}

# ============================================================================
# COUNTING WITH FILTERING
# ============================================================================
print("\n" + "="*60)
print("COUNTING WITH FILTERING")
print("="*60)

def count_vowels_consonants(text):
    """
    Count vowels and consonants separately
    
    Returns:
        tuple: (vowel_count, consonant_count)
    """
    text = text.lower()
    vowels = set('aeiou')
    
    vowel_count = 0
    consonant_count = 0
    
    for char in text:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1
    
    return vowel_count, consonant_count

# Test
text = "Hello World"
vowels, consonants = count_vowels_consonants(text)
print(f"\nText: '{text}'")
print(f"Vowels: {vowels}, Consonants: {consonants}")

# Count only alphabetic characters
def count_only_letters(text):
    """Count only alphabetic characters, ignore others"""
    count = {}
    
    for char in text.lower():
        if char.isalpha():
            count[char] = count.get(char, 0) + 1
    
    return count

# Test
text = "Hello, World! 123"
result = count_only_letters(text)
print(f"\nText: '{text}'")
print(f"Letter count: {result}")

# ============================================================================
# PRACTICAL APPLICATIONS
# ============================================================================
print("\n" + "="*60)
print("PRACTICAL APPLICATIONS")
print("="*60)

# Application 1: Find unique elements (count = 1)
def find_unique_elements(items):
    """Find elements that appear only once"""
    count = {}
    
    for item in items:
        count[item] = count.get(item, 0) + 1
    
    return [item for item, freq in count.items() if freq == 1]

numbers = [1, 2, 3, 2, 4, 3, 5]
print(f"\nNumbers: {numbers}")
print(f"Unique elements: {find_unique_elements(numbers)}")

# Application 2: Check if all elements are unique
def all_unique(items):
    """Check if all elements appear exactly once"""
    count = {}
    
    for item in items:
        if item in count:
            return False  # Found duplicate!
        count[item] = 1
    
    return True

print(f"\n[1,2,3,4] all unique? {all_unique([1,2,3,4])}")
print(f"[1,2,3,2] all unique? {all_unique([1,2,3,2])}")

# Application 3: Top K frequent elements
def top_k_frequent(items, k):
    """Find k most frequent elements"""
    count = Counter(items)
    return [item for item, freq in count.most_common(k)]

numbers = [1, 1, 1, 2, 2, 3, 4, 4, 4, 4]
print(f"\nNumbers: {numbers}")
print(f"Top 2 frequent: {top_k_frequent(numbers, 2)}")
print(f"Top 3 frequent: {top_k_frequent(numbers, 3)}")

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================
"""
COUNTING PATTERN:
✓ THE most common hash map use case
✓ Foundation for many interview problems
✓ Time: O(n), Space: O(k)

FOUR METHODS:
1. if-else: Beginner-friendly, verbose
2. .get(): Cleaner, preferred for interviews
3. defaultdict: Advanced, automatic initialization
4. Counter: Best for pure counting tasks

COMMON OPERATIONS:
✓ Count all: count[item] = count.get(item, 0) + 1
✓ Find most frequent: max(count, key=count.get)
✓ Filter by frequency: [k for k, v in count.items() if v > n]
✓ Get unique: [k for k, v in count.items() if v == 1]

VARIATIONS:
✓ Case-insensitive: text.lower() first
✓ With filtering: if item.isalpha()
✓ Top K: Counter.most_common(k)

USE CASES:
✓ Character/word frequency
✓ Find duplicates
✓ Find unique elements
✓ Most/least common elements
✓ Anagram detection
"""

print("\n" + "="*60)
print("✓ Counting patterns mastered!")
print("="*60)