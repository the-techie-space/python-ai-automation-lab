# Strings - Complete DSA Guide 📚

A comprehensive, well-organized collection of string data structure problems with clear explanations, multiple approaches, and detailed examples.

## 📂 File Structure

```
DSA/Strings/
├── README.md                          # You are here!
├── 01_basics_methods.py              # String fundamentals & methods
├── 02_palindrome_frequency.py        # Palindromes & character counting
├── 03_manipulation_transformations.py # String operations & conversions
└── 04_advanced_problems.py           # Advanced algorithms & patterns
```

## 🎯 Learning Path

### **Beginner** (Start Here)
1. **01_basics_methods.py** - Learn string basics, indexing, slicing, built-in methods
2. **02_palindrome_frequency.py** - Master palindrome checking and frequency counting

### **Intermediate**
3. **03_manipulation_transformations.py** - String compression, deduplication, transformations

### **Advanced**
4. **04_advanced_problems.py** - Anagrams, sliding window, KMP algorithm

## 📖 What You'll Learn

### File 1: Basics & Methods (01_basics_methods.py)
- ✓ String fundamentals & immutability
- ✓ Indexing and slicing
- ✓ Case conversion (upper, lower, title, capitalize, swapcase)
- ✓ Validation methods (isalpha, isdigit, isalnum, isspace)
- ✓ Searching (find, index, count, startswith, endswith)
- ✓ Split & join operations
- ✓ Replace and strip methods
- ✓ String formatting (f-strings, format())
- ✓ Encoding/decoding

### File 2: Palindrome & Frequency (02_palindrome_frequency.py)
- ✓ Simple palindrome checking
- ✓ Advanced palindrome (with cleaning)
- ✓ Character frequency counting
- ✓ First non-repeating character
- ✓ Finding duplicate characters
- ✓ Maximum occurring character
- ✓ Counting vowels & consonants
- ✓ Complete string analysis

### File 3: Manipulation & Transformations (03_manipulation_transformations.py)
- ✓ Remove duplicate characters
- ✓ String compression (run-length encoding)
- ✓ String decompression
- ✓ Reverse words in string
- ✓ Reverse each word individually
- ✓ Remove/replace spaces
- ✓ Title case conversion
- ✓ Toggle case (swap case)
- ✓ Multi-step transformations

### File 4: Advanced Problems (04_advanced_problems.py)
- ✓ Anagram detection
- ✓ Group anagrams
- ✓ Longest common prefix
- ✓ Longest palindromic substring
- ✓ Valid parentheses
- ✓ String to integer (atoi)
- ✓ Longest substring without repeating
- ✓ Zigzag conversion
- ✓ KMP string matching algorithm

## 🔥 Key Techniques Covered

| Technique | Problems Using It |
|-----------|------------------|
| **Frequency Counting** | Character frequency, Duplicates, Anagrams |
| **Two Pointers** | Palindrome, Longest unique substring |
| **Stack** | Valid parentheses, Expression evaluation |
| **Sliding Window** | Longest unique substring, Pattern matching |
| **String Building** | Compression, Decompression, Transformations |
| **Pattern Matching** | KMP algorithm, Find & replace |

## ⚡ Time Complexity Quick Reference

| Operation | Time | Space | Notes |
|-----------|------|-------|-------|
| Access character | O(1) | O(1) | Direct indexing |
| Concatenation (+) | O(n) | O(n) | Creates new string |
| Slicing [start:end] | O(k) | O(k) | k = slice length |
| find() / index() | O(n) | O(1) | Linear search |
| split() | O(n) | O(n) | Creates list |
| join() | O(n) | O(n) | Builds string |
| Palindrome check | O(n) | O(1) | Two pointers |
| Frequency counting | O(n) | O(k) | k = unique chars |
| Anagram check | O(n log n) | O(1) | Using sort |
| KMP search | O(n+m) | O(m) | Optimal pattern match |

## 💡 How to Use This Repository

### Option 1: Sequential Learning
Work through files in order (01 → 04) for systematic learning.

### Option 2: Topic-Based
Jump to specific topics:
- Need string basics? → `01_basics_methods.py`
- Working with palindromes? → `02_palindrome_frequency.py`
- Need to transform strings? → `03_manipulation_transformations.py`
- Advanced algorithms? → `04_advanced_problems.py`

