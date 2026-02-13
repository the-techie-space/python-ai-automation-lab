"""
Arrays & Lists - Two Pointers Technique
=========================================
Master the two-pointer pattern for efficient array problems
"""

# ============================================================================
# WHAT IS TWO POINTERS?
# ============================================================================
"""
Two Pointers = Using two references to traverse array efficiently

Common Patterns:
1. Opposite Direction (left & right converge)
2. Same Direction (slow & fast pointers)
3. Sliding Window (dynamic range)

Benefits:
- Reduces time complexity from O(n²) to O(n)
- Avoids extra space usage
- Clean and intuitive solutions
"""

# ============================================================================
# PATTERN 1: OPPOSITE DIRECTION
# ============================================================================

# Problem: Two Sum in Sorted Array
def two_sum_sorted(arr, target):
    """
    Find if any two numbers sum to target
    
    Args:
        arr: Sorted array of integers
        target: Target sum
    
    Returns:
        bool: True if pair exists
    
    Time: O(n), Space: O(1)
    
    Example:
        arr = [1, 2, 3, 4, 5], target = 9
        left=0, right=4: 1+5=6 < 9 → move left
        left=1, right=4: 2+5=7 < 9 → move left
        left=2, right=4: 3+5=8 < 9 → move left
        left=3, right=4: 4+5=9 ✓
    """
    left = 0
    right = len(arr) - 1
    
    while left < right:
        current_sum = arr[left] + arr[right]
        
        if current_sum == target:
            print(f"Found pair: {arr[left]} + {arr[right]} = {target}")
            return True
        elif current_sum < target:
            left += 1  # Need larger sum
        else:
            right -= 1  # Need smaller sum
    
    return False

# Test
print("--- Two Sum in Sorted Array ---")
print("Array: [1, 2, 3, 4, 5], Target: 9")
two_sum_sorted([1, 2, 3, 4, 5], 9)  # True: 4 + 5

print("\nArray: [1, 2, 3, 4, 5], Target: 10")
print(two_sum_sorted([1, 2, 3, 4, 5], 10))  # False

print("\nArray: [1, 3, 5, 7, 9], Target: 12")
two_sum_sorted([1, 3, 5, 7, 9], 12)  # True: 3 + 9

# ============================================================================
# PATTERN 2: SAME DIRECTION (Slow & Fast)
# ============================================================================

# Problem: Move Zeros to End
def move_zeros(arr):
    """
    Move all zeros to end while maintaining order of non-zeros
    
    Args:
        arr: List of integers
    
    Returns:
        list: Modified array
    
    Time: O(n), Space: O(1)
    
    Visualization:
        [0, 1, 0, 3, 12]
         ↑  ↑
        slow fast
        
        Step 1: fast=1, num=1 (non-zero)
                → swap arr[0] and arr[1]
                → [1, 0, 0, 3, 12]
                → slow=1
        
        Step 2: fast=3, num=3 (non-zero)
                → swap arr[1] and arr[3]
                → [1, 3, 0, 0, 12]
                → slow=2
        
        Step 3: fast=4, num=12 (non-zero)
                → swap arr[2] and arr[4]
                → [1, 3, 12, 0, 0]
                → slow=3
    """
    slow = 0  # Position for next non-zero
    
    for fast in range(len(arr)):
        if arr[fast] != 0:
            arr[slow], arr[fast] = arr[fast], arr[slow]
            slow += 1
    
    return arr

# Test
print("\n--- Move Zeros to End ---")
test_cases = [
    [0, 1, 0, 3, 12],
    [0, 0, 1],
    [1, 2, 3, 0, 0, 0],
]

for arr in test_cases:
    original = arr.copy()
    move_zeros(arr)
    print(f"{original} → {arr}")

# Problem: Remove Duplicates from Sorted Array
def remove_duplicates(arr):
    """
    Remove duplicates in-place, return new length
    
    Args:
        arr: Sorted array
    
    Returns:
        int: Length of unique elements
    
    Time: O(n), Space: O(1)
    
    Visualization:
        [1, 1, 2, 2, 3]
         ↑  ↑
        slow fast
        
        Step 1: fast=1, arr[1]=1 (duplicate)
                → skip
        
        Step 2: fast=2, arr[2]=2 (new)
                → slow=1, arr[1]=2
                → [1, 2, 2, 2, 3]
        
        Step 3: fast=3, arr[3]=2 (duplicate)
                → skip
        
        Step 4: fast=4, arr[4]=3 (new)
                → slow=2, arr[2]=3
                → [1, 2, 3, 2, 3]
    """
    if len(arr) == 0:
        return 0
    
    slow = 0
    
    for fast in range(1, len(arr)):
        if arr[fast] != arr[slow]:
            slow += 1
            arr[slow] = arr[fast]
    
    return slow + 1

