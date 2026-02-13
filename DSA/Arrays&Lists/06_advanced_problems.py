"""
Arrays & Lists - Advanced Problems
====================================
Master challenging array problems combining multiple techniques
"""

import heapq
from typing import List

# ============================================================================
# PROBLEM 1: THREE SUM - Find All Triplets
# ============================================================================
"""
Find all unique triplets that sum to zero
Combines: Sorting + Two Pointers + Duplicate Handling
"""

def three_sum(nums: List[int]) -> List[List[int]]:
    """
    Find all unique triplets [a, b, c] where a + b + c = 0
    
    Args:
        nums: List of integers
    
    Returns:
        List of triplets
    
    Time: O(n²), Space: O(1) (excluding output)
    
    Strategy:
        1. Sort array
        2. Fix first number (i)
        3. Use two pointers for remaining two numbers
        4. Skip duplicates to ensure unique triplets
    
    Example:
        [-1, 0, 1, 2, -1, -4]
        
        After sort: [-4, -1, -1, 0, 1, 2]
        
        i=0, num=-4: target=4, no valid pairs
        i=1, num=-1: target=1
            left=-1, right=2 → sum=1 ✓
            left=0, right=1 → sum=1 ✓
        i=2: skip (duplicate -1)
        i=3, num=0: target=0, no valid pairs
    """
    nums.sort()
    result = []
    n = len(nums)
    
    for i in range(n - 2):
        # Skip duplicates for first number
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        left = i + 1
        right = n - 1
        target = -nums[i]  # We want nums[i] + nums[left] + nums[right] = 0
        
        while left < right:
            current_sum = nums[left] + nums[right]
            
            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates for second number
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                # Skip duplicates for third number
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1
                
                left += 1
                right -= 1
            elif current_sum < target:
                left += 1
            else:
                right -= 1
    
    return result

# Test
print("="*60)
print("PROBLEM 1: THREE SUM")
print("="*60)
test_arr = [-1, 0, 1, 2, -1, -4]
print(f"Input: {test_arr}")
result = three_sum(test_arr)
print(f"Output: {result}")
print("Expected: [[-1, -1, 2], [-1, 0, 1]]")

# ============================================================================
# PROBLEM 2: CONTAINER WITH MOST WATER
# ============================================================================
"""
Find two lines that form container holding maximum water
Combines: Two Pointers (Opposite Direction) + Greedy Logic
"""

def max_area(height: List[int]) -> int:
    """
    Find maximum water container can hold
    
    Args:
        height: Array of line heights
    
    Returns:
        int: Maximum area
    
    Time: O(n), Space: O(1)
    
    Strategy:
        Use two pointers from both ends
        Area = min(height[left], height[right]) * distance
        Move the pointer with smaller height (greedy)
    
    Example:
        [1, 8, 6, 2, 5, 4, 8, 3, 7]
         ↑                       ↑
        left                   right
        
        Area = min(1, 7) * 8 = 8
        Move left (smaller height)
        
        Continue until pointers meet
    """
    left = 0
    right = len(height) - 1
    max_water = 0
    
    while left < right:
        # Calculate current area
        width = right - left
        current_height = min(height[left], height[right])
        current_area = width * current_height
        
        # Update maximum
        max_water = max(max_water, current_area)
        
        # Move pointer with smaller height
        if height[left] < height[right]:
            left += 1
        else:
            right -= 1
    
    return max_water

# Test
print("\n" + "="*60)
print("PROBLEM 2: CONTAINER WITH MOST WATER")
print("="*60)
heights = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(f"Heights: {heights}")
result = max_area(heights)
print(f"Max water: {result}")
print("Expected: 49 (between heights 8 and 7)")

# ============================================================================
# PROBLEM 3: TRAPPING RAIN WATER
# ============================================================================
"""
Calculate how much water can be trapped after raining
Combines: Dynamic Programming + Two Pointers
"""

def trap_water(height: List[int]) -> int:
    """
    Calculate trapped rainwater
    
    Args:
        height: Elevation map
    
    Returns:
        int: Total water trapped
    
    Time: O(n), Space: O(1)
    
    Strategy:
        Water at position i = min(max_left, max_right) - height[i]
        Use two pointers to track max heights from both sides
    
    Example:
        [0,1,0,2,1,0,1,3,2,1,2,1]
         ░░░██░░████░████░██
         Water trapped at each position:
         0 at index 0 (no left wall)
         0 at index 1 (height=1, max_left=0, max_right=3, water=0)
         1 at index 2 (height=0, max_left=1, max_right=3, water=1)
         ...
    """
    if not height:
        return 0
    
    left = 0
    right = len(height) - 1
    left_max = height[left]
    right_max = height[right]
    water = 0
    
    while left < right:
        if height[left] < height[right]:
            left += 1
            left_max = max(left_max, height[left])
            water += left_max - height[left]
        else:
            right -= 1
            right_max = max(right_max, height[right])
            water += right_max - height[right]
    
    return water

# Test
print("\n" + "="*60)
print("PROBLEM 3: TRAPPING RAIN WATER")
print("="*60)
elevation = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]
print(f"Elevation: {elevation}")
result = trap_water(elevation)
print(f"Water trapped: {result}")
print("Expected: 6")

# ============================================================================
# PROBLEM 4: PRODUCT OF ARRAY EXCEPT SELF
# ============================================================================
"""
Calculate product of all elements except current one
Combines: Prefix/Suffix Products
"""

