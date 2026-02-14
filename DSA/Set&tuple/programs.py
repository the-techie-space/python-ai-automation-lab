"""
SET AND TUPLE - INTERVIEW PROBLEMS
===================================

Problems organized by difficulty:
- Easy: Fundamental concepts
- Medium: Combining techniques
- Hard: Complex algorithms

Each problem includes:
- Problem statement
- Examples
- Hints
- Solution with explanation
- Time/Space complexity

Author: DSA Learning
"""

# ============================================================================
# EASY LEVEL PROBLEMS
# ============================================================================

print("=" * 70)
print("EASY LEVEL PROBLEMS")
print("=" * 70)

# -----------------------------------------------------------------------------
# Problem 1: Contains Duplicate
# -----------------------------------------------------------------------------

def contains_duplicate(nums):
    """
    Return True if any value appears at least twice in the array.
    
    Examples:
        contains_duplicate([1, 2, 3, 1]) → True
        contains_duplicate([1, 2, 3, 4]) → False
        contains_duplicate([1,1,1,3,3,4,3,2,4,2]) → True
    
    Hint: Use a set to track seen numbers
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# Alternative one-liner
def contains_duplicate_oneliner(nums):
    """Compare length of list vs set"""
    return len(nums) != len(set(nums))

# Test
print("\nProblem 1: Contains Duplicate")
print(f"[1,2,3,1]: {contains_duplicate([1,2,3,1])}")  # True
print(f"[1,2,3,4]: {contains_duplicate([1,2,3,4])}")  # False

# -----------------------------------------------------------------------------
# Problem 2: Intersection of Two Arrays
# -----------------------------------------------------------------------------

def intersection(nums1, nums2):
    """
    Find the intersection of two arrays (unique elements present in both).
    
    Examples:
        intersection([1,2,2,1], [2,2]) → [2]
        intersection([4,9,5], [9,4,9,8,4]) → [4,9] or [9,4]
    
    Hint: Convert both to sets and use & operator
    
    Time Complexity: O(n + m)
    Space Complexity: O(n + m)
    """
    return list(set(nums1) & set(nums2))

# Alternative using intersection method
def intersection_v2(nums1, nums2):
    return list(set(nums1).intersection(set(nums2)))

# Test
print("\nProblem 2: Intersection of Two Arrays")
print(f"[1,2,2,1] ∩ [2,2]: {intersection([1,2,2,1], [2,2])}")
print(f"[4,9,5] ∩ [9,4,9,8,4]: {intersection([4,9,5], [9,4,9,8,4])}")

# -----------------------------------------------------------------------------
# Problem 3: Valid Anagram
# -----------------------------------------------------------------------------

def is_anagram(s, t):
    """
    Check if two strings are anagrams (same letters, different order).
    
    Examples:
        is_anagram("anagram", "nagaram") → True
        is_anagram("rat", "car") → False
    
    Hint: Compare sorted tuples or character frequency
    
    Time Complexity: O(n log n) for sorting
    Space Complexity: O(n)
    """
    # Method 1: Sort and compare
    return sorted(s) == sorted(t)

def is_anagram_v2(s, t):
    """Using character frequency with Counter"""
    from collections import Counter
    return Counter(s) == Counter(t)

def is_anagram_v3(s, t):
    """Using sets - check same chars and same length"""
    if len(s) != len(t):
        return False
    # This approach needs frequency check too
    from collections import Counter
    return Counter(s) == Counter(t)

# Test
print("\nProblem 3: Valid Anagram")
print(f"'anagram' & 'nagaram': {is_anagram('anagram', 'nagaram')}")
print(f"'rat' & 'car': {is_anagram('rat', 'car')}")

# -----------------------------------------------------------------------------
# Problem 4: Happy Number
# -----------------------------------------------------------------------------

def is_happy(n):
    """
    A happy number is defined by the following process:
    - Starting with any positive integer, replace the number by the sum 
      of the squares of its digits.
    - Repeat until the number equals 1 (happy) or loops endlessly (not happy).
    
    Examples:
        is_happy(19) → True
        1^2 + 9^2 = 82
        8^2 + 2^2 = 68
        6^2 + 8^2 = 100
        1^2 + 0^2 + 0^2 = 1 ✓
        
        is_happy(2) → False (loops forever)
    
    Hint: Use set to detect cycles
    
    Time Complexity: O(log n)
    Space Complexity: O(log n)
    """
    def get_next(num):
        total_sum = 0
        while num > 0:
            digit = num % 10
            total_sum += digit ** 2
            num //= 10
        return total_sum
    
    seen = set()
    while n != 1 and n not in seen:
        seen.add(n)
        n = get_next(n)
    
    return n == 1

# Test
print("\nProblem 4: Happy Number")
print(f"19 is happy? {is_happy(19)}")  # True
print(f"2 is happy? {is_happy(2)}")    # False

# -----------------------------------------------------------------------------
# Problem 5: Single Number
# -----------------------------------------------------------------------------

def single_number(nums):
    """
    Given array where every element appears twice except one, find that one.
    
    Examples:
        single_number([2,2,1]) → 1
        single_number([4,1,2,1,2]) → 4
        single_number([1]) → 1
    
    Hint: Use XOR (^) property: a ^ a = 0, a ^ 0 = a
    Or use set operations
    
    Time Complexity: O(n)
    Space Complexity: O(1) for XOR, O(n) for set
    """
    # Method 1: XOR (most efficient)
    result = 0
    for num in nums:
        result ^= num
    return result

def single_number_set(nums):
    """Method 2: Using sets"""
    return 2 * sum(set(nums)) - sum(nums)

# Test
print("\nProblem 5: Single Number")
print(f"[2,2,1]: {single_number([2,2,1])}")
print(f"[4,1,2,1,2]: {single_number([4,1,2,1,2])}")


# ============================================================================
# MEDIUM LEVEL PROBLEMS
# ============================================================================

print("\n" + "=" * 70)
print("MEDIUM LEVEL PROBLEMS")
print("=" * 70)

# -----------------------------------------------------------------------------
# Problem 6: Group Anagrams
# -----------------------------------------------------------------------------

def group_anagrams(strs):
    """
    Group strings that are anagrams of each other.
    
    Examples:
        group_anagrams(["eat","tea","tan","ate","nat","bat"])
        → [["bat"],["nat","tan"],["ate","eat","tea"]]
    
    Hint: Use sorted tuple as dictionary key
    
    Time Complexity: O(n * k log k) where k is max string length
    Space Complexity: O(n * k)
    """
    from collections import defaultdict
    
    groups = defaultdict(list)
    for word in strs:
        # Sorted tuple as key
        key = tuple(sorted(word))
        groups[key].append(word)
    
    return list(groups.values())

# Test
print("\nProblem 6: Group Anagrams")
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(f"Input: {words}")
print(f"Output: {group_anagrams(words)}")

# -----------------------------------------------------------------------------
# Problem 7: Longest Consecutive Sequence
# -----------------------------------------------------------------------------

def longest_consecutive(nums):
    """
    Find the length of the longest consecutive elements sequence.
    
    Examples:
        longest_consecutive([100,4,200,1,3,2]) → 4
        Explanation: [1,2,3,4] is the longest consecutive sequence
        
        longest_consecutive([0,3,7,2,5,8,4,6,0,1]) → 9
    
    Hint: Use set for O(1) lookup, only start counting from sequence start
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    if not nums:
        return 0
    
    num_set = set(nums)
    max_length = 0
    
    for num in num_set:
        # Only start if it's the beginning of a sequence
        if num - 1 not in num_set:
            current_num = num
            current_length = 1
            
            # Count consecutive numbers
            while current_num + 1 in num_set:
                current_num += 1
                current_length += 1
            
            max_length = max(max_length, current_length)
    
    return max_length

