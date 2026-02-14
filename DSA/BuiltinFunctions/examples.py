"""
PYTHON BUILT-IN FUNCTIONS - COMPREHENSIVE EXAMPLES
===================================================

This file demonstrates all major built-in functions that work across
different Python data types (strings, lists, tuples, sets, dicts).

Each function includes:
- Basic examples
- Advanced use cases
- Performance notes
- Interview patterns

Author: DSA Learning
Run this file to see all outputs!
"""

print("=" * 80)
print("PYTHON BUILT-IN FUNCTIONS - CROSS DATA TYPE REFERENCE")
print("=" * 80)

# ============================================================================
# PART 1: BASIC FUNCTIONS (len, count, index, in, sorted, min/max, sum)
# ============================================================================

print("\n" + "=" * 80)
print("PART 1: BASIC FUNCTIONS")
print("=" * 80)

# ----------------------------------------------------------------------------
# 1.1 len() - Works on ALL containers
# ----------------------------------------------------------------------------

print("\n--- len() ---")
print(f"len('python') = {len('python')}")              # 6
print(f"len([1, 2, 3]) = {len([1, 2, 3])}")            # 3
print(f"len((1, 2)) = {len((1, 2))}")                  # 2
print(f"len({{1, 2, 3}}) = {len({1, 2, 3})}")          # 3
print(f"len({{'a': 1}}) = {len({'a': 1})}")            # 1

# ----------------------------------------------------------------------------
# 1.2 count() - String, List, Tuple ONLY
# ----------------------------------------------------------------------------

print("\n--- count() ---")
print(f"'banana'.count('a') = {'banana'.count('a')}")              # 3
print(f"'banana'.count('na') = {'banana'.count('na')}")            # 2
print(f"[1,2,3,2,2].count(2) = {[1, 2, 3, 2, 2].count(2)}")       # 3
print(f"(1,1,2).count(1) = {(1, 1, 2).count(1)}")                 # 2
# print({1, 2, 3}.count(1))  # ❌ AttributeError

# ----------------------------------------------------------------------------
# 1.3 index() - String, List, Tuple ONLY
# ----------------------------------------------------------------------------

print("\n--- index() ---")
print(f"'python'.index('t') = {'python'.index('t')}")              # 2
print(f"[10,20,30].index(20) = {[10, 20, 30].index(20)}")         # 1
print(f"(5,6,7).index(7) = {(5, 6, 7).index(7)}")                 # 2

# Error handling
try:
    result = [1, 2, 3].index(5)
except ValueError as e:
    print(f"Error: {e}")  # 5 is not in list

# ----------------------------------------------------------------------------
# 1.4 in / not in - ALL iterables
# ----------------------------------------------------------------------------

print("\n--- in / not in ---")
print(f"'a' in 'cat' = {'a' in 'cat'}")                           # True
print(f"2 in [1,2,3] = {2 in [1, 2, 3]}")                         # True
print(f"1 in (1,2) = {1 in (1, 2)}")                              # True
print(f"1 in {{1,2}} = {1 in {1, 2}}")                            # True
print(f"'a' in {{'a':1}} = {'a' in {'a': 1}}")                    # True (checks keys!)

# Performance comparison
import time
large_list = list(range(10000))
large_set = set(range(10000))

start = time.time()
9999 in large_list  # O(n)
list_time = time.time() - start

start = time.time()
9999 in large_set   # O(1)
set_time = time.time() - start

print(f"\nPerformance: List membership = {list_time:.6f}s")
print(f"Performance: Set membership = {set_time:.6f}s")
print(f"Set is ~{list_time/set_time:.0f}x faster!")

# ----------------------------------------------------------------------------
# 1.5 sorted() - ALL iterables
# ----------------------------------------------------------------------------

