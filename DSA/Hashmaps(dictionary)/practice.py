# Part 1: What is a Hash Map? 🤔
# Real-World Analogy
# Imagine a library:


# Bad System (Array/List):
# Books stored by order they arrived:
# Book 1: "Python Basics"
# Book 2: "Java Guide"
# Book 3: "DSA Master"
# ...
# Book 1000: "AI Handbook"

# To find "AI Handbook" → Check all 1000 books! O(n) 😢

# Good System (Hash Map/Dictionary):

# Books organized by unique ID:
# ID "PY001" → "Python Basics"
# ID "JV002" → "Java Guide"
# ID "DS003" → "DSA Master"
# ...
# ID "AI999" → "AI Handbook"

# To find book with ID "AI999" → Direct access! O(1) 🚀

# What is a Hash Map?
# A Hash Map (called Dictionary in Python) stores data in key-value pairs for instant lookup.

# Dictionary syntax in Python
student = {
    "name": "Alice",      # key: "name",  value: "Alice"
    "age": 20,            # key: "age",   value: 20
    "grade": "A"          # key: "grade", value: "A"
}

# Access by key - O(1) time!
print(student["name"])  # "Alice" - INSTANT!

# Key concept:

# Key = Unique identifier (like a label)
# Value = The data you want to store
# Access = Use key to get value instantly

# Part 2: Dictionary Basics in Python 📖
# Creating Dictionaries

# Method 1: Using curly braces
empty_dict = {}
person = {"name": "Bob", "age": 25}

# Method 2: Using dict() function
empty_dict = dict()
person = dict(name="Bob", age=25)

# Method 3: From lists
keys = ["a", "b", "c"]
values = [1, 2, 3]
my_dict = dict(zip(keys, values))
print(my_dict)  # {'a': 1, 'b': 2, 'c': 3}

# Basic Operations (MUST KNOW)

# 1. CREATE
student = {"name": "Alice", "age": 20, "major": "CS"}

# 2. ACCESS (Get value by key)
print(student["name"])        # "Alice"
print(student.get("age"))     # 20
print(student.get("grade"))   # None (key doesn't exist, no error!)

# 3. ADD / UPDATE
student["grade"] = "A"        # Add new key-value
student["age"] = 21           # Update existing value
print(student)
# {'name': 'Alice', 'age': 21, 'major': 'CS', 'grade': 'A'}

# 4. DELETE
del student["major"]          # Remove key-value pair
removed = student.pop("grade")  # Remove and return value
print(student)  # {'name': 'Alice', 'age': 21}

# 5. CHECK if key exists
if "name" in student:
    print("Name exists!")

# 6. GET all keys/values
print(student.keys())    # dict_keys(['name', 'age'])
print(student.values())  # dict_values(['Alice', 21])
print(student.items())   # dict_items([('name', 'Alice'), ('age', 21)])

# 7. LENGTH
print(len(student))  # 2

# Common Gotcha: .get() vs [ ]

student = {"name": "Alice", "age": 20}

# Using [ ] - CRASHES if key doesn't exist
# print(student["grade"])  # ❌ KeyError!

# Using .get() - Returns None if key doesn't exist
print(student.get("grade"))        # None (safe!)
print(student.get("grade", "N/A")) # "N/A" (default value)

# BEST PRACTICE: Use .get() when key might not exist

# Part 3: Why Hash Maps Are O(1)? ⚡
# The Magic of Hashing
# How does Python find values instantly?


student = {"name": "Alice", "age": 20}

# When you do: student["name"]
# Behind the scenes:
# 1. Python calculates hash("name") → number (e.g., 12345)
# 2. Uses that number to find exact memory location
# 3. Retrieves value directly - NO SEARCHING!

# Comparison:

# ARRAY/LIST - Must search O(n)
students = [
    {"name": "Alice", "id": 1},
    {"name": "Bob", "id": 2},
    # ... 1000 more students
]
# Finding student with id=500 → check 500 items!

# HASH MAP - Direct access O(1)
students = {
    1: {"name": "Alice"},
    2: {"name": "Bob"},
    # ... 1000 more students
}
# Finding student with id=500 → INSTANT!
print(students[500])


# Part 4: Common Patterns - Pattern 1: Counting 📊
# Problem: Count how many times each element appears.
# Example: Count Frequency of Characters

def count_characters(s):
    """
    Count frequency of each character
    Input: "hello"
    Output: {'h': 1, 'e': 1, 'l': 2, 'o': 1}
    """
    count = {}
    
    for char in s:
        # Method 1: Using if-else
        if char in count:
            count[char] += 1
        else:
            count[char] = 1
    
    return count

