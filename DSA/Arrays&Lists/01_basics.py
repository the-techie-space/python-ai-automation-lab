"""
Arrays & Lists - Basics
========================
Core concepts: Declaration, Access, Traversal, Length
"""

# ============================================================================
# WHAT IS AN ARRAY/LIST?
# ============================================================================
# A collection of elements stored together in memory, accessed using an index.
# In Python, we use lists which are dynamic arrays.

arr = [10, 20, 30, 40]
print("Array:", arr)

# ============================================================================
# ACCESSING ELEMENTS
# ============================================================================
print("\n--- Accessing Elements ---")
print("First element (index 0):", arr[0])   # 10
print("Second element (index 1):", arr[1])  # 20
print("Last element:", arr[-1])              # 40 (negative indexing)

# ============================================================================
# ARRAY LENGTH
# ============================================================================
print("\n--- Array Length ---")
print("Length of array:", len(arr))          # 4
print("Last valid index:", len(arr) - 1)     # 3

# ============================================================================
# TRAVERSAL - Visiting each element one by one
# ============================================================================
print("\n--- Traversal Methods ---")

# Method 1: Using index
print("Method 1 - Index-based:")
for i in range(len(arr)):
    print(f"Index {i}: {arr[i]}")

# Method 2: Direct iteration (preferred when index not needed)
print("\nMethod 2 - Direct iteration:")
for element in arr:
    print(element)

# ============================================================================
# COMMON LIST METHODS - Quick Reference
# ============================================================================
print("\n--- Common List Methods ---")

# ADDING ELEMENTS
demo_list = [1, 2, 3]
demo_list.append(4)        # Add at end → [1, 2, 3, 4]
demo_list.extend([5, 6])   # Add multiple → [1, 2, 3, 4, 5, 6]
demo_list.insert(1, 10)    # Insert at index 1 → [1, 10, 2, 3, 4, 5, 6]
print("After additions:", demo_list)

# REMOVING ELEMENTS
demo_list.remove(10)       # Remove first occurrence of value
print("After remove(10):", demo_list)

popped = demo_list.pop(0)  # Remove by index, returns value
print(f"Popped value: {popped}, List: {demo_list}")

# SEARCHING & COUNTING
nums = [10, 20, 30, 20, 40]
print(f"\nIndex of 20: {nums.index(20)}")    # 1 (first occurrence)
print(f"Count of 20: {nums.count(20)}")      # 2

# SORTING & REVERSING
unsorted = [3, 1, 4, 2]
unsorted.sort()                               # In-place sort
print(f"Sorted: {unsorted}")

unsorted.reverse()                            # In-place reverse
print(f"Reversed: {unsorted}")

# COPYING LISTS
original = [1, 2, 3]
copy1 = original.copy()      # Method 1
copy2 = list(original)       # Method 2
copy3 = original[:]          # Method 3 (slicing)

# MEMBERSHIP CHECK
print(f"\n2 in original? {2 in original}")       # True
print(f"5 in original? {5 in original}")         # False

# ============================================================================
# PRACTICAL EXAMPLE: Empty Array Check
# ============================================================================
print("\n--- Checking Empty Array ---")
empty_arr = []
if len(empty_arr) >= 1:
    print("Array has elements")
else:
    print("Array is empty")

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================
"""
✓ Arrays store multiple values in one variable
✓ Index starts at 0, last index is len(arr) - 1
✓ Traversal = visiting each element
✓ append() for single, extend() for multiple
✓ remove() by value, pop() by index
✓ Always check if array is empty before operations
"""