def product_except_self(nums: List[int]) -> List[int]:
    """
    Return array where answer[i] = product of all nums except nums[i]
    
    Args:
        nums: List of integers
    
    Returns:
        List of products
    
    Time: O(n), Space: O(1) (output doesn't count)
    
    Strategy:
        Use two passes:
        1. Calculate prefix products (left to right)
        2. Calculate suffix products (right to left)
    
    Example:
        [1, 2, 3, 4]
        
        Prefix:  [1, 1, 2, 6]
        Suffix:  [24, 12, 4, 1]
        Result:  [24, 12, 8, 6]
    """
    n = len(nums)
    result = [1] * n
    
    # Calculate prefix products
    prefix = 1
    for i in range(n):
        result[i] = prefix
        prefix *= nums[i]
    
    # Calculate suffix products and multiply
    suffix = 1
    for i in range(n - 1, -1, -1):
        result[i] *= suffix
        suffix *= nums[i]
    
    return result

# Test
print("\n" + "="*60)
print("PROBLEM 4: PRODUCT EXCEPT SELF")
print("="*60)
nums = [1, 2, 3, 4]
print(f"Input: {nums}")
result = product_except_self(nums)
print(f"Output: {result}")
print("Expected: [24, 12, 8, 6]")

# ============================================================================
# PROBLEM 5: MAXIMUM SUBARRAY SUM (Kadane's Algorithm)
# ============================================================================
"""
Find contiguous subarray with largest sum
Combines: Dynamic Programming + Greedy
"""

def max_subarray_sum(nums: List[int]) -> int:
    """
    Find maximum sum of contiguous subarray
    
    Args:
        nums: List of integers
    
    Returns:
        int: Maximum sum
    
    Time: O(n), Space: O(1)
    
    Strategy (Kadane's Algorithm):
        At each position, decide:
        - Continue current subarray (add to current_sum)
        - Start new subarray (take only current element)
    
    Example:
        [-2, 1, -3, 4, -1, 2, 1, -5, 4]
        
        i=0: current=-2, max=-2
        i=1: current=1 (start new), max=1
        i=2: current=-2, max=1
        i=3: current=4 (start new), max=4
        i=4: current=3, max=4
        i=5: current=5, max=5
        i=6: current=6, max=6
        i=7: current=1, max=6
        i=8: current=5, max=6
    """
    max_sum = nums[0]
    current_sum = nums[0]
    
    for i in range(1, len(nums)):
        # Either extend current subarray or start new
        current_sum = max(nums[i], current_sum + nums[i])
        max_sum = max(max_sum, current_sum)
    
    return max_sum

# Test
print("\n" + "="*60)
print("PROBLEM 5: MAXIMUM SUBARRAY SUM (Kadane's)")
print("="*60)
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(f"Input: {nums}")
result = max_subarray_sum(nums)
print(f"Max sum: {result}")
print("Expected: 6 (subarray [4, -1, 2, 1])")

# ============================================================================
# PROBLEM 6: MERGE INTERVALS
# ============================================================================
"""
Merge overlapping intervals
Combines: Sorting + Greedy Merging
"""

def merge_intervals(intervals: List[List[int]]) -> List[List[int]]:
    """
    Merge overlapping intervals
    
    Args:
        intervals: List of [start, end] intervals
    
    Returns:
        List of merged intervals
    
    Time: O(n log n), Space: O(n)
    
    Example:
        [[1,3], [2,6], [8,10], [15,18]]
        
        After sort: [[1,3], [2,6], [8,10], [15,18]]
        
        Merge [1,3] and [2,6] → [1,6]
        [8,10] doesn't overlap
        [15,18] doesn't overlap
        
        Result: [[1,6], [8,10], [15,18]]
    """
    if not intervals:
        return []
    
    # Sort by start time
    intervals.sort(key=lambda x: x[0])
    
    merged = [intervals[0]]
    
    for current in intervals[1:]:
        last = merged[-1]
        
        # Check if overlaps
        if current[0] <= last[1]:
            # Merge by extending end time
            merged[-1] = [last[0], max(last[1], current[1])]
        else:
            # No overlap, add as new interval
            merged.append(current)
    
    return merged

# Test
print("\n" + "="*60)
print("PROBLEM 6: MERGE INTERVALS")
print("="*60)
intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
print(f"Input: {intervals}")
result = merge_intervals(intervals)
print(f"Output: {result}")
print("Expected: [[1, 6], [8, 10], [15, 18]]")

# ============================================================================
# COMPLEXITY SUMMARY
# ============================================================================

print("\n" + "="*60)
print("TIME & SPACE COMPLEXITY SUMMARY")
print("="*60)

summary = """
Problem                      Time         Space    Technique
────────────────────────────────────────────────────────────
Three Sum                    O(n²)        O(1)     Sort + 2-Pointer
Container Water              O(n)         O(1)     2-Pointer
Trapping Rain Water          O(n)         O(1)     2-Pointer + Max
Product Except Self          O(n)         O(1)     Prefix/Suffix
Max Subarray (Kadane)        O(n)         O(1)     DP + Greedy
Merge Intervals              O(n log n)   O(n)     Sort + Merge
"""

print(summary)

# ============================================================================
# KEY PATTERNS TO REMEMBER
# ============================================================================

print("\n" + "="*60)
print("KEY PATTERNS")
print("="*60)

patterns = """
1. TWO POINTERS
   ├─ Opposite Direction: Two Sum, Container Water
   └─ Same Direction: Remove Duplicates, Move Zeros

2. SORTING + PROCESSING
   ├─ Three Sum (sort then 2-pointer)
   └─ Merge Intervals (sort by start time)

3. PREFIX/SUFFIX ARRAYS
   └─ Product Except Self, Trapping Rain Water

4. KADANE'S ALGORITHM
   └─ Maximum Subarray Sum (DP pattern)

5. GREEDY APPROACHES
   ├─ Container Water (move smaller height)
   └─ Merge Intervals (always merge overlapping)
"""

print(patterns)

print("\n✓ Master these 6 problems to understand core array techniques!")