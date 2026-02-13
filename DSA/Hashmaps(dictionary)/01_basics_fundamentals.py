"""
Hash Maps (Dictionaries) - Basics & Fundamentals
=================================================
Learn the foundation of Python's most powerful data structure
"""

# ============================================================================
# WHAT IS A HASH MAP? 🤔
# ============================================================================
"""
Real-World Analogy: Library System

❌ BAD SYSTEM (Array/List):
Books stored by arrival order:
    Book 1: "Python Basics"
    Book 2: "Java Guide"
    Book 3: "DSA Master"
    ...
    Book 1000: "AI Handbook"

To find "AI Handbook" → Check all 1000 books! O(n) 😢

✅ GOOD SYSTEM (Hash Map/Dictionary):
Books organized by unique ID:
    ID "PY001" → "Python Basics"
    ID "JV002" → "Java Guide"
    ID "DS003" → "DSA Master"
    ...
    ID "AI999" → "AI Handbook"

To find book with ID "AI999" → Direct access! O(1) 🚀

KEY CONCEPT:
- Hash Map stores data in KEY-VALUE pairs for instant lookup
- Key = Unique identifier (like a label)
- Value = The data you want to store
- Access = Use key to get value instantly O(1)
"""

# ============================================================================
# BASIC DICTIONARY SYNTAX
# ============================================================================
print("="*60)
print("BASIC DICTIONARY OPERATIONS")
print("="*60)

# Creating a dictionary
student = {
    "name": "Alice",      # key: "name",  value: "Alice"
    "age": 20,            # key: "age",   value: 20
    "grade": "A"          # key: "grade", value: "A"
}

# Access by key - O(1) time!
print(f"Student name: {student['name']}")  # "Alice" - INSTANT!
print(f"Student age: {student['age']}")    # 20
print(f"Student grade: {student['grade']}")  # "A"

# ============================================================================
# CREATING DICTIONARIES - Multiple Methods
# ============================================================================
print("\n" + "="*60)
print("CREATING DICTIONARIES")
print("="*60)

# Method 1: Using curly braces {}
empty_dict = {}
person = {"name": "Bob", "age": 25, "city": "NYC"}
print(f"Method 1: {person}")

# Method 2: Using dict() constructor
empty_dict2 = dict()
person2 = dict(name="Bob", age=25, city="NYC")
print(f"Method 2: {person2}")

# Method 3: From two lists using zip()
keys = ["a", "b", "c"]
values = [1, 2, 3]
my_dict = dict(zip(keys, values))
print(f"Method 3 (from lists): {my_dict}")  # {'a': 1, 'b': 2, 'c': 3}

# Method 4: Dictionary comprehension
squares = {x: x**2 for x in range(1, 6)}
print(f"Method 4 (comprehension): {squares}")  # {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

# ============================================================================
# ESSENTIAL OPERATIONS - MUST KNOW
# ============================================================================
print("\n" + "="*60)
print("ESSENTIAL DICTIONARY OPERATIONS")
print("="*60)

# 1. CREATE
student = {"name": "Alice", "age": 20, "major": "CS"}
print(f"1. Created: {student}")

# 2. ACCESS (Get value by key)
print("\n2. Accessing values:")
print(f"   Using []: {student['name']}")        # "Alice"
print(f"   Using get(): {student.get('age')}")  # 20

# 3. ADD / UPDATE
print("\n3. Adding/Updating:")
student["grade"] = "A"        # Add new key-value
print(f"   After adding grade: {student}")
student["age"] = 21           # Update existing value
print(f"   After updating age: {student}")

# 4. DELETE
print("\n4. Deleting:")
del student["major"]          # Remove key-value pair
print(f"   After del: {student}")
removed = student.pop("grade")  # Remove and return value
print(f"   Popped '{removed}': {student}")

# 5. CHECK if key exists
print("\n5. Checking existence:")
if "name" in student:
    print("   'name' exists in dictionary!")
if "grade" not in student:
    print("   'grade' does NOT exist!")

# 6. GET all keys/values/items
print("\n6. Getting keys/values/items:")
student = {"name": "Alice", "age": 21, "city": "NYC"}
print(f"   Keys: {list(student.keys())}")      # ['name', 'age', 'city']
print(f"   Values: {list(student.values())}")  # ['Alice', 21, 'NYC']
print(f"   Items: {list(student.items())}")    # [('name', 'Alice'), ...]

# 7. LENGTH
print(f"\n7. Length: {len(student)} key-value pairs")

# ============================================================================
# CRITICAL: .get() vs [] ACCESS
# ============================================================================
print("\n" + "="*60)
print("IMPORTANT: .get() vs [] ACCESS")
print("="*60)

student = {"name": "Alice", "age": 20}

# Using [] - CRASHES if key doesn't exist
print("Using [] notation:")
print(f"  student['name'] = {student['name']}")  # Works: "Alice"
# print(student['grade'])  # ❌ KeyError! CRASHES!

# Using .get() - Returns None if key doesn't exist
print("\nUsing .get() method:")
print(f"  student.get('name') = {student.get('name')}")      # "Alice"
print(f"  student.get('grade') = {student.get('grade')}")    # None (safe!)
print(f"  student.get('grade', 'N/A') = {student.get('grade', 'N/A')}")  # "N/A"

print("\n⭐ BEST PRACTICE: Use .get() when key might not exist!")

# ============================================================================
# WHY ARE HASH MAPS O(1)? ⚡
# ============================================================================
print("\n" + "="*60)
print("THE MAGIC OF HASHING - Why O(1)?")
print("="*60)

