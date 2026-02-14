# count() → string, list, tuple
# Not available for set or dict

# Methods like len, count, index, sorted, and in are commonly
# used across multiple Python data types, while mutation methods are usually type-specific.

text = "banana"
text.count("a")     # 3
text.count("na")    # 2


lst = [1, 2, 3, 2, 2]
lst.count(2)        # 3

"hello".count("l")     # 2
[1, 2, 2].count(2)     # 2
(1, 1, 2).count(1)     # 2


# len() → string, list, tuple, set, dict


len("python")        # 6
len([1, 2, 3])       # 3
len((1, 2))          # 2
len({1, 2, 3})       # 3
len({"a": 1})        # 1


# index() → string, list, tuple

"python".index("t")    # 2
[10, 20, 30].index(20) # 1
(5, 6, 7).index(7)     # 2


# in / not in → ALL iterables

"a" in "cat"           # True
2 in [1, 2, 3]         # True
1 in (1, 2)            # True
1 in {1, 2}            # True
"a" in {"a": 1}        # checks keys → True

# sorted() → string, list, tuple, set, dict
# sort() exists only for lists

sorted("cba")          # ['a', 'b', 'c']
sorted([3, 1, 2])      # [1, 2, 3]
sorted((3, 2, 1))      # [1, 2, 3]
sorted({3, 1, 2})      # [1, 2, 3]
sorted({"b":1,"a":2})  # ['a', 'b']

# min() / max() → string, list, tuple, set

min("python")     # 'h'
max([1, 5, 2])    # 5


# sum() → list, tuple, set (numeric only)
# Not for strings or dicts

sum([1, 2, 3])    # 6
sum((4, 5))       # 9

# any() / all() → ALL iterables

any([0, 1, 0])    # True
all([1, 2, 3])    # True



