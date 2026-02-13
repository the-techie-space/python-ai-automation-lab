"""
Arrays & Lists - Searching & Duplicates
=========================================
Finding elements, handling duplicates, frequency counting
"""

# ============================================================================
# FINDING DUPLICATES - Dictionary Method
# ============================================================================
"""
Use dictionary to track frequency of each element
Time: O(n), Space: O(n)
"""

print("--- Finding Duplicates ---")
arr = [10, 20, 30, 10, 40, 20]
frequency = {}

# Count frequency of each element
for num in arr:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

print("Array:", arr)
print("Frequency dictionary:", frequency)

# Find only duplicates
print("\nDuplicate elements:")
for num, count in frequency.items():
    if count > 1:
        print(f"{num} appears {count} times")

# ============================================================================
# ARMSTRONG NUMBER CHECKER
# ============================================================================
"""
Armstrong number: Sum of digits raised to power of digit count equals the number
Examples: 153 = 1³ + 5³ + 3³ = 1 + 125 + 27 = 153
         9474 = 9⁴ + 4⁴ + 7⁴ + 4⁴ = 9474
"""

def armstrong_number(num):
    """
    Check if number is Armstrong number
    
    Args:
        num: Integer to check
    
    Returns:
        bool: True if Armstrong number
    """
    # Convert to list of digits
    digits = [int(d) for d in str(num)]
    
    # Power is the count of digits
    power = len(digits)
    
    # Calculate sum of each digit raised to power
    sum_of_powers = sum(d ** power for d in digits)
    
    return num == sum_of_powers

# Test Armstrong numbers
print("\n--- Armstrong Number Checker ---")
test_numbers = [0, 1, 153, 370, 371, 407, 1634, 9474, 123]

for num in test_numbers:
    if armstrong_number(num):
        print(f"{num} is an Armstrong number ✓")
    else:
        print(f"{num} is NOT an Armstrong number ✗")

# Interactive input
print("\n--- Try Your Own Number ---")
# Uncomment below for interactive testing
# user_input = int(input("Enter a number: "))
# if armstrong_number(user_input):
#     print(f"{user_input} is an Armstrong number!")
# else:
#     print(f"{user_input} is NOT an Armstrong number")

# ============================================================================
# FINDING MIN & MAX
# ============================================================================
"""
Linear scan to find minimum and maximum values
Time: O(n), Space: O(1)
"""

def find_min_max(arr):
    """
    Find minimum and maximum in single pass
    
    Args:
        arr: List of numbers
    
    Returns:
        tuple: (min_value, max_value)
    """
    if len(arr) == 0:
        return None, None
    
    min_num = max_num = arr[0]
    
    for num in arr:
        if num > max_num:
            max_num = num
        if num < min_num:
            min_num = num
    
    return min_num, max_num

# Test
print("\n--- Finding Min & Max ---")
test_arr = [3, 5, 1, 9, 2, 8, 4]
min_val, max_val = find_min_max(test_arr)
print(f"Array: {test_arr}")
print(f"Minimum: {min_val}, Maximum: {max_val}")

# ============================================================================
# REVERSE ARRAY IN-PLACE
# ============================================================================
"""
Two-pointer technique: swap elements from both ends
Time: O(n/2) = O(n), Space: O(1)
"""

def reverse_array(arr):
    """
    Reverse array using two pointers
    
    Args:
        arr: List to reverse
    
    Returns:
        list: Reversed array (modifies in-place)
    """
    left = 0
    right = len(arr) - 1
    
    while left < right:
        # Swap elements
        arr[left], arr[right] = arr[right], arr[left]
        
        # Move pointers
        left += 1
        right -= 1
    
    return arr

# Test
print("\n--- Reverse Array ---")
test_arr = [1, 2, 3, 4, 5]
print("Original:", test_arr)
reverse_array(test_arr)
print("Reversed:", test_arr)

# ============================================================================
# FIND MISSING NUMBER (1 to n)
# ============================================================================
"""
Given array of n-1 numbers from 1 to n, find missing number
Formula: sum(1 to n) = n * (n + 1) / 2
Time: O(n), Space: O(1)
"""

def find_missing_number(arr):
    """
    Find missing number in sequence 1 to n
    
    Args:
        arr: List with one missing number
    
    Returns:
        int: The missing number
    """
    n = len(arr) + 1  # Total numbers including missing
    
    # Sum of 1 to n
    expected_sum = n * (n + 1) // 2
    
    # Actual sum
    actual_sum = sum(arr)
    
    return expected_sum - actual_sum

# Test
print("\n--- Find Missing Number ---")
test_arr = [1, 2, 4, 5, 6]  # Missing 3
print("Array:", test_arr)
print("Missing number:", find_missing_number(test_arr))

test_arr2 = [1, 2, 3, 4, 5, 7, 8]  # Missing 6
print("\nArray:", test_arr2)
print("Missing number:", find_missing_number(test_arr2))

# ============================================================================
# REMOVE DUPLICATES FROM SORTED ARRAY
# ============================================================================
"""
Two-pointer technique for sorted arrays
Time: O(n), Space: O(1)
"""

def remove_duplicates(arr):
    """
    Remove duplicates in-place from sorted array
    
    Args:
        arr: Sorted list with duplicates
    
    Returns:
        int: Length of array with unique elements
    """
    if len(arr) == 0:
        return 0
    
    slow = 0  # Position for next unique element
    
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    
    return slow + 1

# Test
print("\n--- Remove Duplicates (Sorted) ---")
test_arr = [1, 1, 2, 2, 2, 3, 4, 4, 5]
print("Original:", test_arr)
new_length = remove_duplicates(test_arr)
print(f"After removal: {test_arr[:new_length]}")
print(f"New length: {new_length}")

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================
"""
FINDING DUPLICATES:
✓ Use dictionary for frequency counting
✓ Time: O(n), Space: O(n)

FINDING MIN/MAX:
✓ Single pass comparison
✓ Initialize with first element

REVERSE ARRAY:
✓ Two pointers from both ends
✓ Swap and move inward

MISSING NUMBER:
✓ Use sum formula: n(n+1)/2
✓ Difference gives missing number

REMOVE DUPLICATES:
✓ Two pointers: slow for unique, fast for scanning
✓ Only works on sorted arrays
"""