"""
SET AND TUPLE - ADVANCED TOPICS
================================

This file covers:
1. Frozenset (immutable sets)
2. Set comprehensions
3. Performance optimization techniques
4. Real-world applications
5. Advanced patterns and tricks
6. Memory efficiency

Author: DSA Learning
"""

# ============================================================================
# PART 1: FROZENSET - IMMUTABLE SETS
# ============================================================================

print("=" * 70)
print("PART 1: FROZENSET - IMMUTABLE SETS")
print("=" * 70)

# -----------------------------------------------------------------------------
# 1.1 What is Frozenset?
# -----------------------------------------------------------------------------

# Regular set - mutable
regular_set = {1, 2, 3}
regular_set.add(4)  # Works
print(f"Regular set: {regular_set}")

# Frozenset - immutable
frozen = frozenset([1, 2, 3])
# frozen.add(4)  # ❌ AttributeError: 'frozenset' object has no attribute 'add'
print(f"Frozenset: {frozen}")

# -----------------------------------------------------------------------------
# 1.2 Why Use Frozenset?
# -----------------------------------------------------------------------------

# Reason 1: Can be used as dictionary keys
cache = {}
key1 = frozenset([1, 2, 3])
key2 = frozenset([4, 5, 6])
cache[key1] = "Result for set {1,2,3}"
cache[key2] = "Result for set {4,5,6}"
print(f"\nCache with frozenset keys: {cache}")

# Reason 2: Can be elements of other sets
set_of_sets = {
    frozenset([1, 2]),
    frozenset([3, 4]),
    frozenset([5, 6])
}
print(f"Set of frozensets: {set_of_sets}")

# Reason 3: Guarantee immutability
ALLOWED_OPERATIONS = frozenset(['read', 'write', 'execute'])
# ALLOWED_OPERATIONS.add('delete')  # ❌ Can't modify!

# -----------------------------------------------------------------------------
# 1.3 Frozenset Operations
# -----------------------------------------------------------------------------

fs1 = frozenset([1, 2, 3, 4])
fs2 = frozenset([3, 4, 5, 6])

# All set operations work (return new frozenset)
print(f"\nUnion: {fs1 | fs2}")
print(f"Intersection: {fs1 & fs2}")
print(f"Difference: {fs1 - fs2}")
print(f"Symmetric diff: {fs1 ^ fs2}")

# Membership test
print(f"3 in fs1? {3 in fs1}")

# Convert between set and frozenset
mutable = set(fs1)
immutable = frozenset(mutable)

# -----------------------------------------------------------------------------
# 1.4 Practical Use Case: Graph with Set Edges
# -----------------------------------------------------------------------------

class GraphWithSetEdges:
    """
    Graph where edges are represented as frozensets
    Undirected graph: edge (A, B) same as (B, A)
    """
    def __init__(self):
        self.edges = {}  # frozenset: weight
    
    def add_edge(self, node1, node2, weight):
        edge = frozenset([node1, node2])
        self.edges[edge] = weight
    
    def get_weight(self, node1, node2):
        edge = frozenset([node1, node2])
        return self.edges.get(edge, None)
    
    def has_edge(self, node1, node2):
        edge = frozenset([node1, node2])
        return edge in self.edges

# Test
graph = GraphWithSetEdges()
graph.add_edge('A', 'B', 5)
graph.add_edge('B', 'C', 3)

print(f"\nWeight of A-B: {graph.get_weight('A', 'B')}")
print(f"Weight of B-A (same edge): {graph.get_weight('B', 'A')}")
print(f"Has edge A-C? {graph.has_edge('A', 'C')}")


# ============================================================================
# PART 2: SET COMPREHENSIONS
# ============================================================================

print("\n" + "=" * 70)
print("PART 2: SET COMPREHENSIONS")
print("=" * 70)

# -----------------------------------------------------------------------------
# 2.1 Basic Set Comprehensions
# -----------------------------------------------------------------------------

# Square of numbers
squares = {x**2 for x in range(10)}
print(f"Squares: {squares}")

# Even numbers
evens = {x for x in range(20) if x % 2 == 0}
print(f"Even numbers: {evens}")