# Test
result = count_characters("hello")
print(result)  # {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# Better way using .get():

def count_characters(s):
    count = {}
    
    for char in s:
        # .get(char, 0) returns 0 if char not in dict
        count[char] = count.get(char, 0) + 1
    
    return count

print(count_characters("hello"))

# Even Better - Using defaultdict:

from collections import defaultdict

def count_characters(s):
    count = defaultdict(int)  # Default value is 0
    
    for char in s:
        count[char] += 1  # No need to check if exists!
    
    return dict(count)

print(count_characters("hello"))

# Best - Using Counter (built-in!):

from collections import Counter

def count_characters(s):
    return dict(Counter(s))

print(count_characters("hello"))
# {'h': 1, 'e': 1, 'l': 2, 'o': 1}

# Practice: Count Word Frequency

def count_words(text):
    """
    Count how many times each word appears
    Input: "hello world hello"
    Output: {'hello': 2, 'world': 1}
    """
    count = {}
    words = text.split()  # Split by spaces
    
    for word in words:
        count[word] = count.get(word, 0) + 1
    
    return count

# Test
sentence = "apple banana apple orange banana apple"
print(count_words(sentence))
# {'apple': 3, 'banana': 2, 'orange': 1}

# Part 5: Pattern 2 - Finding Duplicates 🔍
# Problem 1: Find First Duplicate

def first_duplicate(nums):
    """
    Find the first number that appears twice
    Input: [2, 1, 3, 5, 3, 2]
    Output: 3 (first duplicate)
    
    Time: O(n), Space: O(n)
    """
    seen = {}  # or set()
    
    for num in nums:
        if num in seen:
            return num  # Found duplicate!
        seen[num] = True  # Mark as seen
    
    return None  # No duplicate

# Test
print(first_duplicate([2, 1, 3, 5, 3, 2]))  # 3
print(first_duplicate([1, 2, 3, 4]))        # None

# Using Set (simpler for this case):

def first_duplicate(nums):
    seen = set()
    
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    
    return None


# Problem 2: Find All Duplicates

def find_duplicates(nums):
    """
    Find all numbers that appear more than once
    Input: [1, 2, 3, 2, 4, 3, 5]
    Output: [2, 3]
    """
    count = {}
    duplicates = []
    
    # Count occurrences
    for num in nums:
        count[num] = count.get(num, 0) + 1
    
    # Find numbers with count > 1
    for num, freq in count.items():
        if freq > 1:
            duplicates.append(num)
    
    return duplicates

# Test
print(find_duplicates([1, 2, 3, 2, 4, 3, 5]))  # [2, 3]
# ```

# ---

# ## **Part 6: THE Most Important Problem - Two Sum** ⭐⭐⭐

# **This is the #1 most asked interview question!**

# ### **Problem Statement**
# ```
# Given an array of numbers and a target, find two numbers that add up to target.
# Return their indices.

# Example:
# Input: nums = [2, 7, 11, 15], target = 9
# Output: [0, 1]
# Explanation: nums[0] + nums[1] = 2 + 7 = 9


# ✅ Hash Map Solution - O(n) 🚀

def two_sum(nums, target):
    """
    Use hash map to find complement
    Time: O(n) - FAST!
    Space: O(n)
    """
    seen = {}  # num → index
    
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if complement exists
        if complement in seen:
            return [seen[complement], i]
        
        # Store current number and its index
        seen[num] = i
    
    return None

# Test
print(two_sum([2, 7, 11, 15], 9))     # [0, 1]
print(two_sum([3, 2, 4], 6))          # [1, 2]
print(two_sum([3, 3], 6))             # [0, 1]


# Part 7: Your Practice Problems 💪
# Problem 1: Contains Duplicate (Easy)

def contains_duplicate(nums):
    """
    Return True if any value appears at least twice
    
    Input: [1, 2, 3, 1]
    Output: True
    
    Input: [1, 2, 3, 4]
    Output: False
    
    Hint: Use a set or dict to track seen numbers
    """
        # freq_dict = {}

    # for i in nums:
    #     freq_dict[i] = freq_dict.get(i, 0) + 1

    # for _, value in freq_dict.items():
    #     if value > 1:
    #         return True
    # return False

    #or
    freq_dict = {}

    for num in nums:
        if num in freq_dict:
            return True
        freq_dict[num] = 1
    return False


# Test
print(contains_duplicate([1, 2, 3, 1]))      # True
print(contains_duplicate([1, 2, 3, 4]))      # False
print(contains_duplicate([1,1,1,3,3,4,3,2,4,2]))  # True

# using set()
#Method 2: Using Set (Most Efficient for this problem)