print("\n--- sorted() ---")
print(f"sorted('cba') = {sorted('cba')}")                         # ['a', 'b', 'c']
print(f"sorted([3,1,2]) = {sorted([3, 1, 2])}")                   # [1, 2, 3]
print(f"sorted((3,2,1)) = {sorted((3, 2, 1))}")                   # [1, 2, 3]
print(f"sorted({{3,1,2}}) = {sorted({3, 1, 2})}")                 # [1, 2, 3]
print(f"sorted({{'b':1,'a':2}}) = {sorted({'b': 1, 'a': 2})}")    # ['a', 'b']

# Custom sorting
print(f"\nsorted([3,1,2], reverse=True) = {sorted([3, 1, 2], reverse=True)}")
words = ["abc", "a", "ab"]
print(f"sorted by length: {sorted(words, key=len)}")              # ['a', 'ab', 'abc']

students = [("Alice", 95), ("Bob", 87), ("Charlie", 92)]
print(f"sorted by score: {sorted(students, key=lambda x: x[1])}")

# ----------------------------------------------------------------------------
# 1.6 min() / max()
# ----------------------------------------------------------------------------

print("\n--- min() / max() ---")
print(f"min('python') = {min('python')}")                         # 'h'
print(f"max([1,5,2]) = {max([1, 5, 2])}")                         # 5
print(f"min({{3,1,2}}) = {min({3, 1, 2})}")                       # 1

# Custom key
words = ["apple", "a", "at"]
print(f"min by length: {min(words, key=len)}")                    # 'a'
print(f"max by length: {max(words, key=len)}")                    # 'apple'

# With default (avoid errors)
print(f"max([], default=0) = {max([], default=0)}")               # 0

# ----------------------------------------------------------------------------
# 1.7 sum() - Numeric iterables only
# ----------------------------------------------------------------------------

print("\n--- sum() ---")
print(f"sum([1,2,3]) = {sum([1, 2, 3])}")                         # 6
print(f"sum((4,5)) = {sum((4, 5))}")                              # 9
print(f"sum({{1,2,3}}) = {sum({1, 2, 3})}")                       # 6
print(f"sum([1,2,3], 10) = {sum([1, 2, 3], 10)}")                 # 16 (start value)

# ----------------------------------------------------------------------------
# 1.8 any() / all()
# ----------------------------------------------------------------------------

print("\n--- any() / all() ---")
print(f"any([0,0,1]) = {any([0, 0, 1])}")                         # True
print(f"any([False,False]) = {any([False, False])}")              # False
print(f"all([1,2,3]) = {all([1, 2, 3])}")                         # True
print(f"all([1,0,3]) = {all([1, 0, 3])}")                         # False

# With generator (efficient!)
print(f"any(x>100 for x in range(1000)) = {any(x > 100 for x in range(1000))}")
print(f"all(x<10 for x in range(5)) = {all(x < 10 for x in range(5))}")


# ============================================================================
# PART 2: ITERATION FUNCTIONS (enumerate, zip, map, filter, reversed)
# ============================================================================

print("\n" + "=" * 80)
print("PART 2: ITERATION FUNCTIONS")
print("=" * 80)

# ----------------------------------------------------------------------------
# 2.1 enumerate() - Get index + value
# ----------------------------------------------------------------------------

print("\n--- enumerate() ---")

# Basic usage
print("Enumerate string:")
for i, char in enumerate("abc"):
    print(f"  Index {i}: {char}")

# Works with all types
print(f"\nlist(enumerate([10,20,30])) = {list(enumerate([10, 20, 30]))}")

# Custom start index
print(f"enumerate with start=1: {list(enumerate(['a', 'b'], start=1))}")

# Interview pattern: Find index of max element
arr = [3, 1, 4, 1, 5]
max_idx = max(enumerate(arr), key=lambda x: x[1])[0]
print(f"\nIndex of max in {arr}: {max_idx}")

# ----------------------------------------------------------------------------
# 2.2 zip() - Combine iterables
# ----------------------------------------------------------------------------

print("\n--- zip() ---")

names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
print(f"zip names & ages: {list(zip(names, ages))}")

# Multiple iterables
print(f"zip 3 lists: {list(zip([1, 2], ['a', 'b'], [True, False]))}")

