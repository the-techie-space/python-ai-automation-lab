"""
# 📊 **QUICK REFERENCE SUMMARY**

---
```
┌──────────────────────────────────────────────────────┐
│ Pattern          │ Key Problems                      │
├──────────────────────────────────────────────────────┤
│ Two Pointers     │ Reverse, Palindrome, Remove Dups │
│ N-Sum            │ 2Sum, 3Sum, 4Sum                  │
│ Sliding (Fixed)  │ Max Sum K, Anagrams               │
│ Sliding (Var)    │ Longest Substr, Min Window        │
│ Prefix Sum       │ Range Sum, Subarray Sum = K       │
│ Kadane's         │ Max Subarray, Stock Profit        │
│ Binary Basic     │ Search, Insert Position           │
│ Binary Answer    │ Koko Bananas, Ship Packages       │
│ Rotated Array    │ Search Rotated, Find Min          │
│ Peak Element     │ Find Peak                         │
└──────────────────────────────────────────────────────┘
```

---

---

# 🏆 **TOP 20 MUST-KNOW PROBLEMS**

---
```
⭐⭐⭐⭐⭐ MUST DO (Interview Favorites):

1. Two Sum (LC 1)
2. 3Sum (LC 15)
3. Container With Most Water (LC 11)
4. Longest Substring Without Repeat (LC 3)
5. Subarray Sum Equals K (LC 560)
6. Maximum Subarray (Kadane's) (LC 53)
7. Product Except Self (LC 238)
8. Binary Search (LC 704)
9. Search in Rotated Array (LC 33)
10. Koko Eating Bananas (LC 875)

⭐⭐⭐⭐ Very Important:

11. Remove Duplicates (LC 26)
12. Find All Anagrams (LC 438)
13. Maximum Product Subarray (LC 152)
14. Find Min in Rotated Array (LC 153)
15. Smallest Subarray Sum (LC 209)
16. Valid Palindrome (LC 125)
17. Move Zeros (LC 283)
18. Search Insert Position (LC 35)
19. Find Peak Element (LC 162)
20. Split Array Largest Sum (LC 410)
```

---

"""


# 1️⃣ TWO POINTERS

# def two_pointer_template(arr):
#     left = 0
#     right = len(arr) - 1
    
#     while left < right:
#         # Process elements
#         # Move pointers based on condition
#         if condition:
#             left += 1
#         else:
#             right -= 1

# Reverse Array

def reverse_array(arr):
    "Reverse array using two pointers"
    left = 0
    right = len(arr) - 1
    
    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    
    return arr

print(reverse_array([1, 2, 3, 4, 5]))
# [5, 4, 3, 2, 1]

# Valid Palindrome

def is_palindrome(s):
    "Check if string is palindrome"
    left = 0
    right = len(s) - 1
    
    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1
    
    return True

print(is_palindrome("racecar"))  # True
print(is_palindrome("hello"))    # False

# Remove Duplicates from Sorted Array

def remove_duplicates(arr):
    """Remove duplicates in-place, return new length"""
    if not arr:
        return 0
    
    left = 0  # Slow pointer
    
    for right in range(1, len(arr)):  # Fast pointer
        if arr[right] != arr[left]:
            left += 1
            arr[left] = arr[right]
    
    return left + 1

arr = [1, 1, 2, 2, 3, 4, 4]
length = remove_duplicates(arr)
print(arr[:length])  # [1, 2, 3, 4]

# Move Zeros to End

def move_zeros(arr):
    """Move all zeros to end, maintain order"""
    left = 0  # Position for non-zero
    
    for right in range(len(arr)):
        if arr[right] != 0:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
    
    return arr

print(move_zeros([0, 1, 0, 3, 12]))
# [1, 3, 12, 0, 0]

