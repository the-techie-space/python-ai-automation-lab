"""
SET AND TUPLE BASICS - From Fundamentals to Advanced
=====================================================

This file covers:
1. Set fundamentals and operations
2. Tuple fundamentals and operations
3. Practical examples
4. Interview-style problems
5. Best practices and pitfalls

Author: DSA Learning
"""

# ============================================================================
# PART 1: SET FUNDAMENTALS
# ============================================================================

print("=" * 70)
print("PART 1: SET FUNDAMENTALS")
print("=" * 70)

# -----------------------------------------------------------------------------
# 1.1 Creating Sets
# -----------------------------------------------------------------------------

# Empty set (IMPORTANT: {} creates dict, not set!)
empty_set = set()
print(f"Empty set: {empty_set}")

# Set with elements
numbers = {1, 2, 3, 4, 5}
print(f"Number set: {numbers}")

# Set from list (automatically removes duplicates)
list_with_dupes = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
unique_numbers = set(list_with_dupes)
print(f"Unique from list: {unique_numbers}")  # {1, 2, 3, 4}

# Set from string (unique characters)
word = "hello"
unique_chars = set(word)
print(f"Unique chars in '{word}': {unique_chars}")  # {'h', 'e', 'l', 'o'}

# Set with mixed types
mixed_set = {1, "hello", 3.14, True}
print(f"Mixed set: {mixed_set}")

# -----------------------------------------------------------------------------
# 1.2 Basic Set Operations
# -----------------------------------------------------------------------------

my_set = {1, 2, 3, 4, 5}

# Add element - O(1)
my_set.add(6)
print(f"After add(6): {my_set}")

# Add duplicate (no effect - sets only store unique values)
my_set.add(3)
print(f"After add(3) again: {my_set}")  # Still same

# Remove element - O(1) - raises KeyError if not exists
my_set.remove(2)
print(f"After remove(2): {my_set}")

# Discard element - O(1) - no error if not exists
my_set.discard(100)  # Element doesn't exist, but no error
print(f"After discard(100): {my_set}")

# Pop random element - O(1)
removed = my_set.pop()
print(f"Popped element: {removed}")
print(f"Set after pop: {my_set}")

# Check membership - O(1) - THIS IS THE SUPERPOWER OF SETS!
if 3 in my_set:
    print("3 is in the set")

if 100 not in my_set:
    print("100 is NOT in the set")

# Length
print(f"Set length: {len(my_set)}")

# Clear all elements
test_set = {1, 2, 3}
test_set.clear()
print(f"After clear: {test_set}")  # set()

# -----------------------------------------------------------------------------
# 1.3 Set Mathematical Operations
# -----------------------------------------------------------------------------

set_a = {1, 2, 3, 4, 5}
set_b = {4, 5, 6, 7, 8}

# Union - all elements from both sets
union_result = set_a | set_b  # or set_a.union(set_b)
print(f"Union {set_a} | {set_b} = {union_result}")

# Intersection - common elements
intersection_result = set_a & set_b  # or set_a.intersection(set_b)
print(f"Intersection {set_a} & {set_b} = {intersection_result}")

# Difference - elements in set_a but not in set_b
difference_result = set_a - set_b  # or set_a.difference(set_b)
print(f"Difference {set_a} - {set_b} = {difference_result}")

# Symmetric difference - elements in either but not both
sym_diff = set_a ^ set_b  # or set_a.symmetric_difference(set_b)
print(f"Symmetric difference {set_a} ^ {set_b} = {sym_diff}")

# Subset check
subset = {2, 3}
print(f"Is {subset} subset of {set_a}? {subset.issubset(set_a)}")

# Superset check
print(f"Is {set_a} superset of {subset}? {set_a.issuperset(subset)}")

# Disjoint check (no common elements)
set_c = {10, 11, 12}
print(f"Are {set_a} and {set_c} disjoint? {set_a.isdisjoint(set_c)}")

# -----------------------------------------------------------------------------
# 1.4 Set vs List Performance Comparison
# -----------------------------------------------------------------------------

import time

# Create large list and set
large_list = list(range(10000))
large_set = set(range(10000))

# Test membership in list - O(n)
start = time.time()
9999 in large_list
list_time = time.time() - start

# Test membership in set - O(1)
start = time.time()
9999 in large_set
set_time = time.time() - start