# First letter of words
words = ["apple", "banana", "apricot", "blueberry", "cherry"]
first_letters = {word[0] for word in words}
print(f"First letters: {first_letters}")

# Lengths of strings
lengths = {len(word) for word in words}
print(f"Unique lengths: {lengths}")

# -----------------------------------------------------------------------------
# 2.2 Advanced Comprehensions
# -----------------------------------------------------------------------------

# Nested comprehension - all divisors
number = 24
divisors = {i for i in range(1, number + 1) if number % i == 0}
print(f"\nDivisors of {number}: {divisors}")

# Multiple conditions
special_numbers = {x for x in range(100) 
                  if x % 3 == 0 and x % 5 == 0}
print(f"Numbers divisible by both 3 and 5: {special_numbers}")

# Using functions in comprehension
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

primes = {x for x in range(50) if is_prime(x)}
print(f"Prime numbers < 50: {primes}")

# Flatten nested structure
nested = [[1, 2], [3, 4], [5, 6]]
flattened = {item for sublist in nested for item in sublist}
print(f"Flattened: {flattened}")

# -----------------------------------------------------------------------------
# 2.3 Set Comprehension vs Generator
# -----------------------------------------------------------------------------

# Set comprehension - creates set immediately
set_comp = {x**2 for x in range(1000)}  # Uses memory

# Generator - lazy evaluation
gen = (x**2 for x in range(1000))  # Doesn't use memory until needed

# Convert generator to set when needed
set_from_gen = set(gen)

print(f"\nSet comprehension size: {len(set_comp)}")
print(f"Memory efficient generator pattern demonstrated")


# ============================================================================
# PART 3: PERFORMANCE OPTIMIZATION
# ============================================================================

print("\n" + "=" * 70)
print("PART 3: PERFORMANCE OPTIMIZATION")
print("=" * 70)

# -----------------------------------------------------------------------------
# 3.1 When to Use Set vs List
# -----------------------------------------------------------------------------

import time

# Scenario 1: Many membership tests
def find_common_slow(list1, list2):
    """Using list - O(n*m)"""
    common = []
    for item in list1:
        if item in list2:  # O(n) each time!
            common.append(item)
    return common

def find_common_fast(list1, list2):
    """Using set - O(n+m)"""
    set2 = set(list2)  # Convert once
    common = []
    for item in list1:
        if item in set2:  # O(1) each time!
            common.append(item)
    return common

# Test with large lists
large_list1 = list(range(5000))
large_list2 = list(range(2500, 7500))

start = time.time()
result1 = find_common_slow(large_list1, large_list2)
time_slow = time.time() - start

start = time.time()
result2 = find_common_fast(large_list1, large_list2)
time_fast = time.time() - start

print(f"\nList approach: {time_slow:.4f}s")
print(f"Set approach: {time_fast:.4f}s")
print(f"Speedup: {time_slow/time_fast:.1f}x faster")

# -----------------------------------------------------------------------------
# 3.2 Memory Considerations
# -----------------------------------------------------------------------------

import sys

# Compare memory usage
small_list = list(range(100))
small_set = set(range(100))

print(f"\nMemory comparison:")
print(f"List of 100 items: {sys.getsizeof(small_list)} bytes")
print(f"Set of 100 items: {sys.getsizeof(small_set)} bytes")
print("Note: Sets use more memory but provide O(1) operations")

# -----------------------------------------------------------------------------
# 3.3 Optimization Patterns
# -----------------------------------------------------------------------------

# Pattern 1: Pre-convert to set if multiple lookups needed
def has_duplicates_in_ranges(ranges):
    """
    Check if any number appears in multiple ranges
    ranges: [(1,5), (6,10), (3,7)]
    """
    # Bad: Check each range every time
    # for r1 in ranges:
    #     for r2 in ranges:
    #         if r1 != r2:
    #             for num in range(r1[0], r1[1]+1):
    #                 if num in range(r2[0], r2[1]+1):  # Slow!
    
    # Good: Convert ranges to sets first
    sets = [set(range(start, end+1)) for start, end in ranges]
    
    for i in range(len(sets)):
        for j in range(i+1, len(sets)):
            if sets[i] & sets[j]:  # Fast intersection!
                return True
    return False