"""

## **Problems:**

### **Easy:**
```
1. ✅ Reverse Array/String
   arr = [1,2,3,4,5] → [5,4,3,2,1]
   
2. ✅ Valid Palindrome (LC 125)
   "A man, a plan, a canal: Panama" → True
   
3. ✅ Remove Duplicates from Sorted Array (LC 26)
   [1,1,2,2,3] → [1,2,3]
   
4. ✅ Move Zeros to End (LC 283)
   [0,1,0,3,12] → [1,3,12,0,0]
   
5. ✅ Remove Element (LC 27)
   arr=[3,2,2,3], val=3 → [2,2]
```

### **Medium:**
```
6. ✅ Container With Most Water (LC 11)
   Find max area between two lines
   
7. ✅ 3Sum (LC 15)
   Find triplets that sum to 0
   
8. ✅ Sort Colors (LC 75)
   Sort [2,0,2,1,1,0] in-place

"""

# 2️⃣ N-SUM PROBLEMS

# N-Sum needs (N - 2) nested loops + Two Pointers

# 2-Sum: 2 - 2 = 0 loops  → Just two pointers
# 3-Sum: 3 - 2 = 1 loop   → i + two pointers
# 4-Sum: 4 - 2 = 2 loops  → i, j + two pointers
# 5-Sum: 5 - 2 = 3 loops  → i, j, k + two pointers


def two_sum(nums, target):
    # step1 do sort
    nums.sort()
    result = []
    n = len(nums)
    
    # step2 N-2 nested loops (for 2sum 0 Nested loops)
    left = 0
    right = n-1

    # remaining_target = target - nums[i] 
    # here no nested loops for iterating for 2sum so no remaining target direct target
    while left<right:
        two_sum = nums[left] + nums[right]

        if two_sum == target:
            result.append([nums[left], nums[right]])

            # Skip duplicates
            while left < right and nums[left] == nums[left+1]:
                left += 1
            while left < right and nums[right] == nums[right-1]:
                right -= 1
            left+=1
            right-=1
        elif two_sum < target:
            left+=1
        else:
            right-=1
    return result