print(f"\nPerformance comparison:")
print(f"List membership check: {list_time:.6f}s")
print(f"Set membership check: {set_time:.6f}s")
print(f"Set is ~{list_time/set_time:.0f}x faster!")

# -----------------------------------------------------------------------------
# 1.5 Common Set Patterns
# -----------------------------------------------------------------------------

# Pattern 1: Remove duplicates from list
def remove_duplicates(arr):
    """Convert to set and back to list"""
    return list(set(arr))

numbers_with_dupes = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
print(f"\nRemove duplicates: {remove_duplicates(numbers_with_dupes)}")

# Pattern 2: Find common elements
def find_common(list1, list2):
    """Intersection of two lists"""
    return list(set(list1) & set(list2))

list1 = [1, 2, 3, 4, 5]
list2 = [4, 5, 6, 7, 8]
print(f"Common elements: {find_common(list1, list2)}")

# Pattern 3: Find unique elements (symmetric difference)
def find_unique_elements(list1, list2):
    """Elements in either list but not both"""
    return list(set(list1) ^ set(list2))

print(f"Unique elements: {find_unique_elements(list1, list2)}")

# Pattern 4: Check if arrays are equal (regardless of order)
def arrays_equal(arr1, arr2):
    """Check if two arrays have same elements"""
    return set(arr1) == set(arr2)

arr1 = [1, 2, 3, 4, 5]
arr2 = [5, 4, 3, 2, 1]
print(f"Are {arr1} and {arr2} equal? {arrays_equal(arr1, arr2)}")


# ============================================================================
# PART 2: TUPLE FUNDAMENTALS
# ============================================================================

print("\n" + "=" * 70)
print("PART 2: TUPLE FUNDAMENTALS")
print("=" * 70)

# -----------------------------------------------------------------------------
# 2.1 Creating Tuples
# -----------------------------------------------------------------------------

# Empty tuple
empty_tuple = ()
print(f"Empty tuple: {empty_tuple}")

# Single element tuple (IMPORTANT: Note the comma!)
single_wrong = (1)  # This is just int 1, not a tuple!
single_correct = (1,)  # This is a tuple with one element
print(f"Without comma: {single_wrong}, type: {type(single_wrong)}")
print(f"With comma: {single_correct}, type: {type(single_correct)}")

# Multiple elements
coordinates = (10, 20)
rgb_color = (255, 0, 0)  # Red
person = ("Alice", 25, "Engineer")

# Without parentheses (tuple packing)
point = 10, 20
print(f"Tuple packing: {point}, type: {type(point)}")

# From list
my_list = [1, 2, 3, 4, 5]
my_tuple = tuple(my_list)
print(f"Tuple from list: {my_tuple}")

# From string
char_tuple = tuple("hello")
print(f"Tuple from string: {char_tuple}")

# -----------------------------------------------------------------------------
# 2.2 Basic Tuple Operations
# -----------------------------------------------------------------------------

my_tuple = (10, 20, 30, 40, 50)

# Access by index - O(1)
print(f"First element: {my_tuple[0]}")
print(f"Last element: {my_tuple[-1]}")

# Slicing - O(k) where k is slice size
print(f"Slice [1:3]: {my_tuple[1:3]}")
print(f"Every 2nd element: {my_tuple[::2]}")

# Length
print(f"Length: {len(my_tuple)}")

# Count occurrences
tuple_with_dupes = (1, 2, 2, 3, 3, 3, 4)
print(f"Count of 3: {tuple_with_dupes.count(3)}")

# Find index of element
print(f"Index of 30: {my_tuple.index(30)}")

# Concatenation (creates NEW tuple)
tuple1 = (1, 2, 3)
tuple2 = (4, 5, 6)
combined = tuple1 + tuple2
print(f"Concatenation: {combined}")

# Repetition
repeated = (1, 2) * 3
print(f"Repetition: {repeated}")

# Membership test
print(f"Is 30 in tuple? {30 in my_tuple}")

# -----------------------------------------------------------------------------
# 2.3 Tuple Immutability
# -----------------------------------------------------------------------------

immutable_tuple = (1, 2, 3, 4, 5)

# CANNOT modify tuple
# immutable_tuple[0] = 10  # ❌ TypeError: 'tuple' object does not support item assignment
# immutable_tuple.append(6)  # ❌ AttributeError: 'tuple' object has no attribute 'append'
# del immutable_tuple[0]  # ❌ TypeError: 'tuple' object doesn't support item deletion

