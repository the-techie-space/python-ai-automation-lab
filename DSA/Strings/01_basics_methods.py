"""
Strings - Basics & Methods
===========================
Core concepts: String operations, built-in methods, case conversion
"""

# ============================================================================
# WHAT IS A STRING?
# ============================================================================
"""
String = Immutable sequence of characters
- Immutable: Cannot change in-place
- Indexed: Access characters by position
- Iterable: Can loop through characters
"""

# Creating strings
s1 = "Hello"
s2 = 'World'
s3 = """Multi
line
string"""

print("String 1:", s1)
print("String 2:", s2)
print("String 3:", s3)

# ============================================================================
# STRING INDEXING & SLICING
# ============================================================================
print("\n--- String Indexing ---")

text = "Python"
#       012345  (positive indexing)
#      -654321  (negative indexing)

print(f"First character: {text[0]}")      # P
print(f"Last character: {text[-1]}")      # n
print(f"Slice [0:3]: {text[0:3]}")        # Pyt
print(f"Slice [2:]: {text[2:]}")          # thon
print(f"Slice [:4]: {text[:4]}")          # Pyth
print(f"Reverse: {text[::-1]}")           # nohtyP

# ============================================================================
# STRING IMMUTABILITY
# ============================================================================
print("\n--- String Immutability ---")

s = "abc"
print("Original:", s)

# This creates a NEW string, doesn't modify original
s += "d"
print("After concatenation:", s)  # "abcd"

# This would cause an error:
# s[0] = 'A'  # TypeError: 'str' object does not support item assignment

# To modify, create new string:
s = "X" + s[1:]  # Replace first character
print("After replacement:", s)

# ============================================================================
# CASE CONVERSION METHODS
# ============================================================================
print("\n--- Case Conversion ---")

text = "python programming"

print("upper():", text.upper())           # PYTHON PROGRAMMING
print("lower():", text.lower())           # python programming
print("title():", text.title())           # Python Programming
print("capitalize():", text.capitalize()) # Python programming
print("swapcase():", text.swapcase())     # PYTHON PROGRAMMING

# Practical example: Normalize input
user_input = "  PyThOn  "
normalized = user_input.strip().lower()
print(f"\nNormalized input: '{normalized}'")

# ============================================================================
# VALIDATION METHODS (Return True/False)
# ============================================================================
print("\n--- String Validation ---")

# Check character types
print("'abc'.isalpha():", "abc".isalpha())         # True (only letters)
print("'123'.isdigit():", "123".isdigit())         # True (only digits)
print("'abc123'.isalnum():", "abc123".isalnum())   # True (letters + digits)
print("'   '.isspace():", "   ".isspace())         # True (only whitespace)

# Check case
print("'ABC'.isupper():", "ABC".isupper())         # True
print("'abc'.islower():", "abc".islower())         # True

# Practical validation
def is_valid_username(username):
    """Username must be alphanumeric and 3-15 characters"""
    return username.isalnum() and 3 <= len(username) <= 15

print("\nUsername validation:")
print("'user123':", is_valid_username("user123"))  # True
print("'ab':", is_valid_username("ab"))            # False (too short)
print("'user@123':", is_valid_username("user@123")) # False (has @)

# ============================================================================
# STRING SEARCHING METHODS
# ============================================================================
print("\n--- String Searching ---")

text = "Hello World, Hello Python"

# find() - returns index or -1
print("find('Hello'):", text.find("Hello"))        # 0
print("find('World'):", text.find("World"))        # 6
print("find('Java'):", text.find("Java"))          # -1 (not found)

# index() - returns index or raises error
print("index('Python'):", text.index("Python"))    # 20
# print(text.index("Java"))  # Would raise ValueError

# count() - count occurrences
print("count('Hello'):", text.count("Hello"))      # 2
print("count('l'):", text.count("l"))              # 5

# startswith() / endswith()
filename = "script.py"
print(f"\n'{filename}' starts with 'script':", filename.startswith("script"))  # True
print(f"'{filename}' ends with '.py':", filename.endswith(".py"))              # True
print(f"'{filename}' ends with '.txt':", filename.endswith(".txt"))            # False

# ============================================================================
# SPLIT & JOIN METHODS
# ============================================================================
print("\n--- Split & Join ---")

# split() - string to list
sentence = "Python is easy"
words = sentence.split()  # Split by whitespace
print("Split by space:", words)  # ['Python', 'is', 'easy']