ranges = [(1, 5), (6, 10), (3, 7)]
print(f"\nRanges {ranges} have overlap? {has_duplicates_in_ranges(ranges)}")

# Pattern 2: Use set operations instead of loops
def get_unique_items(lists):
    """Get all unique items across all lists"""
    # Bad: Loop and check
    # unique = []
    # for lst in lists:
    #     for item in lst:
    #         if item not in unique:
    #             unique.append(item)
    
    # Good: Union of all sets
    result = set()
    for lst in lists:
        result |= set(lst)
    return result

# Even better: One-liner
def get_unique_items_v2(lists):
    return set().union(*lists)

lists = [[1,2,3], [2,3,4], [3,4,5]]
print(f"Unique items: {get_unique_items(lists)}")


# ============================================================================
# PART 4: REAL-WORLD APPLICATIONS
# ============================================================================

print("\n" + "=" * 70)
print("PART 4: REAL-WORLD APPLICATIONS")
print("=" * 70)

# -----------------------------------------------------------------------------
# 4.1 Permission System
# -----------------------------------------------------------------------------

class PermissionSystem:
    """Role-based access control using sets"""
    
    def __init__(self):
        self.roles = {
            'admin': frozenset(['read', 'write', 'delete', 'execute']),
            'editor': frozenset(['read', 'write']),
            'viewer': frozenset(['read'])
        }
        self.user_roles = {}  # user: set of roles
    
    def assign_role(self, user, role):
        if user not in self.user_roles:
            self.user_roles[user] = set()
        self.user_roles[user].add(role)
    
    def get_permissions(self, user):
        """Get all permissions for user (union of role permissions)"""
        if user not in self.user_roles:
            return set()
        
        permissions = set()
        for role in self.user_roles[user]:
            permissions |= self.roles.get(role, set())
        return permissions
    
    def can_perform(self, user, action):
        """Check if user can perform action"""
        return action in self.get_permissions(user)

# Test
print("\n--- Permission System ---")
perm_system = PermissionSystem()
perm_system.assign_role('alice', 'admin')
perm_system.assign_role('bob', 'editor')
perm_system.assign_role('bob', 'viewer')  # Multiple roles

print(f"Alice's permissions: {perm_system.get_permissions('alice')}")
print(f"Bob's permissions: {perm_system.get_permissions('bob')}")
print(f"Can Bob delete? {perm_system.can_perform('bob', 'delete')}")

# -----------------------------------------------------------------------------
# 4.2 Tagging System (Blog/E-commerce)
# -----------------------------------------------------------------------------

class TaggingSystem:
    """Content tagging system using sets"""
    
    def __init__(self):
        self.items = {}  # item_id: set of tags
        self.tag_index = {}  # tag: set of item_ids
    
    def add_item(self, item_id, tags):
        """Add item with tags"""
        self.items[item_id] = set(tags)
        
        # Update reverse index
        for tag in tags:
            if tag not in self.tag_index:
                self.tag_index[tag] = set()
            self.tag_index[tag].add(item_id)
    
    def find_by_tag(self, tag):
        """Find all items with specific tag"""
        return self.tag_index.get(tag, set())
    
    def find_by_all_tags(self, tags):
        """Find items that have ALL specified tags"""
        if not tags:
            return set()
        
        result = self.tag_index.get(tags[0], set()).copy()
        for tag in tags[1:]:
            result &= self.tag_index.get(tag, set())
        return result
    
    def find_by_any_tags(self, tags):
        """Find items that have ANY of the specified tags"""
        result = set()
        for tag in tags:
            result |= self.tag_index.get(tag, set())
        return result
    
    def similar_items(self, item_id):
        """Find items with similar tags"""
        if item_id not in self.items:
            return set()
        
        item_tags = self.items[item_id]
        similar = set()
        
        for tag in item_tags:
            similar |= self.tag_index.get(tag, set())
        
        similar.discard(item_id)  # Remove itself
        return similar