# But you can create a new tuple
new_tuple = immutable_tuple + (6,)
print(f"New tuple with added element: {new_tuple}")

# HOWEVER: If tuple contains mutable objects, those can be modified!
tuple_with_list = (1, 2, [3, 4, 5])
tuple_with_list[2].append(6)  # This works! Modifying the list inside
print(f"Tuple with modified list: {tuple_with_list}")

# -----------------------------------------------------------------------------
# 2.4 Tuple Unpacking
# -----------------------------------------------------------------------------

# Basic unpacking
x, y = (10, 20)
print(f"Unpacked: x={x}, y={y}")

# Unpacking without parentheses
a, b, c = 1, 2, 3
print(f"Unpacked: a={a}, b={b}, c={c}")

# Swap variables using tuple unpacking
x, y = 5, 10
print(f"Before swap: x={x}, y={y}")
x, y = y, x  # Elegant swap!
print(f"After swap: x={x}, y={y}")

# Extended unpacking (Python 3+)
first, *middle, last = (1, 2, 3, 4, 5, 6, 7)
print(f"First: {first}, Middle: {middle}, Last: {last}")

# Ignore values with underscore
name, _, age = ("Alice", "Ignored", 25)
print(f"Name: {name}, Age: {age}")

# Unpacking in loops
points = [(1, 2), (3, 4), (5, 6)]
for x, y in points:
    print(f"Point: ({x}, {y})")

# -----------------------------------------------------------------------------
# 2.5 Tuples as Function Return Values
# -----------------------------------------------------------------------------

def get_statistics(numbers):
    """Return multiple values as tuple"""
    return min(numbers), max(numbers), sum(numbers), len(numbers)

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
minimum, maximum, total, count = get_statistics(nums)
print(f"\nStatistics: min={minimum}, max={maximum}, sum={total}, count={count}")

def divide_with_remainder(dividend, divisor):
    """Return quotient and remainder"""
    return dividend // divisor, dividend % divisor

quotient, remainder = divide_with_remainder(17, 5)
print(f"17 ÷ 5 = {quotient} remainder {remainder}")

# -----------------------------------------------------------------------------
# 2.6 Tuples as Dictionary Keys
# -----------------------------------------------------------------------------

# Tuples are HASHABLE (immutable), so they can be dict keys
# Lists are NOT hashable, so they CANNOT be dict keys

# Graph represented as dict with tuple keys
graph_edges = {
    (0, 1): 5,  # Edge from node 0 to 1 with weight 5
    (1, 2): 3,
    (2, 3): 7,
    (0, 3): 2
}
print(f"\nGraph edges: {graph_edges}")
print(f"Weight of edge (0,1): {graph_edges[(0, 1)]}")

# Coordinate system
grid = {}
grid[(0, 0)] = "Start"
grid[(5, 5)] = "End"
grid[(2, 3)] = "Obstacle"
print(f"Grid: {grid}")

# Memoization cache for dynamic programming
fibonacci_cache = {}
def fibonacci(n):
    if n in fibonacci_cache:
        return fibonacci_cache[n]
    if n <= 1:
        return n
    result = fibonacci(n-1) + fibonacci(n-2)
    fibonacci_cache[n] = result
    return result

print(f"Fibonacci(10) = {fibonacci(10)}")
print(f"Cache: {fibonacci_cache}")

# -----------------------------------------------------------------------------
# 2.7 Named Tuples (Advanced)
# -----------------------------------------------------------------------------

from collections import namedtuple

# Create a named tuple type
Point = namedtuple('Point', ['x', 'y'])
person_type = namedtuple('Person', ['name', 'age', 'job'])

# Create instances
p1 = Point(10, 20)
p2 = Point(x=30, y=40)

print(f"\nNamed tuple point: {p1}")
print(f"Access by name: x={p1.x}, y={p1.y}")
print(f"Access by index: x={p1[0]}, y={p1[1]}")

# Named tuple for person
alice = person_type("Alice", 25, "Engineer")
print(f"Person: name={alice.name}, age={alice.age}, job={alice.job}")

# Named tuples are still immutable
# alice.age = 26  # ❌ AttributeError


# ============================================================================
# PART 3: PRACTICAL EXAMPLES
# ============================================================================

print("\n" + "=" * 70)
print("PART 3: PRACTICAL EXAMPLES")
print("=" * 70)