# Test
print("\nProblem 7: Longest Consecutive Sequence")
print(f"[100,4,200,1,3,2]: {longest_consecutive([100,4,200,1,3,2])}")
print(f"[0,3,7,2,5,8,4,6,0,1]: {longest_consecutive([0,3,7,2,5,8,4,6,0,1])}")

# -----------------------------------------------------------------------------
# Problem 8: Contains Duplicate II
# -----------------------------------------------------------------------------

def contains_nearby_duplicate(nums, k):
    """
    Return true if there are two distinct indices i and j such that
    nums[i] == nums[j] and abs(i - j) <= k.
    
    Examples:
        contains_nearby_duplicate([1,2,3,1], 3) → True
        contains_nearby_duplicate([1,0,1,1], 1) → True
        contains_nearby_duplicate([1,2,3,1,2,3], 2) → False
    
    Hint: Use dict to store last seen index of each number
    
    Time Complexity: O(n)
    Space Complexity: O(min(n, k))
    """
    last_seen = {}
    
    for i, num in enumerate(nums):
        if num in last_seen and i - last_seen[num] <= k:
            return True
        last_seen[num] = i
    
    return False

# Alternative: Using sliding window with set
def contains_nearby_duplicate_v2(nums, k):
    window = set()
    
    for i, num in enumerate(nums):
        if num in window:
            return True
        window.add(num)
        if len(window) > k:
            window.remove(nums[i - k])
    
    return False

