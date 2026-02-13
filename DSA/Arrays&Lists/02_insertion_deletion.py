"""
Arrays & Lists - Insertion & Deletion
=======================================
Learn how to add and remove elements at any position
"""

# ============================================================================
# INSERTION AT ANY POSITION
# ============================================================================
"""
Strategy: Right shift elements, then insert
Time Complexity: O(n) - need to shift elements
"""

print("--- Insertion at Index 0 ---")
arr = [10, 20, 30, 40]
print("Original:", arr)

# Step 1: Add space at the end
arr.append(0)  # Now: [10, 20, 30, 40, 0]

# Step 2: Right shift elements from end to insertion position
insert_pos = 0
size = len(arr)

for i in range(size - 1, insert_pos, -1):
    arr[i] = arr[i - 1]
    # Iteration:
    # i=4: arr[4] = arr[3] → [10, 20, 30, 40, 40]
    # i=3: arr[3] = arr[2] → [10, 20, 30, 30, 40]
    # i=2: arr[2] = arr[1] → [10, 20, 20, 30, 40]
    # i=1: arr[1] = arr[0] → [10, 10, 20, 30, 40]

# Step 3: Insert new element
arr[insert_pos] = 5
print("After inserting 5 at index 0:", arr)
# Output: [5, 10, 20, 30, 40]

# ============================================================================
# GENERIC INSERTION FUNCTION
# ============================================================================

def insert_at_position(arr, element, position):
    """
    Insert element at given position
    
    Args:
        arr: The list
        element: Value to insert
        position: Index where to insert
    
    Time: O(n), Space: O(1)
    """
    if position < 0 or position > len(arr):
        print("Invalid position!")
        return arr
    
    arr.append(0)  # Make space
    size = len(arr)
    
    # Right shift
    for i in range(size - 1, position, -1):
        arr[i] = arr[i - 1]
    
    # Insert
    arr[position] = element
    return arr

# Test
test_arr = [10, 20, 30]
print("\n--- Generic Insertion ---")
print("Original:", test_arr)
insert_at_position(test_arr, 15, 1)
print("After inserting 15 at index 1:", test_arr)
# Output: [10, 15, 20, 30]

# ============================================================================
# DELETION AT ANY POSITION
# ============================================================================
"""
Strategy: Left shift elements from position, then remove last
Time Complexity: O(n) - need to shift elements
"""

print("\n--- Deletion at Index 1 ---")
arr = [10, 20, 30, 40]
print("Original:", arr)

delete_pos = 1
size = len(arr)

# Step 1: Left shift elements
for i in range(delete_pos, size - 1):
    arr[i] = arr[i + 1]
    # Iteration:
    # i=1: arr[1] = arr[2] → [10, 30, 30, 40]
    # i=2: arr[2] = arr[3] → [10, 30, 40, 40]

# Step 2: Remove last element
arr.pop()
print(f"After deleting index {delete_pos}:", arr)
# Output: [10, 30, 40]

# ============================================================================
# GENERIC DELETION FUNCTION
# ============================================================================

def delete_at_position(arr, position):
    """
    Delete element at given position
    
    Args:
        arr: The list
        position: Index to delete
    
    Time: O(n), Space: O(1)
    """
    if position < 0 or position >= len(arr):
        print("Invalid position!")
        return arr
    
    size = len(arr)
    
    # Left shift
    for i in range(position, size - 1):
        arr[i] = arr[i + 1]
    
    # Remove last
    arr.pop()
    return arr

# Test
test_arr = [10, 20, 30, 40]
print("\n--- Generic Deletion ---")
print("Original:", test_arr)
delete_at_position(test_arr, 2)
print("After deleting index 2:", test_arr)
# Output: [10, 20, 40]

# ============================================================================
# MOVING ZEROS TO END - Two Methods
# ============================================================================

print("\n--- Moving Zeros to End ---")

# Method 1: Create new array (O(n) time, O(n) space)
def move_zeros_method1(arr):
    """Using extra space - simple approach"""
    non_zero = []
    zero_count = 0
    
    for num in arr:
        if num != 0:
            non_zero.append(num)
        else:
            zero_count += 1
    
    return non_zero + [0] * zero_count

arr1 = [0, 10, 0, 20, 30, 0, 40, 0]
print("Original:", arr1)
result1 = move_zeros_method1(arr1)
print("Method 1 (new array):", result1)

# Method 2: In-place using two pointers (O(n) time, O(1) space)
def move_zeros_inplace(arr):
    """In-place - optimal approach"""
    pos = 0  # Position for next non-zero
    
    # Move all non-zeros to front
    for num in arr:
        if num != 0:
            arr[pos] = num
            pos += 1
    
    # Fill remaining with zeros
    for i in range(pos, len(arr)):
        arr[i] = 0
    
    return arr

arr2 = [0, 10, 0, 20, 30, 0, 40, 0]
print("\nOriginal:", arr2)
move_zeros_inplace(arr2)
print("Method 2 (in-place):", arr2)

# Method 3: Swap approach (most elegant!)
def move_zeros_swap(arr):
    """One-pass swap - most efficient"""
    slow = 0  # Position for next non-zero
    
    for fast in range(len(arr)):
        if arr[fast] != 0:
            arr[slow], arr[fast] = arr[fast], arr[slow]
            slow += 1
    
    return arr

arr3 = [0, 10, 0, 20, 30, 0, 40, 0]
print("\nOriginal:", arr3)
move_zeros_swap(arr3)
print("Method 3 (swap):", arr3)

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================
"""
INSERTION:
✓ Right shift from end to position
✓ Time: O(n) due to shifting
✓ Always check valid position

DELETION:
✓ Left shift from position to end
✓ Remove last element
✓ Time: O(n) due to shifting

MOVING ZEROS:
✓ Two-pointer technique is optimal
✓ In-place saves memory
✓ Swap method is cleanest
"""