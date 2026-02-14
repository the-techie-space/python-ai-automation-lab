# Python Built-in Functions - Cross Data Type Reference 🐍

## Table of Contents
1. [Overview](#overview)
2. [Basic Functions](#basic-functions)
3. [Iteration Functions](#iteration-functions)
4. [Type Conversion](#type-conversion)
5. [Functional Programming](#functional-programming)
6. [Testing & Checking](#testing--checking)
7. [Comparison Table](#comparison-table)
8. [Interview Essentials](#interview-essentials)
9. [Hidden Gems](#hidden-gems)

---

## Overview

This guide covers Python built-in functions that work **across multiple data types** (strings, lists, tuples, sets, dictionaries). Understanding which functions work with which types is crucial for writing efficient code and acing interviews!

**Key Principle:** 
- Some functions work on **ALL iterables** (like `len()`, `in`)
- Some work on **MOST** but not all (like `count()` - no set/dict)
- Some are **type-specific** (like `.append()` - lists only)

---

## Basic Functions

### `len()` - Works on ALL containers ✅

Get the number of elements in any container.

```python
len("python")        # 6
len([1, 2, 3])       # 3
len((1, 2))          # 2
len({1, 2, 3})       # 3
len({"a": 1})        # 1 (counts key-value pairs)
```

**Time Complexity:** O(1) for all types

---

### `count()` - String, List, Tuple ONLY ⚠️

Count occurrences of an element.

```python
# ✅ Works
"banana".count("a")        # 3
"banana".count("na")       # 2
[1, 2, 3, 2, 2].count(2)   # 3
(1, 1, 2).count(1)         # 2

# ❌ Doesn't work
# {1, 2, 3}.count(1)       # AttributeError
# {"a": 1}.count("a")      # AttributeError
```

**Why not sets/dicts?** Sets have unique elements (count is always 0 or 1), use `in` instead.

**Time Complexity:** O(n)

---

### `index()` - String, List, Tuple ONLY ⚠️

Find the first index of an element.

```python
# ✅ Works
"python".index("t")        # 2
[10, 20, 30].index(20)     # 1
(5, 6, 7).index(7)         # 2

# ❌ Doesn't work
# {1, 2, 3}.index(1)       # AttributeError (sets are unordered!)
```

**Raises ValueError** if element not found. Use `try-except` or check with `in` first.

**Time Complexity:** O(n)

---

### `in` / `not in` - ALL iterables ✅

Check membership.

```python
# All data types
"a" in "cat"               # True
2 in [1, 2, 3]             # True
1 in (1, 2)                # True
1 in {1, 2}                # True
"a" in {"a": 1}            # True (checks keys, not values!)
```

**Time Complexity:**
- String, List, Tuple: O(n)
- Set, Dict: O(1) ⚡ **This is why sets are powerful!**

---

### `sorted()` - ALL iterables ✅

Returns a **new sorted list** (doesn't modify original).

```python
sorted("cba")              # ['a', 'b', 'c']
sorted([3, 1, 2])          # [1, 2, 3]
sorted((3, 2, 1))          # [1, 2, 3]
sorted({3, 1, 2})          # [1, 2, 3]
sorted({"b": 1, "a": 2})   # ['a', 'b'] (keys only)

# Custom sorting
sorted([3, 1, 2], reverse=True)  # [3, 2, 1]
sorted(["abc", "a", "ab"], key=len)  # ['a', 'ab', 'abc']
```

**Note:** `.sort()` method exists **only for lists** and modifies in-place.

**Time Complexity:** O(n log n)

---

### `min()` / `max()` - Comparable iterables ✅

Find minimum or maximum element.

```python
min("python")              # 'h'
max([1, 5, 2])             # 5
min({3, 1, 2})             # 1
max((4, 2, 8))             # 8

# Custom key function
words = ["apple", "a", "at"]
min(words, key=len)        # "a"
max(words, key=len)        # "apple"

# With default (avoid errors on empty)
max([], default=0)         # 0 (no error!)
```

**Time Complexity:** O(n)

---

### `sum()` - Numeric iterables (NOT string/dict) ⚠️

Sum all numeric elements.

```python
# ✅ Works
sum([1, 2, 3])             # 6
sum((4, 5))                # 9
sum({1, 2, 3})             # 6

# With start value
sum([1, 2, 3], 10)         # 16 (10 + 1 + 2 + 3)

# ❌ Doesn't work
# sum("123")               # TypeError
# sum({"a": 1})            # TypeError
```

**Time Complexity:** O(n)

---

### `any()` / `all()` - ALL iterables ✅

Boolean operations on iterables.

```python
# any() - True if ANY element is truthy
any([0, 0, 1])             # True
any([False, False, False]) # False
any("hello")               # True (non-empty string)
any([])                    # False (empty)

# all() - True if ALL elements are truthy
all([1, 2, 3])             # True
all([1, 0, 3])             # False
all([])                    # True (vacuous truth)
all("")                    # True (empty is True for all)
```

**Use Cases:**
```python
# Check if all numbers are positive
all(x > 0 for x in [1, 2, 3])  # True

# Check if any element is even
any(x % 2 == 0 for x in [1, 3, 5, 6])  # True
```

**Time Complexity:** O(n) worst case, but stops early

---

## Iteration Functions

### `enumerate()` - ALL iterables ✅

Get index along with value during iteration.

```python
# Basic usage
for i, char in enumerate("abc"):
    print(i, char)
# Output:
# 0 a
# 1 b
# 2 c

# Works with all types
list(enumerate([10, 20, 30]))
# [(0, 10), (1, 20), (2, 30)]

list(enumerate({1, 2, 3}))
# [(0, 1), (1, 2), (2, 3)]

# Custom start index
list(enumerate(['a', 'b'], start=1))
# [(1, 'a'), (2, 'b')]
```

**Interview Use:** Finding index while iterating without manual counter.

**Time Complexity:** O(1) per iteration

---

### `zip()` - Combine iterables ✅

Combine multiple iterables element-wise.

```python
# Basic usage
names = ["Alice", "Bob", "Charlie"]
ages = [25, 30, 35]
list(zip(names, ages))
# [('Alice', 25), ('Bob', 30), ('Charlie', 35)]

# Multiple iterables
list(zip([1, 2], ['a', 'b'], [True, False]))
# [(1, 'a', True), (2, 'b', False)]

# Unequal lengths (stops at shortest)
list(zip([1, 2, 3], ['a', 'b']))
# [(1, 'a'), (2, 'b')]

# Unzip using zip(*...)
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
numbers, letters = zip(*pairs)
# numbers = (1, 2, 3)
# letters = ('a', 'b', 'c')

# Create dictionary
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dict(zip(keys, values))
# {'a': 1, 'b': 2, 'c': 3}
```

**Interview Use:** Parallel iteration, creating dicts, matrix operations.

---

### `map()` - Apply function to all elements ✅

Transform all elements using a function.

```python
# Basic usage
list(map(str.upper, ["a", "b", "c"]))
# ['A', 'B', 'C']

# With lambda
list(map(lambda x: x * 2, [1, 2, 3]))
# [2, 4, 6]

# Multiple iterables
list(map(lambda x, y: x + y, [1, 2, 3], [10, 20, 30]))
# [11, 22, 33]

# Type conversion
list(map(int, ["1", "2", "3"]))
# [1, 2, 3]

# Works with any iterable
list(map(len, ["a", "ab", "abc"]))
# [1, 2, 3]
```

**Time Complexity:** O(n)

---

### `filter()` - Keep elements matching condition ✅

Filter elements based on a condition.

```python
# Basic usage
list(filter(lambda x: x > 2, [1, 2, 3, 4]))
# [3, 4]

# Filter even numbers
list(filter(lambda x: x % 2 == 0, [1, 2, 3, 4, 5]))
# [2, 4]

# Filter truthy values
list(filter(None, [0, 1, False, True, "", "hello"]))
# [1, True, 'hello']

# String filtering
list(filter(str.isalpha, "a1b2c3"))
# ['a', 'b', 'c']

# Filter non-empty strings
list(filter(bool, ["", "a", "", "b"]))
# ['a', 'b']
```

**Time Complexity:** O(n)

---

### `reversed()` - Reverse iteration ✅

Return reversed iterator (doesn't modify original).

```python
# Works with sequences
list(reversed("hello"))
# ['o', 'l', 'l', 'e', 'h']

list(reversed([1, 2, 3]))
# [3, 2, 1]

list(reversed((1, 2, 3)))
# [3, 2, 1]

# ❌ Doesn't work with sets (unordered)
# list(reversed({1, 2, 3}))  # TypeError

# Note: For lists, slicing is often simpler
my_list[::-1]  # Reverse list
```

**Time Complexity:** O(1) to create iterator, O(n) to consume

---

## Type Conversion

### Convert Between Types

```python
# To String
str([1, 2, 3])      # '[1, 2, 3]'
str({1, 2})         # '{1, 2}'
str((1, 2))         # '(1, 2)'

# To List
list("abc")         # ['a', 'b', 'c']
list({1, 2, 3})     # [1, 2, 3]
list((1, 2))        # [1, 2]
list({"a": 1})      # ['a'] (keys only!)

# To Tuple
tuple([1, 2, 3])    # (1, 2, 3)
tuple("abc")        # ('a', 'b', 'c')
tuple({1, 2})       # (1, 2)

# To Set (removes duplicates)
set([1, 2, 2, 3])   # {1, 2, 3}
set("hello")        # {'h', 'e', 'l', 'o'}
set((1, 2, 2))      # {1, 2}

# To Dict
dict([("a", 1), ("b", 2)])      # {'a': 1, 'b': 2}
dict(zip(["a", "b"], [1, 2]))   # {'a': 1, 'b': 2}

# To Bool (empty = False)
bool([])            # False
bool([1])           # True
bool("")            # False
bool("hi")          # True
bool(0)             # False
bool({})            # False
```

---

## Functional Programming

### `reduce()` - Reduce to single value

**Requires import:** `from functools import reduce`

```python
from functools import reduce

# Sum all elements
reduce(lambda x, y: x + y, [1, 2, 3, 4])
# 10

# Multiply all elements
reduce(lambda x, y: x * y, [1, 2, 3, 4])
# 24

# Find maximum
reduce(lambda x, y: x if x > y else y, [3, 1, 4, 1, 5])
# 5

# Flatten nested list
reduce(lambda x, y: x + y, [[1, 2], [3, 4], [5, 6]])
# [1, 2, 3, 4, 5, 6]
```

**Note:** For sum, use `sum()`. For max, use `max()`. Use `reduce()` for custom operations.

---

## Testing & Checking

### Type Checking

```python
# isinstance() - Check if object is instance of type
isinstance([1, 2], list)        # True
isinstance("hi", str)           # True
isinstance({1, 2}, set)         # True

# Check multiple types
isinstance([1, 2], (list, tuple))  # True

# type() - Get exact type
type([1, 2])                    # <class 'list'>
type("hi")                      # <class 'str'>

# Type comparison
type([1, 2]) == list            # True
```

**Best Practice:** Use `isinstance()` for type checking (handles inheritance).

---

### Other Checking Functions

```python
# hash() - Get hash value (for hashable types only)
hash("hello")       # Some integer
hash((1, 2))        # Some integer
hash(42)            # 42
# hash([1, 2])      # ❌ TypeError (lists not hashable)

# id() - Get object's memory address
x = [1, 2, 3]
id(x)               # Memory address (unique per object)

y = x
id(y) == id(x)      # True (same object)

z = [1, 2, 3]
id(z) == id(x)      # False (different object)

# repr() - Developer-friendly string representation
repr([1, 2, 3])     # '[1, 2, 3]'
repr("hello")       # "'hello'" (includes quotes)
```

---

## Comparison Table

| Function | String | List | Tuple | Set | Dict | Returns | Notes |
|----------|--------|------|-------|-----|------|---------|-------|
| `len()` | ✅ | ✅ | ✅ | ✅ | ✅ | int | Count of elements |
| `count()` | ✅ | ✅ | ✅ | ❌ | ❌ | int | Occurrences |
| `index()` | ✅ | ✅ | ✅ | ❌ | ❌ | int | First index |
| `in` | ✅ | ✅ | ✅ | ✅ | ✅ | bool | O(1) for set/dict |
| `sorted()` | ✅ | ✅ | ✅ | ✅ | ✅ | list | Always returns list |
| `min()`/`max()` | ✅ | ✅ | ✅ | ✅ | ✅ | element | Comparable items |
| `sum()` | ❌ | ✅ | ✅ | ✅ | ❌ | number | Numeric only |
| `any()`/`all()` | ✅ | ✅ | ✅ | ✅ | ✅ | bool | Boolean check |
| `enumerate()` | ✅ | ✅ | ✅ | ✅ | ✅ | iterator | Index + value |
| `zip()` | ✅ | ✅ | ✅ | ✅ | ✅ | iterator | Combine iterables |
| `map()` | ✅ | ✅ | ✅ | ✅ | ✅ | iterator | Transform elements |
| `filter()` | ✅ | ✅ | ✅ | ✅ | ✅ | iterator | Filter elements |
| `reversed()` | ✅ | ✅ | ✅ | ❌ | ❌* | iterator | *Dicts in 3.8+ |

---

## Interview Essentials

### Top 10 Must-Know Functions

```python
# 1. enumerate() - Index while iterating
for i, val in enumerate([10, 20, 30]):
    print(f"Index {i}: {val}")

# 2. zip() - Parallel iteration
names = ["Alice", "Bob"]
scores = [95, 87]
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# 3. sorted(key=...) - Custom sorting
students = [("Alice", 20), ("Bob", 25), ("Charlie", 22)]
sorted(students, key=lambda x: x[1])
# [('Alice', 20), ('Charlie', 22), ('Bob', 25)]

# 4. map() - Transform all elements
list(map(lambda x: x**2, [1, 2, 3]))
# [1, 4, 9]

# 5. filter() - Keep matching elements
list(filter(lambda x: x > 0, [-1, 0, 1, 2]))
# [1, 2]

# 6. any()/all() - Boolean operations
any([False, False, True])   # True
all([True, True, True])     # True

# 7. max/min with key
words = ["a", "abc", "ab"]
max(words, key=len)         # "abc"

# 8. reversed() - Reverse iteration
list(reversed([1, 2, 3]))   # [3, 2, 1]

# 9. isinstance() - Type checking
if isinstance(data, (list, tuple)):
    print("Sequence!")

# 10. dict(zip()) - Create dict from lists
keys = ['a', 'b', 'c']
values = [1, 2, 3]
dict(zip(keys, values))     # {'a': 1, 'b': 2, 'c': 3}
```

---

## Hidden Gems

### Advanced Patterns

```python
# 1. max/min with default (avoid error on empty)
max([], default=0)                    # 0 (no error!)
min([], default=float('inf'))         # inf

# 2. sorted with multiple keys
students = [("Alice", 20, 95), ("Bob", 25, 87), ("Alice", 22, 90)]
sorted(students, key=lambda x: (x[0], -x[2]))
# Sort by name ascending, then score descending

# 3. enumerate with custom start
list(enumerate(['a', 'b', 'c'], start=1))
# [(1, 'a'), (2, 'b'), (3, 'c')]

# 4. zip(*...) for unzipping
pairs = [(1, 'a'), (2, 'b'), (3, 'c')]
numbers, letters = zip(*pairs)
# numbers = (1, 2, 3), letters = ('a', 'b', 'c')

# 5. any/all with generator (memory efficient)
any(x > 100 for x in range(1000000))  # True, stops early
all(x < 10 for x in range(5))         # True

# 6. sorted with reverse
sorted([3, 1, 2], reverse=True)       # [3, 2, 1]

# 7. Check if all elements are unique
def all_unique(items):
    return len(items) == len(set(items))

# 8. Filter None values
list(filter(None, [0, 1, None, 2, False, 3]))
# [1, 2, 3]

# 9. Sum with start value
sum([1, 2, 3], 100)                   # 106

# 10. Create ranges of tuples
list(zip(range(1, 4), range(10, 13)))
# [(1, 10), (2, 11), (3, 12)]
```

---

## Quick Reference Cheat Sheet

```python
# BASIC OPERATIONS
len(container)              # Size
item in container          # Membership (O(1) for set/dict!)
sorted(iterable)           # Sort (returns new list)
min(iterable) / max(iterable)  # Extremes

# ITERATION
enumerate(iterable)        # Index + value
zip(iter1, iter2, ...)    # Combine
map(func, iterable)       # Transform
filter(func, iterable)    # Filter
reversed(sequence)        # Reverse

# CONVERSION
list(iterable)            # To list
tuple(iterable)           # To tuple
set(iterable)             # To set (removes duplicates)
dict(pairs)               # To dict

# BOOLEAN
any(iterable)             # True if any truthy
all(iterable)             # True if all truthy
bool(value)               # Convert to bool

# TYPE CHECKING
isinstance(obj, type)     # Check type
type(obj)                 # Get type
hash(obj)                 # Hash value (if hashable)
```

---

## Common Interview Patterns

### Pattern 1: Index + Value
```python
# Find index of max element
arr = [3, 1, 4, 1, 5]
max_idx = max(enumerate(arr), key=lambda x: x[1])[0]
```

### Pattern 2: Parallel Iteration
```python
# Sum corresponding elements
list1 = [1, 2, 3]
list2 = [4, 5, 6]
result = [a + b for a, b in zip(list1, list2)]
```

### Pattern 3: Custom Sorting
```python
# Sort by absolute value
sorted([-3, -1, 2, 4], key=abs)  # [-1, 2, -3, 4]
```

### Pattern 4: Filter + Transform
```python
# Get squares of even numbers
nums = [1, 2, 3, 4, 5, 6]
result = list(map(lambda x: x**2, filter(lambda x: x % 2 == 0, nums)))
# [4, 16, 36]
```

### Pattern 5: Check All/Any Condition
```python
# Check if all elements are positive
all(x > 0 for x in [1, 2, 3])  # True

# Check if any element is even
any(x % 2 == 0 for x in [1, 3, 5, 6])  # True
```

---

## Memory & Performance Tips

### When to Use What

**Use `map()` when:** Transforming all elements
```python
# Instead of:
result = [x * 2 for x in numbers]
# Consider:
result = list(map(lambda x: x * 2, numbers))
```

**Use `filter()` when:** Selecting subset
```python
# Instead of:
result = [x for x in numbers if x > 0]
# Consider:
result = list(filter(lambda x: x > 0, numbers))
```

**Use `any()`/`all()` when:** Short-circuit evaluation needed
```python
# Stops at first True (efficient!)
any(expensive_check(x) for x in huge_list)
```

**Use `enumerate()` when:** Need index + value
```python
# Instead of:
for i in range(len(items)):
    print(i, items[i])
# Use:
for i, item in enumerate(items):
    print(i, item)
```

---

## Summary

**Must memorize for interviews:**
1. `enumerate()` - Get index while iterating
2. `zip()` - Combine multiple iterables  
3. `sorted(key=...)` - Custom sorting
4. `map()` / `filter()` - Functional transforms
5. `any()` / `all()` - Boolean checks
6. `max(key=...)` / `min(key=...)` - Custom comparison

**Good to know:**
- `reversed()` - Reverse iteration
- `isinstance()` - Type checking
- `hash()` - Hashability check
- Type conversions: `list()`, `tuple()`, `set()`, `dict()`

**Remember:**
- `in` is O(1) for set/dict but O(n) for list/tuple
- `sorted()` returns new list, `.sort()` modifies in-place (lists only)
- Empty containers are `False` in boolean context
- Use `default` parameter in `max()/min()` to avoid errors on empty

---

**Master these functions and you'll write cleaner, faster, more Pythonic code!** 🚀