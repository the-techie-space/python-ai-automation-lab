# string and its methods
# Case Conversion Methods

# Python provides string methods for case conversion, validation, splitting/joining, searching, replacing, stripping, and formatting.

# Used to change the case of strings.

# upper() → converts to uppercase

# lower() → converts to lowercase

# title() → first letter of each word uppercase

# capitalize() → first letter uppercase

# swapcase() → swaps case

word = " ".join(["python", "is", "easy"])
print(word)

print("python is easy".split())

s = "a,b,c"
print(s.split(","))

print("file.py".startswith("file"))

print("file.py".endswith(".py"))

print("banana".count("a"))

print(len("python"))

print("{} is {}".format("Python", "easy"))

lang = "Python language"

print(f"{lang} is easy")

print("python".encode())

# Checking / Validation Methods

# Used to check string properties (returns True or False).

# isalpha() → only letters

# isdigit() → only digits

# isalnum() → letters + digits

# isspace() → only spaces

# startswith() / endswith()

# Split & Join Methods

# Used to break or combine strings.

# split() → splits string into list

# rsplit() → splits from right

# join() → joins iterable into string

# s = "a,b,c"
# lst = s.split(",")         # ['a', 'b', 'c']
# ",".join(lst)              # 'a,b,c'

# Search & Index Methods

# Used to find substrings.

# find() → returns index or -1

# index() → returns index or error

# count() → number of occurrences

# Replace Methods

# Used to replace characters or substrings.

# replace(old, new)

# "hello world".replace("world", "python")
# 'hello python'

# Strip Methods

# Used to remove unwanted spaces or characters.

# strip() → removes both sides

# lstrip() → left side

# rstrip() → right side

# "  hi  ".strip()    # 'hi'

# Formatting Methods

# Used to format strings.

# format()

# f-strings (recommended)

# Formatting Methods

# Used to format strings.

# format()

# f-strings (recommended)


s = "abc"
s += "d"

print(s)

    
s = "A man a plan a canal Panama"

cleaned_s = "".join(ch.lower() for ch in s if ch.isalnum())

print(cleaned_s)

left, right = 0, len(cleaned_s) - 1
is_pali = True
while left < right:
    if cleaned_s[left] != cleaned_s[right]:
        is_pali = False
        break
    left += 1
    right -= 1

    
print(is_pali)

# first Non repeating character in a given string

s = "aabbcddee"

freq_dict = {}

for ch in s:
    freq_dict[ch] = freq_dict.get(ch, 0) + 1

for ch in s:
    if freq_dict[ch] == 1:
        print(f"First Non Repeating Character = {ch}")
        break

for ch, count in freq_dict.items():
    if count == 1:
        print(f"First Non Repeating Character (dict) = {ch}")
        break

    
# Remove Duplicate Characters (Preserve Order)

s = "banana"

seen = set()

res = []

for ch in s:
    if ch not in seen:
        seen.add(ch)
        res.append(ch)

print("".join(res))

# String Compression

# "aaabbc" → "a3b2c1"

s = "aaabbc"

res = []

count = 1

for i  in range(1, len(s)):
    if s[i] == s[i-1]:
        count += 1
    else:
        res.append(s[i-1] + str(count))
        count = 1

res.append(s[i-1] + str(count))
print("".join(res))

# Count Vowels & Consonants

# s = "Interview"

s = "Interview".lower()

vowels = set('aeiou')

vowel = consonant = 0

for i in s:
    if i.isalpha():
        if i in vowels:
            vowel += 1
        else:
            consonant += 1
        
print(f"vovwels = {vowel} and consonants = {consonant}")


# Find Duplicate Characters

# "programming" → r, g, m

s = "programming"

freq_dict = {}

for i in s:
    freq_dict[i] = freq_dict.get(i, 0) + 1

for i in s:
    if freq_dict[i] > 1:
        print(f"Duplicate Characters are {i}")

# Maximum Occurring Character
# "abbccc" → c
s = "abbccc"

freq_dict = {}

for ch in s:
    freq_dict[ch] = freq_dict.get(ch, 0) + 1

max_occur_ch = s[0]

for ch in s:
    if freq_dict[ch] > freq_dict[max_occur_ch]:
        max_occur_ch = ch

print(f"Maximum Occurring Character = {max_occur_ch}")