def contains_duplicate(nums):
    """
    Time: O(n), Space: O(n)
    Simplest approach!
    """
    seen = set()
    
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    
    return False

# Test
print(contains_duplicate([1, 2, 3, 1]))      # True


# Method 3: One-liner (Pythonic but less efficient)

def contains_duplicate(nums):
    """
    Compare length of list vs set
    If duplicate exists, set will be smaller!
    """
    return len(nums) != len(set(nums))

# Test
print(contains_duplicate([1, 2, 3, 1]))      # True

# Problem 2: First Unique Character (Easy-Medium)

def first_unique_char(s):
    """
    Find the first non-repeating character in a string
    Return its index. If doesn't exist, return -1
    
    Input: "leetcode"
    Output: 0 (because 'l' appears only once)
    
    Input: "loveleetcode"
    Output: 2 (because 'v' is first unique)
    
    Input: "aabb"
    Output: -1
    
    Hint: 
    1. Count frequency of each character
    2. Loop through string again to find first with count=1
    """
    freq_dict = {}

    for ch in s:
        freq_dict[ch] = freq_dict.get(ch, 0) + 1

    for index, char in enumerate(s):
        if freq_dict[char] == 1:
            return index
    return -1
    
# Test
print(first_unique_char("leetcode"))       # 0
print(first_unique_char("loveleetcode"))   # 2
print(first_unique_char("aabb"))           # -1

from collections import Counter

def first_unique_char(s):
    """
    Using Counter for cleaner code
    """
    freq = Counter(s)
    
    for i, char in enumerate(s):
        if freq[char] == 1:
            return i
    
    return -1

# Test
print(first_unique_char("leetcode"))       # 0
print(first_unique_char("loveleetcode"))   # 2
print(first_unique_char("aabb"))           # -1


# Problem 3: Group Anagrams (Medium) ⭐

def group_anagrams(strs):
    """
    Group strings that are anagrams of each other
    
    Input: ["eat", "tea", "tan", "ate", "nat", "bat"]
    Output: [["eat","tea","ate"], ["tan","nat"], ["bat"]]
    
    Hint: Use sorted string as key!
    "eat" → sorted → "aet"
    "tea" → sorted → "aet"  (same key!)
    "ate" → sorted → "aet"  (same key!)
    """
    groups = {}

    for word in strs:
        key = "".join(sorted(word))

        if key in groups:
            groups[key].append(key)
        else:
            groups[key] = [word]

    return list(groups.values())


# Test
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(group_anagrams(words))

def group_anagrams(strs):
    """
    Time: O(n * k log k) where n=number of words, k=max word length
    Space: O(n * k)
    """
    from collections import defaultdict
    
    # Dictionary: sorted_word → list of original words
    groups = defaultdict(list)
    
    for word in strs:
        # Sort the word to get the key
        key = ''.join(sorted(word))
        
        # Add original word to the group
        groups[key].append(word)
    
    # Return all groups as a list
    return list(groups.values())


# Test
words = ["eat", "tea", "tan", "ate", "nat", "bat"]
result = group_anagrams(words)
print(result)
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

def group_by_digit_sum(nums):
    """
    Group numbers with same digit sum
    
    Input: [12, 21, 30, 11, 102]
    Output: [[12, 21, 30], [11, 102]]
    
    Explanation:
    12 → 1+2=3
    21 → 2+1=3  (same as 12!)
    30 → 3+0=3  (same as 12!)
    11 → 1+1=2
    102 → 1+0+2=3 (same as 12!)
    
    Hint: Use sum of digits as KEY!
    """
    groups = {}

    for num in nums:
        num_str = str(num)
        key = sum(int(i) for i in num_str)

        if key in groups:
            groups[key].append(num)
        else:
            groups[key] = [num]

    return list(groups.values())

# Test
print(group_by_digit_sum([12, 21, 30, 11, 102]))
# Expected: [[12, 21, 30, 102], [11]]

from collections import defaultdict

def group_by_digit_sum(nums):
    """
    Cleaner with defaultdict
    """
    groups = defaultdict(list)
    
    for num in nums:
        # Calculate digit sum
        digit_sum = sum(int(d) for d in str(num))
        
        # Add to group
        groups[digit_sum].append(num)
    
    return list(groups.values())

# Test
print(group_by_digit_sum([12, 21, 30, 11, 102]))
# [[12, 21, 30, 102], [11]]

# Common Patterns:

# Counting: count[item] = count.get(item, 0) + 1
# Seen/Visited: if item in seen: ...
# Complement: if (target - num) in dict: ...
# Grouping: groups[key].append(value)