### Option 3: Problem-First
Looking for specific problems? Use the index below.

## 🔍 Problem Index

### By Difficulty

**Easy**
- String indexing and slicing (01)
- Case conversion (01)
- Split and join (01)
- Simple palindrome (02)
- Character frequency (02)
- Remove duplicates (03)
- Reverse words (03)

**Medium**
- Advanced palindrome with cleaning (02)
- First non-repeating character (02)
- String compression (03)
- Anagram detection (04)
- Longest common prefix (04)
- Valid parentheses (04)
- Longest unique substring (04)

**Hard**
- Longest palindromic substring (04)
- Group anagrams (04)
- Zigzag conversion (04)
- KMP string matching (04)

### By Technique

**Frequency Counting**
- Character frequency (02)
- First non-repeating (02)
- Find duplicates (02)
- Max occurring character (02)
- Anagram detection (04)

**Two Pointers**
- Palindrome check (02)
- Longest unique substring (04)

**String Building**
- Compression (03)
- Decompression (03)
- Remove duplicates (03)

**Pattern Matching**
- find(), index() (01)
- KMP algorithm (04)

## 🎓 Tips for Success

1. **Understand Immutability**: Strings can't be modified in-place
2. **Use Built-in Methods**: Python has powerful string methods
3. **Practice Frequency Counting**: Foundation for many problems
4. **Master Two Pointers**: Common in palindrome/substring problems
5. **Learn Time Complexity**: Understand cost of operations
6. **Test Edge Cases**: Empty strings, single characters, all same

## 📝 Common String Patterns

### Pattern 1: Frequency Dictionary
```python
freq = {}
for ch in string:
    freq[ch] = freq.get(ch, 0) + 1
```

### Pattern 2: Two Pointers
```python
left, right = 0, len(s) - 1
while left < right:
    # Compare and move
    left += 1
    right -= 1
```

### Pattern 3: String Building
```python
result = []
for ch in string:
    # Process character
    result.append(processed)
return "".join(result)
```

### Pattern 4: Sliding Window
```python
window = set()
left = 0
for right in range(len(s)):
    while s[right] in window:
        window.remove(s[left])
        left += 1
    window.add(s[right])
```

## 🚀 Interview Tips

### Most Common String Interview Questions
1. **Palindrome checking** (variations)
2. **Anagram detection** (and grouping)
3. **Substring problems** (longest unique, common prefix)
4. **Frequency counting** (first non-repeating, duplicates)
5. **String transformations** (compression, reversals)

### Time Complexity Traps
- Concatenation in loop: O(n²) → Use list + join
- Nested loops on strings: Usually O(n²) → Consider alternatives
- String immutability: Creates new strings → Watch memory

### Optimization Tips
- Use `"".join(list)` instead of repeated `+=`
- Use `set` for O(1) membership checks
- Use `Counter` from collections for frequency
- Consider using `bytearray` for mutable strings

## 🤝 Best Practices

1. **Always Validate Input**: Check for None, empty strings
2. **Consider Case Sensitivity**: Use `.lower()` when needed
3. **Handle Unicode**: Be aware of encoding issues
4. **Use Slicing Wisely**: Remember it creates new strings
5. **Profile Before Optimizing**: Measure actual performance

## 📚 Additional Resources

- **LeetCode String Tag**: 150+ string problems
- **Interview Patterns**: Strings appear in 30%+ of coding interviews
- **Python String Docs**: Official documentation for all methods

## 🔗 Related Topics

After mastering strings:
1. **Arrays** - Similar indexing and slicing
2. **Hash Tables** - Perfect for frequency counting
3. **Dynamic Programming** - For complex substring problems
4. **Tries** - For efficient string storage/search
5. **Regular Expressions** - Advanced pattern matching

---

## 📊 Progress Tracker

- [ ] Completed 01_basics_methods.py
- [ ] Completed 02_palindrome_frequency.py
- [ ] Completed 03_manipulation_transformations.py
- [ ] Completed 04_advanced_problems.py
- [ ] Solved 10+ additional string problems
- [ ] Can explain time/space complexity
- [ ] Ready for string interview questions!

---

**Happy Coding! 🎉**

*Master these string techniques and you'll handle any text manipulation challenge with confidence!*