print("""
How Python finds values INSTANTLY:

When you do: student["name"]

Behind the scenes:
1. Python calculates hash("name") → number (e.g., 12345)
2. Uses that number to find exact memory location
3. Retrieves value directly - NO SEARCHING!

Comparison:
-----------
ARRAY/LIST - Must search O(n):
    students = [
        {"name": "Alice", "id": 1},
        {"name": "Bob", "id": 2},
        ... 1000 more students
    ]
    Finding student with id=500 → check 500 items! 😢

HASH MAP - Direct access O(1):
    students = {
        1: {"name": "Alice"},
        2: {"name": "Bob"},
        ... 1000 more students
    }
    Finding student with id=500 → INSTANT! 🚀
""")

# Practical demonstration
print("\nPractical example:")
students_dict = {
    1: {"name": "Alice"},
    2: {"name": "Bob"},
    500: {"name": "Charlie"}
}
print(f"Finding student 500: {students_dict[500]}")  # Instant!

# ============================================================================
# COMMON DICTIONARY METHODS - Quick Reference
# ============================================================================
print("\n" + "="*60)
print("DICTIONARY METHODS CHEAT SHEET")
print("="*60)

sample = {"a": 1, "b": 2, "c": 3}

print(f"Original dict: {sample}")
print("\nMethods:")
print(f"  .keys()    : {list(sample.keys())}")
print(f"  .values()  : {list(sample.values())}")
print(f"  .items()   : {list(sample.items())}")
print(f"  .get('a')  : {sample.get('a')}")
print(f"  .get('z', 0): {sample.get('z', 0)}")  # Default value

# pop() - remove and return
value = sample.pop("a")
print(f"\nAfter pop('a'): {sample}, returned: {value}")

# update() - merge dictionaries
sample.update({"d": 4, "e": 5})
print(f"After update: {sample}")

# clear() - remove all items
sample_copy = sample.copy()
sample_copy.clear()
print(f"After clear: {sample_copy}")

# setdefault() - get value or set default if not exists
sample.setdefault("f", 6)
print(f"After setdefault('f', 6): {sample}")

# ============================================================================
# ITERATING OVER DICTIONARIES
# ============================================================================
print("\n" + "="*60)
print("ITERATING OVER DICTIONARIES")
print("="*60)

grades = {"Alice": 95, "Bob": 87, "Charlie": 92}

# Method 1: Iterate over keys (default)
print("1. Iterating over keys:")
for name in grades:
    print(f"   {name}: {grades[name]}")

# Method 2: Iterate over keys explicitly
print("\n2. Iterating over keys (explicit):")
for name in grades.keys():
    print(f"   {name}")

# Method 3: Iterate over values
print("\n3. Iterating over values:")
for score in grades.values():
    print(f"   Score: {score}")

# Method 4: Iterate over key-value pairs (MOST COMMON)
print("\n4. Iterating over items (key-value pairs):")
for name, score in grades.items():
    print(f"   {name}: {score}")

# ============================================================================
# NESTED DICTIONARIES
# ============================================================================
print("\n" + "="*60)
print("NESTED DICTIONARIES")
print("="*60)

# Dictionary of dictionaries
students = {
    "student1": {
        "name": "Alice",
        "age": 20,
        "grades": {"math": 95, "english": 88}
    },
    "student2": {
        "name": "Bob",
        "age": 21,
        "grades": {"math": 87, "english": 92}
    }
}

# Accessing nested values
print(f"Student1 name: {students['student1']['name']}")
print(f"Student1 math grade: {students['student1']['grades']['math']}")

# Iterating over nested dict
print("\nAll students:")
for student_id, info in students.items():
    print(f"\n{student_id}:")
    print(f"  Name: {info['name']}")
    print(f"  Age: {info['age']}")
    print(f"  Grades: {info['grades']}")

# ============================================================================
# DICTIONARY VS LIST - WHEN TO USE WHAT
# ============================================================================
print("\n" + "="*60)
print("DICTIONARY vs LIST - When to use what?")
print("="*60)

comparison = """
USE DICTIONARY WHEN:
✓ Need fast lookup by key (O(1))
✓ Data has natural key-value relationship
✓ Need to count/track occurrences
✓ Want to group related data
Examples: phone book, word count, user profiles

USE LIST WHEN:
✓ Order matters
✓ Need to access by position/index
✓ Data is sequential
✓ Need to maintain duplicates
Examples: todo list, ordered scores, timeline
"""
print(comparison)

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================
"""
DICTIONARY BASICS:
✓ Key-value pairs for O(1) lookup
✓ Keys must be unique and immutable (strings, numbers, tuples)
✓ Values can be anything

CREATION:
✓ Literal: {"key": "value"}
✓ Constructor: dict(key="value")
✓ From lists: dict(zip(keys, values))

ACCESS:
✓ Use [] for guaranteed existence
✓ Use .get() for safe access with default

OPERATIONS:
✓ Add/Update: dict[key] = value
✓ Delete: del dict[key] or dict.pop(key)
✓ Check: key in dict
✓ Iterate: for k, v in dict.items()

WHY O(1)?
✓ Hashing converts key to memory address
✓ Direct access without searching
✓ Makes dictionaries incredibly fast!

BEST PRACTICES:
✓ Use meaningful key names
✓ Use .get() when key might not exist
✓ Use dict.items() for key-value iteration
✓ Consider defaultdict for automatic defaults
"""

print("\n" + "="*60)
print("✓ Dictionary basics complete!")
print("="*60)