# Test
print("\n--- Tagging System ---")
tagging = TaggingSystem()
tagging.add_item('post1', ['python', 'tutorial', 'beginner'])
tagging.add_item('post2', ['python', 'advanced', 'performance'])
tagging.add_item('post3', ['javascript', 'tutorial', 'beginner'])
tagging.add_item('post4', ['python', 'tutorial', 'web'])

print(f"Items with 'python': {tagging.find_by_tag('python')}")
print(f"Items with both 'python' AND 'tutorial': {tagging.find_by_all_tags(['python', 'tutorial'])}")
print(f"Similar to post1: {tagging.similar_items('post1')}")

# -----------------------------------------------------------------------------
# 4.3 Deduplication System
# -----------------------------------------------------------------------------

class DeduplicationSystem:
    """Remove duplicates from data stream"""
    
    def __init__(self):
        self.seen = set()
        self.seen_tuples = set()  # For composite keys
    
    def is_duplicate(self, item):
        """Check if item seen before (hashable items)"""
        if item in self.seen:
            return True
        self.seen.add(item)
        return False
    
    def is_duplicate_composite(self, *fields):
        """Check duplicate using multiple fields"""
        key = tuple(fields)
        if key in self.seen_tuples:
            return True
        self.seen_tuples.add(key)
        return False
    
    def process_stream(self, items):
        """Process stream and return unique items"""
        unique = []
        for item in items:
            if not self.is_duplicate(item):
                unique.append(item)
        return unique

# Test
print("\n--- Deduplication System ---")
dedup = DeduplicationSystem()
stream = [1, 2, 3, 2, 4, 3, 5, 1, 6]
unique = dedup.process_stream(stream)
print(f"Stream: {stream}")
print(f"Unique: {unique}")

# For database records
class Record:
    def __init__(self, user_id, action, timestamp):
        self.user_id = user_id
        self.action = action
        self.timestamp = timestamp

records = [
    Record(1, 'login', 100),
    Record(2, 'logout', 101),
    Record(1, 'login', 100),  # Duplicate
    Record(1, 'logout', 102),
]

dedup2 = DeduplicationSystem()
for record in records:
    is_dup = dedup2.is_duplicate_composite(
        record.user_id, record.action, record.timestamp
    )
    if not is_dup:
        print(f"New record: user={record.user_id}, action={record.action}")

# -----------------------------------------------------------------------------
# 4.4 Cache with Set-based Eviction
# -----------------------------------------------------------------------------

class LRUCacheWithSet:
    """
    LRU Cache using set for O(1) key checking
    Demonstrates practical use of tuples and sets together
    """
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}  # key: (value, timestamp)
        self.keys = set()  # Fast key existence check
        self.access_count = 0
    
    def get(self, key):
        if key not in self.keys:
            return None
        
        value, _ = self.cache[key]
        # Update access time
        self.access_count += 1
        self.cache[key] = (value, self.access_count)
        return value
    
    def put(self, key, value):
        self.access_count += 1
        
        # If key exists, just update
        if key in self.keys:
            self.cache[key] = (value, self.access_count)
            return
        
        # If at capacity, evict LRU
        if len(self.keys) >= self.capacity:
            lru_key = min(self.cache.keys(), 
                         key=lambda k: self.cache[k][1])
            del self.cache[lru_key]
            self.keys.remove(lru_key)
        
        # Add new item
        self.cache[key] = (value, self.access_count)
        self.keys.add(key)
    
    def contains(self, key):
        """O(1) check if key exists"""
        return key in self.keys

# Test
print("\n--- LRU Cache with Set ---")
cache = LRUCacheWithSet(capacity=3)
cache.put('a', 1)
cache.put('b', 2)
cache.put('c', 3)
print(f"Cache contains 'b': {cache.contains('b')}")
cache.put('d', 4)  # Evicts 'a' (LRU)
print(f"Cache contains 'a': {cache.contains('a')}")  # False


# ============================================================================
# PART 5: ADVANCED PATTERNS AND TRICKS
# ============================================================================

print("\n" + "=" * 70)
print("PART 5: ADVANCED PATTERNS AND TRICKS")
print("=" * 70)

