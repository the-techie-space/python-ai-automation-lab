# Set and Tuple - Complete Guide 🎯

## Table of Contents
1. [Introduction](#introduction)
2. [Sets](#sets)
3. [Tuples](#tuples)
4. [Interview Patterns](#interview-patterns)
5. [Common Problems](#common-problems)
6. [Time Complexity](#time-complexity)

---

## Introduction

**Set** and **Tuple** are fundamental Python data structures that complement Lists and Dictionaries. While they're not as complex as Trees or Graphs, they're frequently used in coding interviews and real-world applications.

### When to Use What?

| Need | Use |
|------|-----|
| Unique elements + Fast lookup | **Set** |
| Immutable sequence | **Tuple** |
| Dictionary key (hashable) | **Tuple** |
| Remove duplicates | **Set** |
| Multiple return values | **Tuple** |

---

## Sets

### What is a Set?

A **Set** is an unordered collection of unique elements with O(1) lookup time. Think of it as a Hash Map that only stores keys (no values).

### Key Characteristics
- ✓ **Unordered** - No index access
- ✓ **Unique elements** - Automatically removes duplicates
- ✓ **Mutable** - Can add/remove elements
- ✓ **O(1) operations** - Add, remove, check membership
- ❌ **Not hashable** - Cannot be used as dict key

### Creating Sets

```python
# Empty set
empty_set = set()  # NOT {} - that's a dict!

# With elements
my_set = {1, 2, 3, 4, 5}

# From list (removes duplicates)
numbers = [1, 2, 2, 3, 3, 3, 4]
unique = set(numbers)  # {1, 2, 3, 4}

# From string
chars = set("hello")  # {'h', 'e', 'l', 'o'}
```

### Basic Operations

```python
my_set = {1, 2, 3}

# Add element - O(1)
my_set.add(4)  # {1, 2, 3, 4}

# Remove element - O(1)
my_set.remove(2)  # {1, 3, 4} - Error if not exists
my_set.discard(2)  # {1, 3, 4} - No error if not exists

# Check membership - O(1) ⚡
if 3 in my_set:
    print("Found!")

# Length
len(my_set)  # 3

# Clear all elements
my_set.clear()
```

### Set Mathematics

```python
set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

# Union (all elements from both)
set1 | set2  # {1, 2, 3, 4, 5, 6}
set1.union(set2)

# Intersection (common elements)
set1 & set2  # {3, 4}
set1.intersection(set2)

# Difference (in set1 but not set2)
set1 - set2  # {1, 2}
set1.difference(set2)

# Symmetric difference (in either but not both)
set1 ^ set2  # {1, 2, 5, 6}
set1.symmetric_difference(set2)

# Subset check
{1, 2}.issubset({1, 2, 3})  # True

# Superset check
{1, 2, 3}.issuperset({1, 2})  # True
```

### When to Use Sets in Interviews

1. **Remove duplicates from array**
2. **Check for common elements**
3. **Fast membership testing**
4. **Track visited nodes (graphs/trees)**
5. **Find missing/extra elements**

---

## Tuples

### What is a Tuple?

A **Tuple** is an immutable sequence of elements. Once created, it cannot be modified.

### Key Characteristics
- ✓ **Ordered** - Elements have index
- ✓ **Immutable** - Cannot change after creation
- ✓ **Allows duplicates**
- ✓ **Hashable** - Can be used as dict key
- ✓ **Faster than lists** - Less memory
- ✓ **O(1) access** by index

### Creating Tuples

```python
# Empty tuple
empty = ()

# Single element (note the comma!)
single = (1,)  # Without comma: just int 1

# Multiple elements
coordinates = (10, 20)
rgb = (255, 0, 0)

# Without parentheses (tuple packing)
point = 10, 20  # Same as (10, 20)

# From list
my_list = [1, 2, 3]
my_tuple = tuple(my_list)
```

### Basic Operations

```python
my_tuple = (1, 2, 3, 4, 5)

# Access by index - O(1)
my_tuple[0]  # 1
my_tuple[-1]  # 5

# Slicing - O(k) where k is slice size
my_tuple[1:3]  # (2, 3)

# Length
len(my_tuple)  # 5

# Count occurrences
my_tuple.count(2)  # 1

# Find index
my_tuple.index(3)  # 2

# Concatenation (creates new tuple)
tuple1 = (1, 2)
tuple2 = (3, 4)
combined = tuple1 + tuple2  # (1, 2, 3, 4)

# Repetition
repeated = (1, 2) * 3  # (1, 2, 1, 2, 1, 2)

# CANNOT modify!
# my_tuple[0] = 10  # ❌ TypeError!
```

### Tuple Unpacking

```python
# Basic unpacking
x, y = (10, 20)
print(x, y)  # 10 20

# Swap variables
a, b = 5, 10
a, b = b, a  # Swap using tuple packing/unpacking

# Extended unpacking
first, *middle, last = (1, 2, 3, 4, 5)
# first = 1, middle = [2, 3, 4], last = 5

# Function returns
def get_stats(numbers):
    return min(numbers), max(numbers), sum(numbers)

minimum, maximum, total = get_stats([1, 2, 3, 4, 5])
```

### When to Use Tuples in Interviews

1. **Return multiple values from function**
2. **Dictionary keys (must be hashable)**
3. **Represent coordinates, edges in graphs**
4. **Fixed data that shouldn't change**
5. **Slightly faster than lists for iteration**

---

## Interview Patterns

### Pattern 1: Remove Duplicates with Set

```python
# Remove duplicates from list
def remove_duplicates(arr):
    return list(set(arr))

# Time: O(n), Space: O(n)
```

### Pattern 2: Find Common Elements

```python
# Intersection of two arrays
def intersection(arr1, arr2):
    return list(set(arr1) & set(arr2))

# Time: O(n + m), Space: O(n + m)
```

### Pattern 3: Tuple as Dictionary Key

```python
# Memoization in dynamic programming
cache = {}
def fibonacci(n):
    if n in cache:
        return cache[n]
    if n <= 1:
        return n
    cache[n] = fibonacci(n-1) + fibonacci(n-2)
    return cache[n]

# Graph edges
graph = {
    (0, 1): 5,  # Edge from 0 to 1 with weight 5
    (1, 2): 3,
    (2, 3): 7
}
```

### Pattern 4: Multiple Return Values

```python
def min_max_avg(numbers):
    return (min(numbers), max(numbers), sum(numbers) / len(numbers))

minimum, maximum, average = min_max_avg([1, 2, 3, 4, 5])
```

### Pattern 5: Set for Visited Tracking

```python
def has_cycle(graph, node, visited=None):
    if visited is None:
        visited = set()
    
    if node in visited:
        return True  # Cycle found
    
    visited.add(node)
    # Continue traversal...
```

---

## Common Problems

### Easy Level

1. **Contains Duplicate** - Use set for O(n) solution
2. **Intersection of Arrays** - Set intersection
3. **Remove Duplicates** - Convert to set and back
4. **Valid Anagram** - Compare sorted tuples or character sets
5. **Single Number** - XOR or set operations

### Medium Level

1. **Longest Consecutive Sequence** - Set for O(n) lookup
2. **Group Anagrams** - Tuple of sorted chars as key
3. **3Sum** - Set to avoid duplicates
4. **Word Pattern** - Bijection using sets
5. **Happy Number** - Set to detect cycles

### Hard Level

1. **Longest Substring Without Repeating** - Sliding window + set
2. **Sudoku Validator** - Sets for rows/cols/boxes
3. **Word Ladder** - BFS with visited set
4. **Alien Dictionary** - Topological sort with sets

---

## Time Complexity

### Set Operations

| Operation | Average Case | Worst Case |
|-----------|-------------|------------|
| Add | O(1) | O(n) |
| Remove | O(1) | O(n) |
| Contains | O(1) | O(n) |
| Union | O(len(s1) + len(s2)) | - |
| Intersection | O(min(len(s1), len(s2))) | - |
| Difference | O(len(s1)) | - |

### Tuple Operations

| Operation | Time Complexity |
|-----------|----------------|
| Access | O(1) |
| Search | O(n) |
| Count | O(n) |
| Index | O(n) |
| Slice | O(k) where k is slice size |

---

## Set vs List Performance

```python
# Membership test
my_list = list(range(1000000))
my_set = set(range(1000000))

# List: O(n) - checks each element
999999 in my_list  # SLOW

# Set: O(1) - hash lookup
999999 in my_set  # FAST ⚡
```

**Rule of thumb:** If you need to check `if x in container` repeatedly, use Set!

---

## Interview Tips

### When Interviewer Says...

- "Find unique elements" → Think **Set**
- "Remove duplicates" → Think **Set**
- "Check if exists" repeatedly → Think **Set**
- "Return multiple values" → Think **Tuple**
- "Need immutable collection" → Think **Tuple**
- "Use as dict key" → Think **Tuple**

### Common Mistakes to Avoid

1. ❌ Creating empty set with `{}` → That's a dict!
2. ❌ Trying to modify tuple → It's immutable!
3. ❌ Using list as dict key → Use tuple instead
4. ❌ Forgetting set is unordered → No indexing!
5. ❌ Single element tuple without comma: `(1)` → Just int 1

### Space-Time Tradeoffs

```python
# Brute force - O(n²) time, O(1) space
for i in range(len(arr)):
    for j in range(i+1, len(arr)):
        if arr[i] == arr[j]:
            return True

# Using set - O(n) time, O(n) space
return len(arr) != len(set(arr))
```

**Interview strategy:** Sets often trade space for time!

---

## Next Steps

After mastering Sets and Tuples:
1. ✓ Understand when to use each data structure
2. ✓ Practice problems in `problems.py`
3. ✓ Move on to **Sliding Window** technique
4. ✓ Learn **Recursion** for advanced topics

---

## Quick Reference

```python
# Set cheat sheet
s = {1, 2, 3}
s.add(4)           # Add element
s.remove(2)        # Remove (error if not exists)
s.discard(2)       # Remove (no error)
3 in s             # Check membership - O(1)
len(s)             # Size
s.clear()          # Remove all

# Tuple cheat sheet
t = (1, 2, 3)
t[0]               # Access
t.count(2)         # Count occurrences
t.index(3)         # Find index
x, y, z = t        # Unpack
```

---

**Remember:** Sets and Tuples are tools in your DSA toolkit. Master when to use them, and they'll make your solutions faster and cleaner! 🚀