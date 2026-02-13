"""
Hash Maps - Two Sum & Complement Patterns
==========================================
Master the most important interview problem pattern!
"""

# ============================================================================
# THE TWO SUM PROBLEM - #1 INTERVIEW QUESTION ⭐⭐⭐
# ============================================================================
"""
This is THE most asked coding interview question!

Problem:
Given an array of numbers and a target, find two numbers that add up to target.
Return their indices.

Example:
    Input: nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]
    Explanation: nums[0] + nums[1] = 2 + 7 = 9
"""

print("="*60)
print("TWO SUM - The Most Important Interview Problem")
print("="*60)

# ============================================================================
# NAIVE SOLUTION - Brute Force O(n²)
# ============================================================================

def two_sum_brute_force(nums, target):
    """
    Brute force: Try every pair
    
    Time: O(n²) - TOO SLOW! ❌
    Space: O(1)
    
    Don't use this in interviews unless specifically asked!
    """
    n = len(nums)
    
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    
    return None

# ============================================================================
# OPTIMAL SOLUTION - Hash Map O(n) ✅
# ============================================================================

def two_sum(nums, target):
    """
    Use hash map to find complement
    
    Args:
        nums: List of integers
        target: Target sum
    
    Returns:
        list: Indices of two numbers that sum to target
    
    Time: O(n) - FAST! ✅
    Space: O(n)
    
    Strategy:
        For each number, check if (target - number) exists in hash map
        This is called finding the "complement"
    """
    seen = {}  # num → index
    
    for i, num in enumerate(nums):
        complement = target - num
        
        # Check if complement exists
        if complement in seen:
            return [seen[complement], i]
        
        # Store current number and its index
        seen[num] = i
    
    return None

# ============================================================================
# STEP-BY-STEP VISUALIZATION
# ============================================================================

def two_sum_with_visualization(nums, target):
    """Show how Two Sum works step by step"""
    print(f"\nFinding two numbers that sum to {target} in {nums}")
    print("-" * 60)
    
    seen = {}
    
    for i, num in enumerate(nums):
        complement = target - num
        
        print(f"\nStep {i+1}: num={num}, index={i}")
        print(f"  Complement needed: {target} - {num} = {complement}")
        print(f"  Current seen dict: {seen}")
        
        if complement in seen:
            print(f"  ✓ Found! {complement} exists at index {seen[complement]}")
            print(f"  Solution: [{seen[complement]}, {i}]")
            return [seen[complement], i]
        
        print(f"  ✗ Not found. Adding {num} → {i} to seen dict")
        seen[num] = i
    
    print("\nNo solution found")
    return None

# Test with visualization
print("\n--- Visualization Example ---")
result = two_sum_with_visualization([2, 7, 11, 15], 9)

# ============================================================================
# TEST CASES
# ============================================================================
print("\n" + "="*60)
print("TWO SUM - Test Cases")
print("="*60)

test_cases = [
    ([2, 7, 11, 15], 9),
    ([3, 2, 4], 6),
    ([3, 3], 6),
    ([1, 5, 3, 7, 9], 12),
]

for nums, target in test_cases:
    result_hash = two_sum(nums, target)
    result_brute = two_sum_brute_force(nums, target)
    print(f"\nnums={nums}, target={target}")
    print(f"  Hash map solution: {result_hash}")
    print(f"  Brute force verification: {result_brute}")

# ============================================================================
# VARIATION 1: RETURN VALUES INSTEAD OF INDICES
# ============================================================================
print("\n" + "="*60)
print("VARIATION 1: Return Values (Not Indices)")
print("="*60)

def two_sum_values(nums, target):
    """
    Return the actual values instead of indices
    
    Returns:
        list: The two numbers that sum to target
    """
    seen = set()
    
    for num in nums:
        complement = target - num
        
        if complement in seen:
            return [complement, num]
        
        seen.add(num)
    
    return None

# Test
nums = [2, 7, 11, 15]
target = 9
result = two_sum_values(nums, target)
print(f"\nnums={nums}, target={target}")
print(f"Values that sum to {target}: {result}")

# ============================================================================
# VARIATION 2: FIND ALL PAIRS (Not Just First)
# ============================================================================
print("\n" + "="*60)
print("VARIATION 2: Find All Pairs")
print("="*60)

def two_sum_all_pairs(nums, target):
    """
    Find all pairs that sum to target
    
    Returns:
        list: All pairs [i, j] where nums[i] + nums[j] = target
    """
    seen = {}
    pairs = []
    
    for i, num in enumerate(nums):
        complement = target - num
        
        if complement in seen:
            # Found a pair! Add it
            pairs.append([seen[complement], i])
        
        seen[num] = i
    
    return pairs

# Test
nums = [1, 3, 2, 2, 4, 3]
target = 5
result = two_sum_all_pairs(nums, target)
print(f"\nnums={nums}, target={target}")
print(f"All pairs: {result}")

# ============================================================================
# VARIATION 3: COUNT PAIRS
# ============================================================================
print("\n" + "="*60)
print("VARIATION 3: Count Pairs")
print("="*60)