# Unequal lengths (stops at shortest)
print(f"unequal: {list(zip([1, 2, 3], ['a', 'b']))}")

# Unzip using zip(*)
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
numbers, letters = zip(*pairs)
print(f"unzip: numbers={numbers}, letters={letters}")

# Create dictionary
keys = ['a', 'b', 'c']
values = [1, 2, 3]
print(f"dict from zip: {dict(zip(keys, values))}")

# Parallel iteration
print("\nParallel iteration:")
for name, age in zip(names, ages):
    print(f"  {name} is {age} years old")

# ----------------------------------------------------------------------------
# 2.3 map() - Transform all elements
# ----------------------------------------------------------------------------

print("\n--- map() ---")

# Basic usage
print(f"uppercase: {list(map(str.upper, ['a', 'b', 'c']))}")
print(f"double: {list(map(lambda x: x * 2, [1, 2, 3]))}")

# Multiple iterables
print(f"add pairs: {list(map(lambda x, y: x + y, [1, 2, 3], [10, 20, 30]))}")

# Type conversion
print(f"str to int: {list(map(int, ['1', '2', '3']))}")

# Get lengths
print(f"lengths: {list(map(len, ['a', 'ab', 'abc']))}")

# Square all numbers
nums = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, nums))
print(f"squared: {squared}")

# ----------------------------------------------------------------------------
# 2.4 filter() - Keep matching elements
# ----------------------------------------------------------------------------

print("\n--- filter() ---")

# Basic usage
print(f"filter >2: {list(filter(lambda x: x > 2, [1, 2, 3, 4]))}")

# Even numbers
print(f"even numbers: {list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))}")

# Filter truthy values
print(f"truthy: {list(filter(None, [0, 1, False, True, '', 'hello']))}")

# String filtering
print(f"only letters: {list(filter(str.isalpha, 'a1b2c3'))}")

# Positive numbers only
nums = [-3, -1, 0, 1, 2, 5]
positive = list(filter(lambda x: x > 0, nums))
print(f"positive from {nums}: {positive}")

# ----------------------------------------------------------------------------
# 2.5 reversed() - Reverse iteration
# ----------------------------------------------------------------------------

print("\n--- reversed() ---")

print(f"reverse string: {list(reversed('hello'))}")
print(f"reverse list: {list(reversed([1, 2, 3]))}")
print(f"reverse tuple: {list(reversed((1, 2, 3)))}")

# For lists, slicing is simpler
my_list = [1, 2, 3, 4, 5]
print(f"list[::-1] = {my_list[::-1]}")


# ============================================================================
# PART 3: TYPE CONVERSION
# ============================================================================

print("\n" + "=" * 80)
print("PART 3: TYPE CONVERSION")
print("=" * 80)

# ----------------------------------------------------------------------------
# 3.1 Convert to String
# ----------------------------------------------------------------------------

print("\n--- str() ---")
print(f"str([1,2,3]) = {str([1, 2, 3])}")
print(f"str({{1,2}}) = {str({1, 2})}")
print(f"str((1,2)) = {str((1, 2))}")

# ----------------------------------------------------------------------------
# 3.2 Convert to List
# ----------------------------------------------------------------------------

print("\n--- list() ---")
print(f"list('abc') = {list('abc')}")
print(f"list({{1,2,3}}) = {list({1, 2, 3})}")
print(f"list((1,2)) = {list((1, 2))}")
print(f"list({{'a':1}}) = {list({'a': 1})}")  # Keys only!

# ----------------------------------------------------------------------------
# 3.3 Convert to Tuple
# ----------------------------------------------------------------------------

print("\n--- tuple() ---")
print(f"tuple([1,2,3]) = {tuple([1, 2, 3])}")
print(f"tuple('abc') = {tuple('abc')}")
print(f"tuple({{1,2}}) = {tuple({1, 2})}")

# ----------------------------------------------------------------------------
# 3.4 Convert to Set (removes duplicates!)
# ----------------------------------------------------------------------------