print(two_sum([2,-4,5,6,2,0,1], 4))
# Output: [[-4, 8]] or pairs that sum to 4
"""

---

### **Your Key Points:**
```
✅ 2 - 2 = 0 loops needed
✅ Just use left and right pointers
✅ No remaining_target (use target directly)
✅ Skip duplicates with while loops

"""
def three_sum(nums, target):
    # step1 sort the given list
    nums.sort()
    result = []
    n = len(nums)

    # step2 N-2 nested loops
    # writing for 3sum N-2=3-2=1 nested loop(i)
    for i in range(n-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        left = i + 1
        right = n-1

        remaining_target = target - nums[i]
        while left < right:
            two_sum = nums[left] + nums[right]

            if two_sum == remaining_target:
                result.append([nums[i], nums[left], nums[right]])

                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1

            elif two_sum < remaining_target:
                left += 1
            else:
                right -= 1

    return result
            
print(three_sum([1,-3,4,5,6], 2))
# Output: Triplets that sum to 2
"""

---

### **Your Key Points:**
```
✅ 3 - 2 = 1 loop (i)
✅ Fix one number (i)
✅ Use two pointers for remaining two
✅ remaining_target = target - nums[i]
✅ Skip duplicates at i, left, and right

"""

def four_sum(nums, target):
    # step1 do sort
    nums.sort()
    result = []
    n = len(nums)

    # step2 N-2 nested loops 
    # (here for 4sum 4-2 = 2 nested loops we need i.e.., i and j)
    # fix 1 number then two pointer, next do the same process we done for 3sum
    for i in range(n-3):
        if i > 0 and nums[i] == nums[i-1]:  # remove the duplicates
            continue

        for j in range(i+1, n-2):
            if j > i+1 and nums[j] == nums[j-1]:
                continue

            left = j+1
            right = n-1

            remaining_target = target-nums[i]-nums[j]

            while left < right:
                two_sum = nums[left]+ nums[right]

                if two_sum == remaining_target:
                    result.append([nums[i], nums[j], nums[left], nums[right]])

                    while left<right and nums[left] == nums[left+1]:
                        left += 1
                    while left<right and nums[right] == nums[right-1]:
                        right -= 1
                    left+=1
                    right-=1
                elif two_sum< remaining_target:
                    left+=1
                else:
                    right-=1
    return result

print(four_sum([2,3,5,1,-5,-2,0], 4))
# Output: Quadruplets that sum to 4
"""
---

### **Your Key Points:**
```
✅ 4 - 2 = 2 loops (i and j)
✅ Fix two numbers (i, j)
✅ Use two pointers for remaining two
✅ remaining_target = target - nums[i] - nums[j]
✅ Skip duplicates at all levels

"""

def five_sum(nums, target):
    #step1 sort nums
    nums.sort()
    result = []
    n = len(nums)

    # step2 N-2 nested loops (for 5sum 5-2 = 3 nested loops i.e.., i,j,k)
    for i in range(n-4):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        for j in range(i+1, n-3):
            if j > i+1 and nums[j] == nums[j-1]:
                continue
            for k in range(j+1, n-2):
                if k > j+1 and nums[k] == nums[k-1]:
                    continue

                left = k+1
                right = n-1

                remaining_target = target-nums[i]-nums[j]-nums[k]

                while left < right:
                    two_sum = nums[left]+nums[right]

                    if two_sum == remaining_target:
                        result.append([nums[i], nums[j], nums[k], 
                                     nums[left], nums[right]])

                        while left < right and nums[left] == nums[left+1]:
                            left+=1
                        while left < right and nums[right] == nums[right-1]:
                            right -= 1

                        left+=1
                        right-=1
                    elif two_sum < remaining_target:
                        left+=1
                    else:
                        right-=1
    return result

print(five_sum([1,2,3,4,5], 15))
# Output: [[1, 2, 3, 4, 5]]
"""

---

### **Your Key Points:**
```
✅ 5 - 2 = 3 loops (i, j, k)
✅ Fix three numbers (i, j, k)
✅ Use two pointers for remaining two
✅ remaining_target = target - nums[i] - nums[j] - nums[k]
✅ Skip duplicates at all levels
```

---

---

# 📊 **YOUR N-SUM PATTERN SUMMARY**

---
```
┌────────────────────────────────────────────────────────┐
│ N-Sum │ Loops │ Fixed    │ Two Pointers │ Remaining   │
├────────────────────────────────────────────────────────┤
│ 2-Sum │   0   │ None     │ left, right  │ target      │
│ 3-Sum │   1   │ i        │ left, right  │ target - i  │
│ 4-Sum │   2   │ i, j     │ left, right  │ target-i-j  │
│ 5-Sum │   3   │ i, j, k  │ left, right  │ target-i-j-k│
└────────────────────────────────────────────────────────┘

"""

def n_sum(nums, target, n):
    """
    Your pattern for ANY N-Sum!
    
    Steps:
    1. Sort array
    2. Use (N-2) nested loops
    3. Two pointers for last two elements
    4. Skip duplicates at all levels
    """
    nums.sort()
    result = []
    
    # Base case: 2-Sum
    if n == 2:
        left, right = 0, len(nums) - 1
        while left < right:
            two_sum = nums[left] + nums[right]
            if two_sum == target:
                result.append([nums[left], nums[right]])
                # Skip duplicates
                while left < right and nums[left] == nums[left+1]:
                    left += 1
                while left < right and nums[right] == nums[right-1]:
                    right -= 1
                left += 1
                right -= 1
            elif two_sum < target:
                left += 1
            else:
                right -= 1
        return result
    
    # Recursive case: N-Sum reduces to (N-1)-Sum
    for i in range(len(nums) - n + 1):
        # Skip duplicates
        if i > 0 and nums[i] == nums[i-1]:
            continue
        
        # Recursively solve (N-1)-Sum
        sub_results = n_sum(nums[i+1:], target - nums[i], n - 1)
        
        for sub_result in sub_results:
            result.append([nums[i]] + sub_result)
    
    return result
"""
1. Loop Count Formula:

# Your brilliant observation!
N-Sum needs (N - 2) nested loops

2-Sum: 0 loops  # No loop, just two pointers!
3-Sum: 1 loop   # for i in range(n-2)
4-Sum: 2 loops  # for i, for j
5-Sum: 3 loops  # for i, for j, for k


2. Range Formula:

# Your pattern for loop ranges:

2-Sum: No loops
3-Sum: for i in range(n-2)      # n-2 for 3-sum
4-Sum: for i in range(n-3)      # n-3 for 4-sum
       for j in range(i+1, n-2)  # n-2 for inner
5-Sum: for i in range(n-4)      # n-4 for 5-sum
       for j in range(i+1, n-3)
       for k in range(j+1, n-2)

Pattern: Outermost loop uses range(n - (N-1))

3. Remaining Target:

# Your formula:

2-Sum: remaining_target = target
       # No subtraction needed!

3-Sum: remaining_target = target - nums[i]

4-Sum: remaining_target = target - nums[i] - nums[j]

5-Sum: remaining_target = target - nums[i] - nums[j] - nums[k]

Pattern: Subtract all fixed elements from target

4. Duplicate Skip Pattern:

# Your duplicate removal:

# Skip at loop level:
if i > 0 and nums[i] == nums[i-1]:
    continue

if j > i+1 and nums[j] == nums[j-1]:
    continue

# Skip at two-pointer level:
while left < right and nums[left] == nums[left+1]:
    left += 1
while left < right and nums[right] == nums[right-1]:
    right -= 1

Before Interview:

□ Remember: N-Sum = (N-2) loops + Two Pointers
□ Always sort first: nums.sort()
□ Skip duplicates at ALL levels
□ Use remaining_target for fixed elements
□ Two pointers always work on sorted portion
□ Time complexity: O(n^(N-1))
  - 2-Sum: O(n)
  - 3-Sum: O(n²)
  - 4-Sum: O(n³)

Your template works for 2-Sum through 5-Sum! ✅

## **Problems:**
```
1. ✅ Two Sum (LC 1)
   arr=[2,7,11,15], target=9 → [0,1]
   
2. ✅ Two Sum II - Sorted Array (LC 167)
   arr=[2,7,11,15], target=9 → [1,2]
   
3. ✅ 3Sum (LC 15)
   Find all triplets that sum to 0
   
4. ✅ 3Sum Closest (LC 16)
   Find triplet closest to target
   
5. ✅ 4Sum (LC 18)
   Find all quadruplets that sum to target

"""

# 3️⃣ SLIDING WINDOW (FIXED)

#Maximum Sum of Subarray Size K

def max_sum_k(arr, k):
    """Find maximum sum of subarray of size k"""
    left = 0
    temp = 0
    max_sum = 0

    for right in range(len(arr)):
        temp += arr[right]

        if right - left == k:
            temp -= arr[left]
            left += 1

        if right - left + 1 == k:
            max_sum = max(max_sum, temp)

    return max_sum

print(max_sum_k([2, 1, 5, 1, 3, 2], 3))  # 9

# Count Good Substrings (K Unique Characters)

def count_good_substrings(s, k):
    """Count substrings with exactly k unique characters"""
    left = 0
    n = len(s)
    freq_dict = {}
    ans = 0
    good_substrings = []
    
    for right in range(n):
        # Add right character
        if s[right] in freq_dict:
            freq_dict[s[right]] += 1
        else:
            freq_dict[s[right]] = 1
        
        # Window too big? Remove left
        if right - left == k:
            freq_dict[s[left]] -= 1
            if freq_dict[s[left]] == 0:
                freq_dict.pop(s[left])
            left += 1
        
        # Window exact size with k unique?
        if right - left + 1 == k and len(freq_dict) == k:
            ans += 1
            good_substrings.append(s[left:right+1])
    
    return ans, good_substrings

print(count_good_substrings("xyzzaz", 3))
# (1, ['yza'])


def fixed_sliding_window(arr, k):
    left = 0
    temp = 0
    result = 0
    
    for right in range(len(arr)):
        # Add right element
        temp += arr[right]
        
        # Window too big? Remove left
        if right - left == k:
            temp -= arr[left]
            left += 1
        
        # Window exact size? Update result
        if right - left + 1 == k:
            result = max(result, temp)
    
    return result
"""

---

## **Problems:**

### **Easy:**
```
1. ✅ Maximum Sum Subarray of Size K
   arr=[2,1,5,1,3,2], k=3 → 9
   
2. ✅ Average of Subarrays of Size K
   arr=[1,3,2,6,-1,4,1,8,2], k=5
   
3. ✅ Maximum Average Subarray (LC 643)
   Find max average of subarray size k
```

### **Medium:**
```
4. ✅ Count Good Substrings (K unique chars)
   s="xyzzaz", k=3 → 1
   
5. ✅ Maximum Vowels in Substring (LC 1456)
   s="abciiidef", k=3 → 3
   
6. ✅ Find All Anagrams (LC 438)
   s="cbaebabacd", p="abc"
   
7. ✅ Permutation in String (LC 567)
   Check if permutation exists in string
"""


# 4️⃣ SLIDING WINDOW (VARIABLE)

## **Problems:**

### **Medium:**
# ```
# 1. ✅ Longest Substring Without Repeating (LC 3) ⭐⭐⭐⭐⭐
#    s="abcabcbb" → 3
   
# 2. ✅ Smallest Subarray Sum ≥ S (LC 209)
#    arr=[2,3,1,2,4,3], s=7 → 2
   
# 3. ✅ Longest Subarray Sum ≤ K
#    arr=[1,2,3,4,5], k=10 → 4
   
# 4. ✅ Longest Repeating Character Replacement (LC 424)
#    s="AABABBA", k=1 → 4
   
# 5. ✅ Max Consecutive Ones III (LC 1004)
#    After flipping at most K zeros

# Longest Subarray Sum ≤ K

def variable_sliding_window(arr, k):
    """Find longest subarray with sum <= k"""
    left = 0
    n = len(arr)
    temp = 0
    ans = 0

    for right in range(n):
        temp += arr[right]

        # Shrink while sum > k
        while temp > k:
            temp -= arr[left]
            left += 1
        
        print(arr[left:right+1], temp)
        ans = max(ans, right - left + 1)
    
    return ans

print(variable_sliding_window([1, 2, 5, 4, 7], 10))
# Maximum length: 3

# Longest Substring Without Repeating

def longest_substring_no_repeat(s):
    """Find longest substring without repeating characters"""
    left = 0
    seen = set()
    max_length = 0

    for right in range(len(s)):
        # Shrink while duplicate exists
        while s[right] in seen:
            seen.remove(s[left])
            left += 1
        
        # Add current character
        seen.add(s[right])
        
        # Update max length
        max_length = max(max_length, right - left + 1)
    
    return max_length

print(longest_substring_no_repeat("abcabcbb"))  # 3
print(longest_substring_no_repeat("bbbbb"))     # 1
print(longest_substring_no_repeat("pwwkew"))    # 3

# Smallest Subarray Sum ≥ S

def smallest_subarray_sum(arr, S):
    """Find smallest subarray with sum >= S"""
    left = 0
    current_sum = 0
    min_length = float('inf')

    for right in range(len(arr)):
        # Add right element
        current_sum += arr[right]
        
        # Shrink while condition met
        while current_sum >= S:
            min_length = min(min_length, right - left + 1)
            current_sum -= arr[left]
            left += 1
    
    return min_length if min_length != float('inf') else 0

print(smallest_subarray_sum([2, 1, 5, 2, 3, 2], 7))  # 2
print(smallest_subarray_sum([2, 1, 5, 2, 8], 7))     # 1

# 4️⃣ PREFIX SUM

# Build Prefix Sum & Range Query

def build_prefix_sum(arr):
    """Build prefix sum array"""
    n = len(arr)
    prefix = [0] * n
    prefix[0] = arr[0]
    
    for i in range(1, n):
        prefix[i] = prefix[i-1] + arr[i]
    
    return prefix


def range_sum(prefix, left, right):
    """Get sum from left to right"""
    if left == 0:
        return prefix[right]
    else:
        return prefix[right] - prefix[left - 1]


# Test
arr = [3, 1, 4, 2, 5]
print(f"Array: {arr}")

prefix = build_prefix_sum(arr)
print(f"Prefix: {prefix}")

print(f"\nQueries:")
print(f"Sum[0:3] = {range_sum(prefix, 0, 3)}")  # 10
print(f"Sum[1:3] = {range_sum(prefix, 1, 3)}")  # 7
print(f"Sum[2:4] = {range_sum(prefix, 2, 4)}")  # 11

# Subarray Sum Equals K


def subarray_sum_k(arr, k):
    """Count subarrays with sum = k"""
    from collections import defaultdict
    
    prefix_sum = 0
    count = 0
    seen = defaultdict(int)
    seen[0] = 1  # Empty prefix
    
    for num in arr:
        prefix_sum += num
        
        # If (prefix_sum - k) exists, found subarray!
        if (prefix_sum - k) in seen:
            count += seen[prefix_sum - k]
        
        seen[prefix_sum] += 1
    
    return count

print(subarray_sum_k([1, 2, 3], 3))      # 2
print(subarray_sum_k([1, 1, 1], 2))      # 2
print(subarray_sum_k([1, -1, 1, 1], 2))  # 3

# Suffix Sum

def build_suffix_sum(arr):
    """Build suffix sum array (sum from i to end)"""
    n = len(arr)
    suffix = [0] * n
    
    # Last element stays same
    suffix[n-1] = arr[n-1]
    
    # Build from right to left
    for i in range(n-2, -1, -1):
        suffix[i] = suffix[i+1] + arr[i]
    
    return suffix

arr = [3, 1, 4, 2, 5]
suffix = build_suffix_sum(arr)
print(f"Array:  {arr}")
print(f"Suffix: {suffix}")
# Suffix: [15, 12, 11, 7, 5]

# 5️⃣ KADANE'S ALGORITHM

## **Problems:**

# ### **Easy:**
# ```
# 1. ✅ Maximum Sum Subarray (LC 53) ⭐⭐⭐⭐⭐
#    arr=[-2,1,-3,4,-1,2,1,-5,4] → 6
   
# 2. ✅ Best Time to Buy/Sell Stock (LC 121)
#    Find max profit
# ```

# ### **Medium:**
# ```
# 3. ✅ Maximum Product Subarray (LC 152)
#    Track max AND min
   
# 4. ✅ Maximum Circular Subarray (LC 918)
#    Array wraps around
   
# 5. ✅ Maximum Sum with At Most K Elements
#    Kadane's with constraint

# Maximum Sum Subarray

def kadanes(arr):
    """Find maximum sum of any subarray"""
    max_sum = float('-inf')
    current_sum = 0
    
    for num in arr:
        current_sum += num
        max_sum = max(max_sum, current_sum)
        
        if current_sum < 0:
            current_sum = 0
    
    return max_sum

print(kadanes([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6
print(kadanes([1, 2, 3, 4, 5]))                   # 15
print(kadanes([-1, -2, -3, -4]))                  # -1

# Kadane's with Indices

def kadanes_with_indices(arr):
    """Find max sum subarray and return subarray itself"""
    max_sum = float('-inf')
    current_sum = 0
    start = 0
    end = 0
    temp_start = 0
    
    for i in range(len(arr)):
        current_sum += arr[i]
        
        if current_sum > max_sum:
            max_sum = current_sum
            start = temp_start
            end = i
        
        if current_sum < 0:
            current_sum = 0
            temp_start = i + 1
    
    return arr[start:end+1], max_sum

arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
subarray, sum_val = kadanes_with_indices(arr)
print(f"Subarray: {subarray}, Sum: {sum_val}")
# Subarray: [4, -1, 2, 1], Sum: 6

# 6️⃣ BINARY SEARCH (BASIC)

## **Problems:**

# ### **Easy:**
# ```
# 1. ✅ Binary Search (LC 704)
#    Find element in sorted array
   
# 2. ✅ Search Insert Position (LC 35)
#    Find position to insert
   
# 3. ✅ First Bad Version (LC 278)
#    Find first bad version
   
# 4. ✅ Sqrt(x) (LC 69)
#    Find square root
   
# 5. ✅ Valid Perfect Square (LC 367)
#    Check if perfect square
# ```

# ### **Medium:**
# ```
# 6. ✅ Find First and Last Position (LC 34)
#    In sorted array with duplicates
   
# 7. ✅ Search in 2D Matrix (LC 74)
#    Binary search on matrix

# Binary Search in Sorted Array

def binary_search(arr, target):
    """Find target in sorted array"""
    left = 0
    right = len(arr) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

arr = [1, 3, 5, 7, 9, 11, 13]
print(binary_search(arr, 7))   # 3
print(binary_search(arr, 13))  # 6
print(binary_search(arr, 20))  # -1

# First and Last Occurrence

def first_occurrence(arr, target):
    """Find first occurrence of target"""
    left = 0
    right = len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            right = mid - 1  # Keep searching LEFT
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result


def last_occurrence(arr, target):
    """Find last occurrence of target"""
    left = 0
    right = len(arr) - 1
    result = -1
    
    while left <= right:
        mid = (left + right) // 2
        
        if arr[mid] == target:
            result = mid
            left = mid + 1  # Keep searching RIGHT
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return result

arr = [1, 2, 2, 2, 3, 4, 5]
print(first_occurrence(arr, 2))  # 1
print(last_occurrence(arr, 2))   # 3

# 7️⃣ BINARY SEARCH ON ANSWER

## **Problems:**

# ### **Medium:**
# ```
# 1. ✅ Koko Eating Bananas (LC 875) ⭐⭐⭐⭐⭐
#    Find minimum eating speed
   
# 2. ✅ Capacity to Ship Packages (LC 1011)
#    Find minimum ship capacity
   
# 3. ✅ Split Array Largest Sum (LC 410)
#    Minimize largest sum
   
# 4. ✅ Smallest Divisor (LC 1283)
#    Find smallest divisor
   
# 5. ✅ Minimum Speed to Arrive on Time (LC 1870)
#    Find minimum speed

# Koko Eating Bananas (Monkey & Coconuts)

import math

def min_eating_speed(piles, H):
    """Find minimum eating speed to finish in H hours"""
    
    def can_finish(speed):
        """Check if can finish at this speed"""
        hours = 0
        for pile in piles:
            hours += math.ceil(pile / speed)
        return hours <= H
    
    # Binary search on speed
    left = 1
    right = max(piles)
    
    while left <= right:
        mid = (left + right) // 2
        
        if can_finish(mid):
            right = mid - 1  # Try slower
        else:
            left = mid + 1   # Need faster
    
    return left

print(min_eating_speed([3, 6, 7, 11], 8))  # 4
print(min_eating_speed([30, 11, 23, 4, 20], 5))  # 30

# Capacity to Ship Packages

def ship_within_days(weights, days):
    """Find minimum ship capacity"""
    
    def can_ship(capacity):
        """Check if can ship with this capacity"""
        current_weight = 0
        days_needed = 1
        
        for weight in weights:
            if current_weight + weight > capacity:
                days_needed += 1
                current_weight = weight
            else:
                current_weight += weight
        
        return days_needed <= days
    
    # Binary search on capacity
    left = max(weights)
    right = sum(weights)
    
    while left <= right:
        mid = (left + right) // 2
        
        if can_ship(mid):
            right = mid - 1
        else:
            left = mid + 1
    
    return left

print(ship_within_days([1,2,3,4,5,6,7,8,9,10], 5))  # 15

# 8️⃣ ROTATED SORTED ARRAY

# ## **Problems:**

# ### **Medium:**
# ```
# 1. ✅ Search in Rotated Sorted Array (LC 33) ⭐⭐⭐⭐⭐
#    arr=[4,5,6,7,0,1,2], target=0
   
# 2. ✅ Find Minimum in Rotated Array (LC 153)
#    arr=[3,4,5,1,2] → 1
   
# 3. ✅ Search in Rotated Array II (LC 81)
#    With duplicates
   
# 4. ✅ Find Minimum in Rotated Array II (LC 154)
#    With duplicates

# Search in Rotated Sorted Array

def search_rotated(nums, target):
    """Find target in rotated sorted array"""
    left = 0
    right = len(nums) - 1
    
    while left <= right:
        mid = (left + right) // 2
        
        if nums[mid] == target:
            return mid
        
        # Check which half is sorted
        if nums[left] <= nums[mid]:
            # Left half sorted
            if nums[left] <= target < nums[mid]:
                right = mid - 1
            else:
                left = mid + 1
        else:
            # Right half sorted
            if nums[mid] < target <= nums[right]:
                left = mid + 1
            else:
                right = mid - 1
    
    return -1

arr = [4, 5, 6, 7, 0, 1, 2]
print(search_rotated(arr, 0))  # 4
print(search_rotated(arr, 3))  # -1

# Find Minimum in Rotated Array

def find_min(nums):
    """Find minimum element in rotated sorted array"""
    left = 0
    right = len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if nums[mid] > nums[right]:
            # Minimum in right half
            left = mid + 1
        else:
            # Minimum in left half (including mid)
            right = mid
    
    return nums[left]

print(find_min([3, 4, 5, 1, 2]))     # 1
print(find_min([4, 5, 6, 7, 0, 1, 2]))  # 0


# 🔟 PEAK ELEMENT

# Pattern:

def find_peak(arr):
    left, right = 0, len(arr) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if arr[mid] > arr[mid + 1]:
            # Peak on left (including mid)
            right = mid
        else:
            # Peak on right
            left = mid + 1
    
    return left

# ---

# ## **Problems:**
# ```
# 1. ✅ Find Peak Element (LC 162)
#    Find any peak in array
   
# 2. ✅ Peak Index in Mountain Array (LC 852)
#    Find peak in mountain
   
# 3. ✅ Find in Mountain Array (LC 1095)
#    Search in mountain array
# ```

# ---

# ---

# # 📊 **QUICK REFERENCE SUMMARY**

# ---
# ```
# ┌──────────────────────────────────────────────────────┐
# │ Pattern          │ Key Problems                      │
# ├──────────────────────────────────────────────────────┤
# │ Two Pointers     │ Reverse, Palindrome, Remove Dups │
# │ N-Sum            │ 2Sum, 3Sum, 4Sum                  │
# │ Sliding (Fixed)  │ Max Sum K, Anagrams               │
# │ Sliding (Var)    │ Longest Substr, Min Window        │
# │ Prefix Sum       │ Range Sum, Subarray Sum = K       │
# │ Kadane's         │ Max Subarray, Stock Profit        │
# │ Binary Basic     │ Search, Insert Position           │
# │ Binary Answer    │ Koko Bananas, Ship Packages       │
# │ Rotated Array    │ Search Rotated, Find Min          │
# │ Peak Element     │ Find Peak                         │
# └──────────────────────────────────────────────────────┘
# ```

# ---

# ---

# # 🏆 **TOP 20 MUST-KNOW PROBLEMS**

# ---
# ```
# ⭐⭐⭐⭐⭐ MUST DO (Interview Favorites):

# 1. Two Sum (LC 1)
# 2. 3Sum (LC 15)
# 3. Container With Most Water (LC 11)
# 4. Longest Substring Without Repeat (LC 3)
# 5. Subarray Sum Equals K (LC 560)
# 6. Maximum Subarray (Kadane's) (LC 53)
# 7. Product Except Self (LC 238)
# 8. Binary Search (LC 704)
# 9. Search in Rotated Array (LC 33)
# 10. Koko Eating Bananas (LC 875)

# ⭐⭐⭐⭐ Very Important:

# 11. Remove Duplicates (LC 26)
# 12. Find All Anagrams (LC 438)
# 13. Maximum Product Subarray (LC 152)
# 14. Find Min in Rotated Array (LC 153)
# 15. Smallest Subarray Sum (LC 209)
# 16. Valid Palindrome (LC 125)
# 17. Move Zeros (LC 283)
# 18. Search Insert Position (LC 35)
# 19. Find Peak Element (LC 162)
# 20. Split Array Largest Sum (LC 410)
# ```

# ---

# ---

# # 📝 **REVISION CHECKLIST**

# ---
# ```
# Week 1 Review:
# □ Two Pointers (3-4 problems)
# □ N-Sum (2-3 problems)
# □ Sliding Window Fixed (3-4 problems)

# Week 2 Review:
# □ Sliding Window Variable (3-4 problems)
# □ Prefix Sum (3-4 problems)
# □ Kadane's (2-3 problems)

# Week 3 Review:
# □ Binary Search Basic (3-4 problems)
# □ Binary Search on Answer (3-4 problems)
# □ Rotated Array (2-3 problems)

# Total: 30-35 problems for solid revision! ✅