def count_pairs(nums, target):
    """
    Count how many pairs sum to target
    
    Returns:
        int: Number of pairs
    """
    seen = {}
    count = 0
    
    for num in nums:
        complement = target - num
        
        if complement in seen:
            count += seen[complement]  # Add how many times complement appears
        
        seen[num] = seen.get(num, 0) + 1
    
    return count

# Test
nums = [1, 1, 1, 1]
target = 2
result = count_pairs(nums, target)
print(f"\nnums={nums}, target={target}")
print(f"Number of pairs: {result}")

# ============================================================================
# VARIATION 4: TWO SUM - SORTED ARRAY
# ============================================================================
print("\n" + "="*60)
print("VARIATION 4: Two Sum in Sorted Array")
print("="*60)

def two_sum_sorted(nums, target):
    """
    If array is sorted, can use two pointers instead!
    
    Time: O(n), Space: O(1) - Even better space!
    
    But hash map works for both sorted and unsorted
    """
    left = 0
    right = len(nums) - 1
    
    while left < right:
        current_sum = nums[left] + nums[right]
        
        if current_sum == target:
            return [left, right]
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return None

# Test
nums = [1, 2, 3, 4, 5, 6]
target = 9
result = two_sum_sorted(nums, target)
print(f"\nSorted nums={nums}, target={target}")
print(f"Indices: {result}")

# ============================================================================
# RELATED PROBLEM: THREE SUM (Extension)
# ============================================================================
print("\n" + "="*60)
print("EXTENSION: Three Sum (Brief Overview)")
print("="*60)

def three_sum_zero(nums):
    """
    Find all triplets that sum to zero
    
    Strategy: Fix one number, use Two Sum for the rest
    
    Time: O(n²)
    """
    nums.sort()
    result = []
    n = len(nums)
    
    for i in range(n - 2):
        # Skip duplicates
        if i > 0 and nums[i] == nums[i - 1]:
            continue
        
        # Use two pointers for remaining elements
        left = i + 1
        right = n - 1
        target = -nums[i]
        
        while left < right:
            current_sum = nums[left] + nums[right]
            
            if current_sum == target:
                result.append([nums[i], nums[left], nums[right]])
                
                # Skip duplicates
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
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
nums = [-1, 0, 1, 2, -1, -4]
result = three_sum_zero(nums)
print(f"\nNums: {nums}")
print(f"Triplets that sum to 0: {result}")

# ============================================================================
# COMPLEMENT PATTERN - General Template
# ============================================================================
print("\n" + "="*60)
print("THE COMPLEMENT PATTERN - General Template")
print("="*60)

template = """
COMPLEMENT PATTERN TEMPLATE:

def find_complement_pair(nums, target):
    '''
    Find pair where: nums[i] + nums[j] = target
    OR any other operation: nums[i] * nums[j] = target, etc.
    '''
    seen = {}  # or set(), depending on what you need
    
    for i, num in enumerate(nums):
        # Calculate what you're looking for
        complement = target - num  # or target / num, etc.
        
        # Check if complement exists
        if complement in seen:
            return [seen[complement], i]  # or return values
        
        # Store current element
        seen[num] = i  # or seen.add(num)
    
    return None

KEY POINTS:
✓ Calculate complement: what you need to find
✓ Check if complement already seen: O(1) lookup
✓ Store current element for future checks
✓ Return as soon as found (or collect all)
"""
print(template)

# ============================================================================
# PRACTICE PROBLEMS
# ============================================================================
print("\n" + "="*60)
print("RELATED PRACTICE PROBLEMS")
print("="*60)

practice = """
EASY:
✓ Two Sum (this problem!)
✓ Two Sum II - Input array is sorted
✓ Contains Duplicate
✓ Valid Anagram

MEDIUM:
✓ Two Sum - All pairs
✓ Three Sum
✓ Four Sum
✓ Subarray Sum Equals K

HARD:
✓ Two Sum - Count pairs
✓ 4Sum II
✓ Max Points on a Line
"""
print(practice)

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================
"""
TWO SUM PATTERN:
✓ Most asked interview question
✓ Brute force: O(n²) - Don't use!
✓ Hash map: O(n) - Optimal solution!

THE COMPLEMENT IDEA:
✓ For each number, look for (target - number)
✓ Hash map gives O(1) lookup
✓ Total time: O(n)

IMPLEMENTATION:
1. Create seen dictionary (num → index)
2. For each number:
   - Calculate complement = target - num
   - Check if complement in seen
   - If yes: return [seen[complement], current_index]
   - If no: add current to seen

VARIATIONS:
✓ Return indices vs values
✓ Find one pair vs all pairs
✓ Count pairs
✓ Sorted array (can use two pointers)
✓ Three sum, four sum (extensions)

WHY IT WORKS:
✓ Hash map stores all previous numbers
✓ For each new number, check if its complement was seen before
✓ If yes, we found our pair!
✓ O(1) lookup makes it O(n) overall

INTERVIEW TIPS:
✓ Start by stating brute force (shows you understand)
✓ Then explain hash map optimization
✓ Mention time/space complexity
✓ Handle edge cases: empty array, no solution, duplicates
✓ Ask if array is sorted (two pointers might work)
"""

print("\n" + "="*60)
print("✓ Two Sum pattern mastered!")
print("="*60)