# Test
print("\n--- Remove Duplicates ---")
test_arr = [1, 1, 2, 2, 2, 3, 4, 4, 5]
original = test_arr.copy()
length = remove_duplicates(test_arr)
print(f"Original: {original}")
print(f"After: {test_arr[:length]}")
print(f"New length: {length}")

# ============================================================================
# ADVANCED: THREE POINTER
# ============================================================================

# Problem: Three Sum (find all triplets that sum to zero)
def three_sum(arr):
    """
    Find all unique triplets that sum to zero
    
    Args:
        arr: Array of integers
    
    Returns:
        list: List of triplets
    
    Time: O(n²), Space: O(1) (excluding output)
    
    Strategy:
        1. Sort the array
        2. Fix one number (i)
        3. Use two pointers for remaining two numbers
    """
    arr.sort()
    result = []
    n = len(arr)
    
    for i in range(n - 2):
        # Skip duplicates for first number
        if i > 0 and arr[i] == arr[i - 1]:
            continue
        
        left = i + 1
        right = n - 1
        target = -arr[i]  # We want arr[i] + arr[left] + arr[right] = 0
        
        while left < right:
            current_sum = arr[left] + arr[right]
            
            if current_sum == target:
                result.append([arr[i], arr[left], arr[right]])
                
                # Skip duplicates for second number
                while left < right and arr[left] == arr[left + 1]:
                    left += 1
                # Skip duplicates for third number
                while left < right and arr[right] == arr[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    
    return result

# Test
print("\n--- Three Sum ---")
test_arr = [-1, 0, 1, 2, -1, -4]
print(f"Array: {test_arr}")
result = three_sum(test_arr)
print(f"Triplets that sum to 0: {result}")
# Output: [[-1, -1, 2], [-1, 0, 1]]

# ============================================================================
# PATTERN COMPARISON
# ============================================================================

print("\n" + "="*60)
print("TWO POINTER PATTERNS SUMMARY")
print("="*60)

patterns = """
1. OPPOSITE DIRECTION (Converging)
   ├─ Use when: Sorted array, finding pairs/sums
   ├─ Movement: left++, right--
   └─ Example: Two Sum, Three Sum

2. SAME DIRECTION (Slow & Fast)
   ├─ Use when: Removing/moving elements, duplicates
   ├─ Movement: Both move forward, fast faster
   └─ Example: Remove duplicates, Move zeros

3. SLIDING WINDOW (Dynamic range)
   ├─ Use when: Subarrays, consecutive elements
   ├─ Movement: Expand right, shrink left
   └─ Example: Max sum subarray, longest substring
"""

print(patterns)

# ============================================================================
# PRACTICE PROBLEMS
# ============================================================================

print("\n--- Practice These Problems ---")
problems = """
Easy:
✓ Remove duplicates from sorted array
✓ Move zeros to end
✓ Two sum in sorted array
✓ Valid palindrome (string)

Medium:
✓ Three sum
✓ Container with most water
✓ Trapping rain water
✓ Sort colors (Dutch flag problem)

Hard:
✓ Four sum
✓ Minimum window substring
✓ Longest substring without repeating
"""
print(problems)

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================
"""
TWO POINTERS:
✓ Opposite direction: O(n²) → O(n) for pair problems
✓ Same direction: In-place modifications
✓ Always consider: sorted vs unsorted
✓ Watch for: duplicates, edge cases

WHEN TO USE:
✓ "Find pair/triplet with sum X"
✓ "Remove/move elements in-place"
✓ "Reverse or partition array"
✓ Array is sorted (big hint!)

TIME COMPLEXITY:
✓ Usually O(n) for single pass
✓ O(n²) when nested (like three sum)
✓ Space: O(1) - no extra arrays needed!
"""