print("\n--- set() ---")
print(f"set([1,2,2,3]) = {set([1, 2, 2, 3])}")
print(f"set('hello') = {set('hello')}")
print(f"set((1,2,2)) = {set((1, 2, 2))}")

# Remove duplicates from list
duplicates = [1, 2, 2, 3, 3, 3, 4]
unique = list(set(duplicates))
print(f"remove duplicates: {duplicates} → {unique}")

# ----------------------------------------------------------------------------
# 3.5 Convert to Dict
# ----------------------------------------------------------------------------

print("\n--- dict() ---")
print(f"dict from pairs: {dict([('a', 1), ('b', 2)])}")
print(f"dict from zip: {dict(zip(['a', 'b'], [1, 2]))}")

# ----------------------------------------------------------------------------
# 3.6 Convert to Bool
# ----------------------------------------------------------------------------

print("\n--- bool() ---")
print(f"bool([]) = {bool([])}")              # False
print(f"bool([1]) = {bool([1])}")            # True
print(f"bool('') = {bool('')}")              # False
print(f"bool('hi') = {bool('hi')}")          # True
print(f"bool(0) = {bool(0)}")                # False
print(f"bool({{}}) = {bool({})}")            # False


# ============================================================================
# PART 4: FUNCTIONAL PROGRAMMING
# ============================================================================

print("\n" + "=" * 80)
print("PART 4: FUNCTIONAL PROGRAMMING")
print("=" * 80)

# ----------------------------------------------------------------------------
# 4.1 reduce() - Reduce to single value
# ----------------------------------------------------------------------------

print("\n--- reduce() ---")
from functools import reduce

# Sum all elements
result = reduce(lambda x, y: x + y, [1, 2, 3, 4])
print(f"sum with reduce: {result}")  # 10

# Multiply all elements
result = reduce(lambda x, y: x * y, [1, 2, 3, 4])
print(f"multiply with reduce: {result}")  # 24

# Find maximum
result = reduce(lambda x, y: x if x > y else y, [3, 1, 4, 1, 5])
print(f"max with reduce: {result}")  # 5

# Flatten nested list
nested = [[1, 2], [3, 4], [5, 6]]
flattened = reduce(lambda x, y: x + y, nested)
print(f"flatten: {nested} → {flattened}")


# ============================================================================
# PART 5: TESTING & CHECKING
# ============================================================================

print("\n" + "=" * 80)
print("PART 5: TESTING & CHECKING")
print("=" * 80)

# ----------------------------------------------------------------------------
# 5.1 isinstance() - Type checking
# ----------------------------------------------------------------------------

print("\n--- isinstance() ---")
print(f"isinstance([1,2], list) = {isinstance([1, 2], list)}")
print(f"isinstance('hi', str) = {isinstance('hi', str)}")
print(f"isinstance({{1,2}}, set) = {isinstance({1, 2}, set)}")

# Check multiple types
print(f"isinstance([1,2], (list,tuple)) = {isinstance([1, 2], (list, tuple))}")

# ----------------------------------------------------------------------------
# 5.2 type() - Get exact type
# ----------------------------------------------------------------------------

print("\n--- type() ---")
print(f"type([1,2]) = {type([1, 2])}")
print(f"type('hi') = {type('hi')}")
print(f"type({{1,2}}) = {type({1, 2})}")

# ----------------------------------------------------------------------------
# 5.3 hash() - Get hash value
# ----------------------------------------------------------------------------

print("\n--- hash() ---")
print(f"hash('hello') = {hash('hello')}")
print(f"hash((1,2)) = {hash((1, 2))}")
print(f"hash(42) = {hash(42)}")
# print(hash([1, 2]))  # ❌ TypeError (lists not hashable)

# ----------------------------------------------------------------------------
# 5.4 id() - Get memory address
# ----------------------------------------------------------------------------

print("\n--- id() ---")
x = [1, 2, 3]
y = x
z = [1, 2, 3]
print(f"id(x) = {id(x)}")
print(f"id(y) = {id(y)} (same as x: {id(y) == id(x)})")
print(f"id(z) = {id(z)} (same as x: {id(z) == id(x)})")