csv = "apple,banana,cherry"
fruits = csv.split(",")  # Split by comma
print("Split by comma:", fruits)  # ['apple', 'banana', 'cherry']

# join() - list to string
words = ["Python", "is", "easy"]
sentence = " ".join(words)
print("Join with space:", sentence)  # "Python is easy"

csv = ",".join(["a", "b", "c"])
print("Join with comma:", csv)  # "a,b,c"

# Practical example: Path manipulation
path_parts = ["home", "user", "documents", "file.txt"]
unix_path = "/".join(path_parts)
windows_path = "\\".join(path_parts)
print(f"\nUnix path: {unix_path}")
print(f"Windows path: {windows_path}")

# ============================================================================
# REPLACE METHOD
# ============================================================================
print("\n--- String Replace ---")

text = "Hello World"
new_text = text.replace("World", "Python")
print("Replace 'World' with 'Python':", new_text)

# Replace multiple occurrences
text = "banana"
new_text = text.replace("a", "o")
print("Replace all 'a' with 'o':", new_text)  # "bonono"

# Replace with limit
text = "banana"
new_text = text.replace("a", "o", 2)  # Replace only first 2
print("Replace first 2 'a':", new_text)  # "bonona"

# ============================================================================
# STRIP METHODS (Remove Whitespace)
# ============================================================================
print("\n--- Strip Methods ---")

text = "   Hello World   "
print(f"Original: '{text}'")
print(f"strip(): '{text.strip()}'")      # Remove both sides
print(f"lstrip(): '{text.lstrip()}'")    # Remove left side
print(f"rstrip(): '{text.rstrip()}'")    # Remove right side

# Strip specific characters
text = "xxxHelloxxx"
print(f"\nStrip 'x': '{text.strip('x')}'")  # "Hello"

# Practical example: Clean user input
user_input = "  john.doe@email.com  "
clean_email = user_input.strip().lower()
print(f"\nCleaned email: {clean_email}")

# ============================================================================
# STRING FORMATTING
# ============================================================================
print("\n--- String Formatting ---")

name = "Alice"
age = 25

# Method 1: f-strings (Recommended - Python 3.6+)
message = f"{name} is {age} years old"
print("f-string:", message)

# Method 2: format()
message = "{} is {} years old".format(name, age)
print("format():", message)

# Method 3: format() with names
message = "{name} is {age} years old".format(name=name, age=age)
print("format() with names:", message)

# Advanced formatting
price = 123.456
print(f"\nPrice: ${price:.2f}")  # 2 decimal places
print(f"Price: ${price:>10.2f}")  # Right-aligned, width 10

# ============================================================================
# STRING LENGTH
# ============================================================================
print("\n--- String Length ---")

text = "Python"
print(f"Length of '{text}': {len(text)}")

# Empty string
empty = ""
print(f"Length of empty string: {len(empty)}")

# ============================================================================
# STRING ENCODING
# ============================================================================
print("\n--- String Encoding ---")

text = "python"
encoded = text.encode()  # Default UTF-8
print(f"Encoded: {encoded}")
print(f"Type: {type(encoded)}")

# Decode back
decoded = encoded.decode()
print(f"Decoded: {decoded}")

# ============================================================================
# COMMON STRING OPERATIONS
# ============================================================================
print("\n--- Common Operations ---")

# Concatenation
s1 = "Hello"
s2 = "World"
result = s1 + " " + s2
print("Concatenation:", result)

# Repetition
text = "Ha" * 3
print("Repetition:", text)  # "HaHaHa"

# Membership
text = "Python Programming"
print("'Python' in text:", "Python" in text)      # True
print("'Java' in text:", "Java" in text)          # False

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================
"""
STRING BASICS:
✓ Strings are immutable - operations create new strings
✓ Use indexing [0] and slicing [start:end]
✓ Negative indexing starts from end

CASE METHODS:
✓ upper(), lower(), title(), capitalize(), swapcase()
✓ Always return new strings

VALIDATION:
✓ isalpha(), isdigit(), isalnum(), isspace()
✓ isupper(), islower()
✓ All return True/False

SEARCHING:
✓ find() returns -1 if not found
✓ index() raises error if not found
✓ count() for occurrences
✓ startswith(), endswith() for prefixes/suffixes

SPLIT & JOIN:
✓ split() converts string → list
✓ join() converts list → string
✓ Useful for CSV, paths, sentences

FORMATTING:
✓ f-strings are the modern way (Python 3.6+)
✓ format() for older code
✓ Use for clean, readable string construction
"""