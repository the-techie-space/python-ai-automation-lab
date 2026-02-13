# Hash Maps (Dictionaries) - Complete DSA Guide 📚

A comprehensive, well-organized collection of hash map (dictionary) problems with clear explanations, multiple approaches, and real-world applications.

## 📂 File Structure

```
DSA/HashMaps/
├── README.md                       # You are here!
├── 01_basics_fundamentals.py      # Dictionary fundamentals & operations
├── 02_counting_patterns.py        # Frequency counting techniques
├── 03_finding_duplicates.py       # Duplicate detection patterns
├── 04_two_sum_complement.py       # Two Sum & complement patterns
└── 05_grouping_anagrams.py        # Grouping & anagram problems
```

## 🎯 Learning Path

### **Beginner** (Start Here)
1. **01_basics_fundamentals.py** - Learn dictionary syntax, operations, why O(1)?
2. **02_counting_patterns.py** - Master frequency counting (most common pattern)

### **Intermediate**
3. **03_finding_duplicates.py** - Duplicate detection using hash maps
4. **04_two_sum_complement.py** - The #1 interview question!

### **Advanced**
5. **05_grouping_anagrams.py** - Grouping patterns and anagram problems

## 📖 What You'll Learn

### File 1: Basics & Fundamentals (01_basics_fundamentals.py)
- ✓ What is a hash map and why O(1)?
- ✓ Creating dictionaries (4 methods)
- ✓ Essential operations (access, add, update, delete)
- ✓ .get() vs [] access (critical difference!)
- ✓ Dictionary methods (keys, values, items, pop, update)
- ✓ Iterating over dictionaries
- ✓ Nested dictionaries
- ✓ When to use dict vs list

### File 2: Counting Patterns (02_counting_patterns.py)
- ✓ Character frequency counting (4 methods)
- ✓ Word frequency counting
- ✓ Number frequency counting
- ✓ Finding most/least frequent elements
- ✓ Filtering by frequency
- ✓ Case-insensitive counting
- ✓ Counting with filtering
- ✓ Using Counter from collections

### File 3: Finding Duplicates (03_finding_duplicates.py)
- ✓ Contains duplicate (3 methods)
- ✓ First duplicate
- ✓ Find all duplicates
- ✓ First unique element
- ✓ First unique character in string
- ✓ Duplicate within K distance
- ✓ Count distinct elements
- ✓ Dictionary vs Set comparison

### File 4: Two Sum & Complement (04_two_sum_complement.py)
- ✓ Two Sum problem (brute force vs optimal)
- ✓ The complement pattern explained
- ✓ Step-by-step visualization
- ✓ Return indices vs values
- ✓ Find all pairs (not just first)
- ✓ Count pairs
- ✓ Two Sum in sorted array
- ✓ Three Sum extension

### File 5: Grouping & Anagrams (05_grouping_anagrams.py)
- ✓ Group anagrams (top interview question!)
- ✓ Group by digit sum
- ✓ Group by length
- ✓ Group by first character
- ✓ Valid anagram (3 methods)
- ✓ Group shifted strings
- ✓ Generic grouping template
- ✓ Using defaultdict

## 🔥 Key Patterns Covered

| Pattern | Use Case | Time | Problems |
|---------|----------|------|----------|
| **Frequency Counting** | Count occurrences | O(n) | Character/word frequency, duplicates |
| **Seen Set** | Track visited | O(n) | Contains duplicate, first duplicate |
| **Complement** | Find pair with sum | O(n) | Two Sum, Three Sum |
| **Grouping** | Group by property | O(n*k) | Group anagrams, digit sum |
| **Index Tracking** | Store positions | O(n) | Two Sum, nearby duplicate |

## ⚡ Time Complexity Quick Reference

| Operation | Dict | List | Set |
|-----------|------|------|-----|
| Access by key/index | O(1) | O(1) | - |
| Search for value | O(n) | O(n) | O(1) |
| Insert | O(1) | O(1) or O(n) | O(1) |
| Delete | O(1) | O(n) | O(1) |
| Check existence | O(1) | O(n) | O(1) |

## 💡 Common Interview Patterns

### Pattern 1: Frequency Counting
```python
count = {}
for item in items:
    count[item] = count.get(item, 0) + 1
```

### Pattern 2: Seen/Visited
```python
seen = set()  # or {}
for item in items:
    if item in seen:
        # Found duplicate!
    seen.add(item)  # or seen[item] = True
```

### Pattern 3: Complement
```python
seen = {}  # value → index
for i, num in enumerate(nums):
    complement = target - num
    if complement in seen:
        return [seen[complement], i]
    seen[num] = i
```

### Pattern 4: Grouping
```python
from collections import defaultdict
groups = defaultdict(list)
for item in items:
    key = calculate_key(item)
    groups[key].append(item)
```

## 🔍 Problem Index

### By Difficulty

**Easy**
- Dictionary basics (01)
- Character frequency (02)
- Contains duplicate (03)
- Valid anagram (05)

**Medium**
- Two Sum ⭐⭐⭐ (04)
- First unique character (03)
- Group anagrams ⭐⭐⭐ (05)
- Top K frequent elements (02)
- Duplicate within K (03)

**Hard**
- Three Sum (04)
- Group shifted strings (05)
- Four Sum variations (04)

### By Pattern

**Frequency Counting**
- Character frequency (02)
- Word frequency (02)
- Most frequent element (02)
- Top K frequent (02)