# ----------------------------------------------------------------------------
# 5.5 repr() - Developer-friendly string
# ----------------------------------------------------------------------------

print("\n--- repr() ---")
print(f"repr([1,2,3]) = {repr([1, 2, 3])}")
print(f"repr('hello') = {repr('hello')}")  # Includes quotes


# ============================================================================
# PART 6: INTERVIEW PATTERNS & ADVANCED USAGE
# ============================================================================

print("\n" + "=" * 80)
print("PART 6: INTERVIEW PATTERNS & ADVANCED USAGE")
print("=" * 80)

# ----------------------------------------------------------------------------
# Pattern 1: Index + Value
# ----------------------------------------------------------------------------

print("\n--- Pattern 1: Index + Value ---")
arr = [3, 1, 4, 1, 5, 9, 2, 6]
max_idx, max_val = max(enumerate(arr), key=lambda x: x[1])
print(f"Array: {arr}")
print(f"Max value {max_val} is at index {max_idx}")

# ----------------------------------------------------------------------------
# Pattern 2: Parallel Iteration
# ----------------------------------------------------------------------------

print("\n--- Pattern 2: Parallel Iteration ---")
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = [a + b for a, b in zip(list1, list2)]
print(f"Sum corresponding: {list1} + {list2} = {result}")

# ----------------------------------------------------------------------------
# Pattern 3: Custom Sorting
# ----------------------------------------------------------------------------

print("\n--- Pattern 3: Custom Sorting ---")

# Sort by absolute value
nums = [-3, -1, 2, 4, -5]
sorted_abs = sorted(nums, key=abs)
print(f"Sort by abs: {nums} → {sorted_abs}")

# Sort by multiple criteria
students = [("Alice", 20, 95), ("Bob", 25, 87), ("Alice", 22, 90)]
sorted_students = sorted(students, key=lambda x: (x[0], -x[2]))
print(f"Sort by name ASC, score DESC:")
for s in sorted_students:
    print(f"  {s}")

# ----------------------------------------------------------------------------
# Pattern 4: Filter + Transform
# ----------------------------------------------------------------------------

print("\n--- Pattern 4: Filter + Transform ---")

# Get squares of even numbers
nums = [1, 2, 3, 4, 5, 6]
result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))
print(f"Squares of evens in {nums}: {result}")

# ----------------------------------------------------------------------------
# Pattern 5: Check All/Any Condition
# ----------------------------------------------------------------------------

print("\n--- Pattern 5: Check All/Any Condition ---")

# Check if all positive
nums = [1, 2, 3, 4, 5]
print(f"All positive in {nums}? {all(x > 0 for x in nums)}")

# Check if any even
nums = [1, 3, 5, 6, 7]
print(f"Any even in {nums}? {any(x % 2 == 0 for x in nums)}")

# ----------------------------------------------------------------------------
# Pattern 6: Dictionary from Two Lists
# ----------------------------------------------------------------------------

print("\n--- Pattern 6: Dictionary from Two Lists ---")
keys = ['name', 'age', 'city']
values = ['Alice', 25, 'NYC']
person = dict(zip(keys, values))
print(f"Create dict: {person}")

# ----------------------------------------------------------------------------
# Pattern 7: Unzip Pairs
# ----------------------------------------------------------------------------

print("\n--- Pattern 7: Unzip Pairs ---")
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
numbers, letters = zip(*pairs)
print(f"Unzip {pairs}")
print(f"  Numbers: {numbers}")
print(f"  Letters: {letters}")

# ----------------------------------------------------------------------------
# Pattern 8: Check if All Unique
# ----------------------------------------------------------------------------

print("\n--- Pattern 8: Check if All Unique ---")

def all_unique(items):
    return len(items) == len(set(items))

print(f"[1,2,3] all unique? {all_unique([1, 2, 3])}")
print(f"[1,2,2] all unique? {all_unique([1, 2, 2])}")

# ----------------------------------------------------------------------------
# Pattern 9: Filter None/Empty Values
# ----------------------------------------------------------------------------