# Test
print("\nProblem 8: Contains Duplicate II")
print(f"[1,2,3,1], k=3: {contains_nearby_duplicate([1,2,3,1], 3)}")
print(f"[1,0,1,1], k=1: {contains_nearby_duplicate([1,0,1,1], 1)}")

# -----------------------------------------------------------------------------
# Problem 9: Intersection of Multiple Arrays
# -----------------------------------------------------------------------------

def arrays_intersection(arrays):
    """
    Find elements that appear in all arrays.
    
    Examples:
        arrays_intersection([[1,2,3],[2,3,4],[3,4,5]]) → [3]
        arrays_intersection([[1,2,3,4],[2,3,4,5],[3,4,5,6]]) → [3,4]
    
    Hint: Start with first array as set, intersect with others
    
    Time Complexity: O(n * m) where n is number of arrays, m is avg length
    Space Complexity: O(m)
    """
    if not arrays:
        return []
    
    result = set(arrays[0])
    for arr in arrays[1:]:
        result &= set(arr)
    
    return sorted(list(result))

# Test
print("\nProblem 9: Intersection of Multiple Arrays")
arrays = [[1,2,3], [2,3,4], [3,4,5]]
print(f"Input: {arrays}")
print(f"Output: {arrays_intersection(arrays)}")

# -----------------------------------------------------------------------------
# Problem 10: Find All Duplicates in Array
# -----------------------------------------------------------------------------

def find_duplicates(nums):
    """
    Given array of integers where 1 ≤ a[i] ≤ n (n = size of array),
    some elements appear twice and others appear once.
    Find all elements that appear twice.
    
    Examples:
        find_duplicates([4,3,2,7,8,2,3,1]) → [2,3]
        find_duplicates([1,1,2]) → [1]
    
    Hint: Use set to track seen numbers
    
    Time Complexity: O(n)
    Space Complexity: O(n)
    """
    seen = set()
    duplicates = set()
    
    for num in nums:
        if num in seen:
            duplicates.add(num)
        else:
            seen.add(num)
    
    return list(duplicates)

# Test
print("\nProblem 10: Find All Duplicates")
print(f"[4,3,2,7,8,2,3,1]: {find_duplicates([4,3,2,7,8,2,3,1])}")


# ============================================================================
# HARD LEVEL PROBLEMS
# ============================================================================

print("\n" + "=" * 70)
print("HARD LEVEL PROBLEMS")
print("=" * 70)

# -----------------------------------------------------------------------------
# Problem 11: Longest Substring Without Repeating Characters
# -----------------------------------------------------------------------------