# -----------------------------------------------------------------------------
# 5.1 Set Algebra for Problem Solving
# -----------------------------------------------------------------------------

def find_missing_and_duplicate(nums, n):
    """
    Array should contain 1 to n, but one number is duplicated
    and one is missing. Find both.
    
    Example: nums = [1,2,2,4], n = 4
    Missing: 3, Duplicate: 2
    """
    expected = set(range(1, n + 1))
    actual = set(nums)
    
    missing = expected - actual
    duplicate = set([x for x in nums if nums.count(x) > 1])
    
    return list(missing)[0] if missing else None, \
           list(duplicate)[0] if duplicate else None

nums = [1, 2, 2, 4]
missing, duplicate = find_missing_and_duplicate(nums, 4)
print(f"\nArray {nums}: missing={missing}, duplicate={duplicate}")

# -----------------------------------------------------------------------------
# 5.2 Cartesian Product with Sets
# -----------------------------------------------------------------------------

def cartesian_product_sets(set1, set2):
    """Generate all pairs from two sets"""
    return {(a, b) for a in set1 for b in set2}

colors = {'red', 'blue'}
sizes = {'small', 'large'}
products = cartesian_product_sets(colors, sizes)
print(f"\nProduct variants: {products}")

# -----------------------------------------------------------------------------
# 5.3 Power Set (All Subsets)
# -----------------------------------------------------------------------------

def power_set(s):
    """
    Generate all subsets of a set
    Uses frozenset for hashable subsets
    """
    s = list(s)
    result = set()
    n = len(s)
    
    # Generate all 2^n subsets
    for i in range(2 ** n):
        subset = frozenset([s[j] for j in range(n) if (i >> j) & 1])
        result.add(subset)
    
    return result

original = {1, 2, 3}
subsets = power_set(original)
print(f"\nPower set of {original}:")
for subset in sorted(subsets, key=len):
    print(f"  {set(subset)}")

# -----------------------------------------------------------------------------
# 5.4 Symmetric Difference for Change Detection
# -----------------------------------------------------------------------------

def detect_changes(old_state, new_state):
    """
    Detect what was added and removed
    Returns (added, removed)
    """
    old = set(old_state)
    new = set(new_state)
    
    added = new - old
    removed = old - new
    
    return added, removed

old_users = ['alice', 'bob', 'charlie']
new_users = ['bob', 'charlie', 'david', 'eve']

added, removed = detect_changes(old_users, new_users)
print(f"\nUser changes:")
print(f"  Added: {added}")
print(f"  Removed: {removed}")

# -----------------------------------------------------------------------------
# 5.5 Bloom Filter (Probabilistic Set)
# -----------------------------------------------------------------------------

class SimpleBloomFilter:
    """
    Space-efficient probabilistic set
    May have false positives but NO false negatives
    """
    def __init__(self, size=100):
        self.size = size
        self.bits = set()  # In real implementation, use bit array
    
    def _hash(self, item):
        """Simple hash functions"""
        h1 = hash(item) % self.size
        h2 = hash(str(item) + "salt") % self.size
        return [h1, h2]
    
    def add(self, item):
        """Add item to bloom filter"""
        for h in self._hash(item):
            self.bits.add(h)
    
    def might_contain(self, item):
        """Check if item might be in set"""
        return all(h in self.bits for h in self._hash(item))

# Test
print("\n--- Bloom Filter ---")
bloom = SimpleBloomFilter()
bloom.add("alice")
bloom.add("bob")

print(f"Might contain 'alice': {bloom.might_contain('alice')}")
print(f"Might contain 'charlie': {bloom.might_contain('charlie')}")
print("Note: May have false positives in real implementation")

print("\n" + "=" * 70)
print("END OF ADVANCED TOPICS")
print("=" * 70)

print("\nKey Takeaways:")
print("1. Frozensets for immutable sets (dict keys, set elements)")
print("2. Set comprehensions for concise set creation")
print("3. Convert to sets for repeated membership tests")
print("4. Use set operations (union, intersection) instead of loops")
print("5. Sets trade memory for speed - choose wisely")
print("6. Real-world: permissions, tags, deduplication, caching")