print("\n--- Pattern 9: Filter None/Empty ---")
mixed = [0, 1, None, 2, False, 3, '', 'hello']
filtered = list(filter(None, mixed))
print(f"Filter truthy: {mixed}")
print(f"  Result: {filtered}")

# ----------------------------------------------------------------------------
# Pattern 10: Group by Criteria
# ----------------------------------------------------------------------------

print("\n--- Pattern 10: Group by Criteria ---")
from itertools import groupby

data = [1, 1, 2, 2, 2, 3, 3, 4]
grouped = {k: list(g) for k, g in groupby(data)}
print(f"Group consecutive: {data}")
print(f"  Result: {grouped}")

# ----------------------------------------------------------------------------
# Pattern 11: Enumerate with Custom Start
# ----------------------------------------------------------------------------

print("\n--- Pattern 11: Enumerate with Custom Start ---")
months = ['Jan', 'Feb', 'Mar']
for num, month in enumerate(months, start=1):
    print(f"  Month {num}: {month}")

# ----------------------------------------------------------------------------
# Pattern 12: Max/Min with Default
# ----------------------------------------------------------------------------

print("\n--- Pattern 12: Max/Min with Default ---")
empty_list = []
print(f"max of empty list with default: {max(empty_list, default=0)}")
print(f"min of empty list with default: {min(empty_list, default=float('inf'))}")


# ============================================================================
# PART 7: PERFORMANCE TIPS
# ============================================================================

print("\n" + "=" * 80)
print("PART 7: PERFORMANCE TIPS")
print("=" * 80)

# ----------------------------------------------------------------------------
# Tip 1: Use set for membership tests
# ----------------------------------------------------------------------------

print("\n--- Tip 1: Set for membership ---")
allowed = {'admin', 'editor', 'viewer'}  # Fast O(1) lookup
# Instead of: allowed = ['admin', 'editor', 'viewer']  # Slow O(n)
print(f"'admin' in set: {'admin' in allowed}")

# ----------------------------------------------------------------------------
# Tip 2: Use any() for short-circuit
# ----------------------------------------------------------------------------

print("\n--- Tip 2: any() for short-circuit ---")
# Stops at first True (efficient!)
result = any(x > 5 for x in [1, 2, 3, 6, 7, 8])
print(f"any > 5: {result} (stops at 6, doesn't check 7, 8)")

# ----------------------------------------------------------------------------
# Tip 3: Use enumerate instead of range(len())
# ----------------------------------------------------------------------------

print("\n--- Tip 3: enumerate vs range(len()) ---")
items = ['a', 'b', 'c']

# Bad
print("Using range(len()):")
for i in range(len(items)):
    print(f"  {i}: {items[i]}")

# Good
print("Using enumerate:")
for i, item in enumerate(items):
    print(f"  {i}: {item}")

# ----------------------------------------------------------------------------
# Tip 4: Use sorted() for one-time sort
# ----------------------------------------------------------------------------

print("\n--- Tip 4: sorted() vs .sort() ---")
nums = [3, 1, 4, 1, 5]

# sorted() - returns new list (keeps original)
sorted_nums = sorted(nums)
print(f"Original: {nums}")
print(f"Sorted: {sorted_nums}")

# .sort() - modifies in place (for lists only)
nums_copy = nums.copy()
nums_copy.sort()
print(f"After .sort(): {nums_copy}")

print("\n" + "=" * 80)
print("END OF EXAMPLES - All built-in functions demonstrated!")
print("=" * 80)

print("\n📚 KEY TAKEAWAYS:")
print("1. enumerate() - Get index while iterating")
print("2. zip() - Combine multiple iterables")
print("3. sorted(key=...) - Custom sorting")
print("4. map()/filter() - Functional transforms")
print("5. any()/all() - Boolean operations with short-circuit")
print("6. Use 'in' with sets/dicts for O(1) lookup")
print("7. Type conversion: list(), tuple(), set(), dict()")
print("8. isinstance() for type checking (better than type())")
print("\n🚀 Master these and write cleaner, faster Python code!")