def length_of_longest_substring(s):
    """
    Find the length of the longest substring without repeating characters.
    
    Examples:
        length_of_longest_substring("abcabcbb") → 3 ("abc")
        length_of_longest_substring("bbbbb") → 1 ("b")
        length_of_longest_substring("pwwkew") → 3 ("wke")
    
    Hint: Use sliding window with set to track characters in current window
    
    Time Complexity: O(n)
    Space Complexity: O(min(m, n)) where m is charset size
    """
    char_set = set()
    left = 0
    max_length = 0
    
    for right in range(len(s)):
        # Shrink window until no duplicates
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        
        char_set.add(s[right])
        max_length = max(max_length, right - left + 1)
    
    return max_length

# Test
print("\nProblem 11: Longest Substring Without Repeating Characters")
print(f"'abcabcbb': {length_of_longest_substring('abcabcbb')}")
print(f"'bbbbb': {length_of_longest_substring('bbbbb')}")
print(f"'pwwkew': {length_of_longest_substring('pwwkew')}")

# -----------------------------------------------------------------------------
# Problem 12: Valid Sudoku
# -----------------------------------------------------------------------------

def is_valid_sudoku(board):
    """
    Determine if a 9x9 Sudoku board is valid.
    
    Rules:
    - Each row must contain digits 1-9 without repetition
    - Each column must contain digits 1-9 without repetition
    - Each 3x3 sub-box must contain digits 1-9 without repetition
    - Empty cells are marked with '.'
    
    Hint: Use sets to track seen numbers in rows, cols, and boxes
    
    Time Complexity: O(1) - board is always 9x9
    Space Complexity: O(1) - fixed size sets
    """
    # Sets for rows, columns, and 3x3 boxes
    rows = [set() for _ in range(9)]
    cols = [set() for _ in range(9)]
    boxes = [set() for _ in range(9)]
    
    for i in range(9):
        for j in range(9):
            num = board[i][j]
            
            if num == '.':
                continue
            
            # Calculate box index
            box_index = (i // 3) * 3 + (j // 3)
            
            # Check if number already exists
            if num in rows[i] or num in cols[j] or num in boxes[box_index]:
                return False
            
            # Add to sets
            rows[i].add(num)
            cols[j].add(num)
            boxes[box_index].add(num)
    
    return True

# Test
print("\nProblem 12: Valid Sudoku")
board = [
    ["5","3",".",".","7",".",".",".","."],
    ["6",".",".","1","9","5",".",".","."],
    [".","9","8",".",".",".",".","6","."],
    ["8",".",".",".","6",".",".",".","3"],
    ["4",".",".","8",".","3",".",".","1"],
    ["7",".",".",".","2",".",".",".","6"],
    [".","6",".",".",".",".","2","8","."],
    [".",".",".","4","1","9",".",".","5"],
    [".",".",".",".","8",".",".","7","9"]
]
print(f"Board is valid: {is_valid_sudoku(board)}")

# -----------------------------------------------------------------------------
# Problem 13: Word Pattern II (Backtracking with Sets)
# -----------------------------------------------------------------------------

def word_pattern_match(pattern, s):
    """
    Given pattern and string s, check if s follows the same pattern.
    
    Examples:
        word_pattern_match("abab", "redblueredblue") → True
        word_pattern_match("aaaa", "asdasdasdasd") → True
        word_pattern_match("aabb", "xyzabcxzyabc") → False
    
    Hint: Use backtracking with sets to track used mappings
    
    Time Complexity: O(n^m) where n is length of s, m is length of pattern
    Space Complexity: O(m)
    """
    def backtrack(pattern_idx, s_idx, mapping, used_words):
        # Base case: both exhausted
        if pattern_idx == len(pattern) and s_idx == len(s):
            return True
        
        # One exhausted but not the other
        if pattern_idx == len(pattern) or s_idx == len(s):
            return False
        
        char = pattern[pattern_idx]
        
        # If character already mapped
        if char in mapping:
            word = mapping[char]
            # Check if word matches at current position
            if s[s_idx:s_idx + len(word)] == word:
                return backtrack(pattern_idx + 1, s_idx + len(word), 
                               mapping, used_words)
            return False
        
        # Try all possible words
        for end in range(s_idx + 1, len(s) + 1):
            word = s[s_idx:end]
            
            # Skip if word already used for different character
            if word in used_words:
                continue
            
            # Try this mapping
            mapping[char] = word
            used_words.add(word)
            
            if backtrack(pattern_idx + 1, end, mapping, used_words):
                return True
            
            # Backtrack
            del mapping[char]
            used_words.remove(word)
        
        return False
    
    return backtrack(0, 0, {}, set())

# Test
print("\nProblem 13: Word Pattern II")
print(f"'abab' & 'redblueredblue': {word_pattern_match('abab', 'redblueredblue')}")
print(f"'aabb' & 'xyzabcxzyabc': {word_pattern_match('aabb', 'xyzabcxzyabc')}")

# -----------------------------------------------------------------------------
# Problem 14: Tuple as Keys - LRU Cache Coordinate System
# -----------------------------------------------------------------------------

class CoordinateCache:
    """
    Cache system using tuples as keys for coordinates
    Demonstrates practical use of tuples as dictionary keys
    """
    def __init__(self):
        self.cache = {}
    
    def set_value(self, x, y, value):
        """Store value at coordinate (x, y)"""
        self.cache[(x, y)] = value
    
    def get_value(self, x, y):
        """Retrieve value at coordinate (x, y)"""
        return self.cache.get((x, y), None)
    
    def get_neighbors(self, x, y):
        """Get all neighboring coordinates that have values"""
        neighbors = []
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        
        for dx, dy in directions:
            coord = (x + dx, y + dy)
            if coord in self.cache:
                neighbors.append((coord, self.cache[coord]))
        
        return neighbors

# Test
print("\nProblem 14: Coordinate Cache with Tuples")
cache = CoordinateCache()
cache.set_value(0, 0, "Origin")
cache.set_value(1, 0, "East")
cache.set_value(0, 1, "North")
print(f"Value at (0,0): {cache.get_value(0, 0)}")
print(f"Neighbors of (0,0): {cache.get_neighbors(0, 0)}")

# -----------------------------------------------------------------------------
# Problem 15: Set Operations - Social Network
# -----------------------------------------------------------------------------

class SocialNetwork:
    """
    Demonstrate practical use of set operations in social network
    """
    def __init__(self):
        self.friendships = {}
    
    def add_friendship(self, person1, person2):
        """Add bidirectional friendship"""
        if person1 not in self.friendships:
            self.friendships[person1] = set()
        if person2 not in self.friendships:
            self.friendships[person2] = set()
        
        self.friendships[person1].add(person2)
        self.friendships[person2].add(person1)
    
    def mutual_friends(self, person1, person2):
        """Find common friends"""
        if person1 not in self.friendships or person2 not in self.friendships:
            return set()
        return self.friendships[person1] & self.friendships[person2]
    
    def friend_suggestions(self, person):
        """Suggest friends (friends of friends who aren't already friends)"""
        if person not in self.friendships:
            return set()
        
        friends = self.friendships[person]
        suggestions = set()
        
        # Friends of friends
        for friend in friends:
            suggestions |= self.friendships.get(friend, set())
        
        # Remove person and existing friends
        suggestions -= friends
        suggestions.discard(person)
        
        return suggestions

# Test
print("\nProblem 15: Social Network with Sets")
network = SocialNetwork()
network.add_friendship("Alice", "Bob")
network.add_friendship("Alice", "Charlie")
network.add_friendship("Bob", "Charlie")
network.add_friendship("Bob", "David")
network.add_friendship("Charlie", "David")

print(f"Alice's friends: {network.friendships['Alice']}")
print(f"Mutual friends of Alice & Bob: {network.mutual_friends('Alice', 'Bob')}")
print(f"Friend suggestions for Alice: {network.friend_suggestions('Alice')}")

print("\n" + "=" * 70)
print("END OF PROBLEMS")
print("=" * 70)
print("\nKey Takeaways:")
print("1. Sets provide O(1) membership testing - use them!")
print("2. Tuples are immutable and can be dict keys")
print("3. Set operations (union, intersection) are powerful")
print("4. Combine with other techniques (sliding window, backtracking)")
print("5. Practice recognizing when to use sets vs lists vs dicts")