**Duplicate Detection**
- Contains duplicate (03)
- First duplicate (03)
- All duplicates (03)
- First unique (03)

**Complement Pattern**
- Two Sum (04)
- Three Sum (04)
- Count pairs (04)

**Grouping**
- Group anagrams (05)
- Group by digit sum (05)
- Group by length (05)

## 🎓 Interview Preparation

### Must-Know Problems (Star Rating)
- ⭐⭐⭐ Two Sum (appears in 40% of interviews)
- ⭐⭐⭐ Group Anagrams (very common)
- ⭐⭐ Contains Duplicate
- ⭐⭐ First Unique Character
- ⭐⭐ Valid Anagram

### Common Follow-ups
After solving Two Sum, interviewers often ask:
- "What if array is sorted?" → Two pointers
- "Find all pairs?" → Modify to collect all
- "What about Three Sum?" → Extension
- "Count pairs instead?" → Track frequency

### Time Complexity Discussion
Always be ready to explain:
- Why hash map is O(1) for lookup
- Trade-off: O(n) space for O(n) time
- Alternative approaches (brute force, sorting)

## 📝 Best Practices

### When to Use Dictionary vs Set vs List

**Use Dictionary when:**
- Need key-value mapping
- Need to count frequency
- Need to track indices
- Need to group items

**Use Set when:**
- Only need existence check
- No associated data
- Automatically handle uniqueness

**Use List when:**
- Order matters
- Need index access
- Duplicates are meaningful

### Code Style Tips
1. **Use .get() for safe access**: `dict.get(key, default)`
2. **Use defaultdict for grouping**: `defaultdict(list)`
3. **Use Counter for counting**: `Counter(items)`
4. **Use in for membership**: `if key in dict`
5. **Iterate with .items()**: `for k, v in dict.items()`

## 🚀 Advanced Topics

After mastering basic hash maps:
1. **OrderedDict** - Preserves insertion order
2. **ChainMap** - Combine multiple dicts
3. **Hash collisions** - Understanding internals
4. **Custom hash functions** - For complex keys
5. **LRU Cache** - Using OrderedDict

## 📊 Comparison: Dict vs Other Data Structures

```
Dictionary (Hash Map):
✓ Fast lookup O(1)
✓ Fast insert/delete O(1)
✓ No order guarantee (Python 3.7+ maintains insertion order)
✗ Uses more memory
Use: When need fast key-based access

List:
✓ Ordered
✓ Index-based access O(1)
✗ Search by value O(n)
✗ Insert/delete O(n)
Use: When order matters, sequential data

Set:
✓ Fast lookup O(1)
✓ Automatic uniqueness
✗ No associated values
✗ No order
Use: When only need existence check
```

## 🤝 Common Gotchas

1. **KeyError**: Use .get() or check with `in`
2. **Mutable keys**: Can't use lists/dicts as keys
3. **Default values**: Use .get(key, default) or defaultdict
4. **Iteration during modification**: Make a copy first
5. **None as value**: .get() returns None by default

## 📚 Practice Resources

### LeetCode Hash Table Tag
- Easy: 50+ problems
- Medium: 100+ problems
- Hard: 30+ problems

### By Company
- **Facebook**: Two Sum, Group Anagrams
- **Google**: Subarray Sum, Longest Substring
- **Amazon**: Two Sum, Valid Anagram
- **Microsoft**: Contains Duplicate, Top K Frequent

## 🔗 Related Concepts

1. **Hash Functions** - How keys map to indices
2. **Collision Resolution** - Chaining vs open addressing
3. **Load Factor** - When dict resizes
4. **Time Complexity** - Amortized O(1)
5. **Space Complexity** - O(n) storage

---

## 📊 Progress Tracker

- [ ] Completed 01_basics_fundamentals.py
- [ ] Completed 02_counting_patterns.py
- [ ] Completed 03_finding_duplicates.py
- [ ] Completed 04_two_sum_complement.py
- [ ] Completed 05_grouping_anagrams.py
- [ ] Solved Two Sum independently
- [ ] Solved Group Anagrams independently
- [ ] Can explain O(1) lookup
- [ ] Ready for hash map interviews!

---

## 🎯 Learning Outcomes

After completing this module, you should be able to:

✓ Explain why hash maps provide O(1) lookup
✓ Choose between dict, set, and list appropriately
✓ Implement frequency counting efficiently
✓ Detect duplicates in multiple ways
✓ Solve Two Sum and its variations
✓ Group items by properties
✓ Detect and group anagrams
✓ Handle edge cases (empty inputs, no solution)
✓ Optimize space/time trade-offs
✓ Ace hash map interview questions!

---

**Happy Coding! 🎉**

*Master these hash map patterns and you'll solve 30-40% of all coding interview problems!*

## 💬 Quick Reference Card

```python
# Create
d = {}
d = dict()
d = {"key": "value"}

# Access
d["key"]           # Raises KeyError if missing
d.get("key")       # Returns None if missing
d.get("key", 0)    # Returns 0 if missing

# Add/Update
d["key"] = value

# Delete
del d["key"]
d.pop("key")
d.pop("key", default)

# Check
"key" in d

# Iterate
for key in d:
for key, value in d.items():
for value in d.values():

# Frequency count
count[x] = count.get(x, 0) + 1

# Grouping
from collections import defaultdict
groups = defaultdict(list)
groups[key].append(item)
```