# -----------------------------------------------------------------------------
# 3.1 Using Sets for Deduplication
# -----------------------------------------------------------------------------

def get_unique_words(text):
    """Extract unique words from text"""
    words = text.lower().split()
    return set(words)

text = "hello world hello python world programming python"
unique = get_unique_words(text)
print(f"Unique words: {unique}")

# -----------------------------------------------------------------------------
# 3.2 Fast Membership Testing with Sets
# -----------------------------------------------------------------------------

def contains_duplicate(nums):
    """Check if array has duplicates - O(n) time"""
    seen = set()
    for num in nums:
        if num in seen:  # O(1) lookup!
            return True
        seen.add(num)
    return False

print(f"\n[1,2,3,4] has duplicate? {contains_duplicate([1,2,3,4])}")
print(f"[1,2,3,1] has duplicate? {contains_duplicate([1,2,3,1])}")

# -----------------------------------------------------------------------------
# 3.3 Finding Intersection and Union
# -----------------------------------------------------------------------------

def common_friends(person1_friends, person2_friends):
    """Find mutual friends"""
    return set(person1_friends) & set(person2_friends)

def all_friends(person1_friends, person2_friends):
    """Find all unique friends"""
    return set(person1_friends) | set(person2_friends)

alice_friends = ["Bob", "Charlie", "David"]
bob_friends = ["Alice", "Charlie", "Eve"]

print(f"\nMutual friends: {common_friends(alice_friends, bob_friends)}")
print(f"All friends: {all_friends(alice_friends, bob_friends)}")

# -----------------------------------------------------------------------------
# 3.4 Tuples for Coordinates and Points
# -----------------------------------------------------------------------------

def manhattan_distance(point1, point2):
    """Calculate Manhattan distance between two points"""
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 - x2) + abs(y1 - y2)

p1 = (0, 0)
p2 = (3, 4)
print(f"\nManhattan distance between {p1} and {p2}: {manhattan_distance(p1, p2)}")

# -----------------------------------------------------------------------------
# 3.5 Tuples for Immutable Configuration
# -----------------------------------------------------------------------------

# Configuration that shouldn't change
DATABASE_CONFIG = (
    "localhost",  # host
    5432,         # port
    "mydb",       # database name
    "user"        # username
)

host, port, db_name, user = DATABASE_CONFIG
print(f"\nDatabase config: {host}:{port}/{db_name} as {user}")


# ============================================================================
# PART 4: INTERVIEW-STYLE PROBLEMS
# ============================================================================

print("\n" + "=" * 70)
print("PART 4: INTERVIEW-STYLE PROBLEMS")
print("=" * 70)

# -----------------------------------------------------------------------------
# Problem 1: Two Sum - Using Set for O(n) solution
# -----------------------------------------------------------------------------

def two_sum_set(nums, target):
    """
    Find two numbers that add up to target
    Time: O(n), Space: O(n)
    """
    seen = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            return True
        seen.add(num)
    return False

print(f"\nTwo Sum exists in [2,7,11,15] for target 9? {two_sum_set([2,7,11,15], 9)}")

# -----------------------------------------------------------------------------
# Problem 2: Longest Consecutive Sequence
# -----------------------------------------------------------------------------

def longest_consecutive(nums):
    """
    Find length of longest consecutive sequence
    Time: O(n), Space: O(n)
    
    Example: [100, 4, 200, 1, 3, 2] → [1,2,3,4] → length 4
    """
    if not nums:
        return 0
    
    num_set = set(nums)
    max_length = 0
    
    for num in num_set:
        # Only start counting if it's the beginning of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            
            # Count consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            
            max_length = max(max_length, current_length)
    
    return max_length

nums = [100, 4, 200, 1, 3, 2]
print(f"Longest consecutive in {nums}: {longest_consecutive(nums)}")

# -----------------------------------------------------------------------------
# Problem 3: Valid Anagram - Using Sets and Tuples
# -----------------------------------------------------------------------------

def is_anagram(s1, s2):
    """
    Check if two strings are anagrams
    Method 1: Compare sorted tuples
    """
    return tuple(sorted(s1)) == tuple(sorted(s2))

def is_anagram_set(s1, s2):
    """
    Method 2: Compare character sets and counts
    """
    if len(s1) != len(s2):
        return False
    if set(s1) != set(s2):
        return False
    # Check counts
    from collections import Counter
    return Counter(s1) == Counter(s2)

print(f"\n'listen' and 'silent' are anagrams? {is_anagram('listen', 'silent')}")
print(f"'hello' and 'world' are anagrams? {is_anagram('hello', 'world')}")

# -----------------------------------------------------------------------------
# Problem 4: Intersection of Multiple Arrays
# -----------------------------------------------------------------------------

def intersect_multiple_arrays(arrays):
    """
    Find common elements across all arrays
    """
    if not arrays:
        return []
    
    # Start with first array as set
    result = set(arrays[0])
    
    # Intersect with each subsequent array
    for arr in arrays[1:]:
        result &= set(arr)
    
    return list(result)

arrays = [[1, 2, 3, 4], [2, 3, 4, 5], [3, 4, 5, 6]]
print(f"\nIntersection of {arrays}: {intersect_multiple_arrays(arrays)}")

# -----------------------------------------------------------------------------
# Problem 5: Group Anagrams Using Tuple Keys
# -----------------------------------------------------------------------------

def group_anagrams(words):
    """
    Group words that are anagrams of each other
    Time: O(n * k log k) where k is max word length
    """
    from collections import defaultdict
    
    groups = defaultdict(list)
    
    for word in words:
        # Use sorted tuple as key
        key = tuple(sorted(word))
        groups[key].append(word)
    
    return list(groups.values())

words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(f"\nGrouped anagrams: {group_anagrams(words)}")


# ============================================================================
# PART 5: BEST PRACTICES AND COMMON PITFALLS
# ============================================================================

print("\n" + "=" * 70)
print("PART 5: BEST PRACTICES AND COMMON PITFALLS")
print("=" * 70)

# -----------------------------------------------------------------------------
# Pitfall 1: Empty set vs empty dict
# -----------------------------------------------------------------------------

wrong_empty_set = {}  # This is a DICT, not a set!
correct_empty_set = set()

print(f"Type of {{}}: {type(wrong_empty_set)}")
print(f"Type of set(): {type(correct_empty_set)}")

# -----------------------------------------------------------------------------
# Pitfall 2: Single element tuple
# -----------------------------------------------------------------------------

not_a_tuple = (1)  # Just integer 1
is_a_tuple = (1,)  # Tuple with one element

print(f"\nType of (1): {type(not_a_tuple)}")
print(f"Type of (1,): {type(is_a_tuple)}")

# -----------------------------------------------------------------------------
# Pitfall 3: Modifying set while iterating
# -----------------------------------------------------------------------------

# WRONG: Don't modify set while iterating
# my_set = {1, 2, 3, 4, 5}
# for item in my_set:
#     if item % 2 == 0:
#         my_set.remove(item)  # ❌ RuntimeError!

# CORRECT: Create new set or use list comprehension
my_set = {1, 2, 3, 4, 5}
my_set = {item for item in my_set if item % 2 != 0}
print(f"\nFiltered set: {my_set}")

# -----------------------------------------------------------------------------
# Best Practice 1: Use set for membership testing
# -----------------------------------------------------------------------------

# If you need to check "if x in container" repeatedly, use set!
allowed_users = {"alice", "bob", "charlie"}  # Fast O(1) lookup
# Instead of: allowed_users = ["alice", "bob", "charlie"]  # Slow O(n) lookup

print(f"Is 'alice' allowed? {'alice' in allowed_users}")

# -----------------------------------------------------------------------------
# Best Practice 2: Use tuple for fixed data
# -----------------------------------------------------------------------------

# Good: Tuple for unchanging data
DAYS_OF_WEEK = ("Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun")
RGB_RED = (255, 0, 0)

# Bad: List for unchanging data (can be accidentally modified)
# DAYS_OF_WEEK = ["Mon", "Tue", ...]  # Can be changed by mistake

# -----------------------------------------------------------------------------
# Best Practice 3: Frozenset for immutable sets
# -----------------------------------------------------------------------------

# Frozenset: immutable version of set (can be used as dict key)
immutable_set = frozenset([1, 2, 3, 4, 5])
print(f"\nFrozenset: {immutable_set}")

# Can be used as dict key or set element
dict_with_set_key = {immutable_set: "value"}
set_of_sets = {frozenset([1, 2]), frozenset([3, 4])}
print(f"Set of sets: {set_of_sets}")

print("\n" + "=" * 70)
print("END OF BASICS - Check problems.py for more practice!")
print("=" * 70)