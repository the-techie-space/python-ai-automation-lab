# Python list methods are used for adding, removing, searching, sorting, copying, and managing elements dynamically

# Adding Elements

# Used to add items to a list.

# append() → adds single element at end

# extend() → adds multiple elements

# insert() → adds element at specific index


lst = [1, 2, 3]

lst.append(4)        # [1, 2, 3, 4]
lst.extend([5, 6])   # [1, 2, 3, 4, 5, 6]
lst.insert(1, 10)    # [1, 10, 2, 3, 4, 5, 6]

# Removing Elements

# Used to remove items from a list.

# remove() → removes first occurrence

# pop() → removes by index (returns value)

# clear() → removes all elements

lst = [1, 2, 3, 2]

lst.remove(2)   # [1, 3, 2]
lst.pop(1)      # removes 3 → [1, 2]
lst.clear()     # []


# Searching & Counting

# Used to find elements.

# index() → returns index of element

# count() → number of occurrences

lst = [10, 20, 30, 20]

lst.index(20)   # 1
lst.count(20)   # 2

# Sorting & Reversing

# Used to reorder list elements.

# sort() → sorts list in-place

# sorted() → returns new sorted list

# reverse() → reverses list

lst = [3, 1, 4, 2]

lst.sort()              # [1, 2, 3, 4]
new_lst = sorted(lst)   # creates new list
lst.reverse()           # [4, 3, 2, 1]

# Copying Lists

# Used to copy list elements.

# copy() → shallow copy

# list() → copy constructor

# slicing [:]


lst = [1, 2, 3]

a = lst.copy()
b = list(lst)
c = lst[:]


# List Checking & Length

# Used to check elements and size.

# len() → length of list

# in / not in → membership

lst = [1, 2, 3]

len(lst)        # 3
2 in lst        # True

# selenium (saving images into list)
# elements = driver.find_elements(By.TAG_NAME, "img")
# src_list = []

# for ele in elements:
#     src_list.append(ele.get_attribute("src"))


# Reverse Array In-Place
# Find Max & Min
arr = [3, 5, 1, 9, 2]

min_num = max_num = arr[0]

for i in arr:
    if i > max_num:
        max_num = i
    if i < min_num:
        min_num = i

print(min_num, max_num)

# Reverse Array In-Place

# Two pointers

# No extra memory

arr = [1, 2, 3, 4, 5]

left, right = 0, len(arr) - 1

while left < right:
    arr[left], arr[right] = arr[right], arr[left]

    left += 1
    right -= 1

print(arr)

# Find Missing Number (1 to n)

# [1,2,4,5] → 3

# Sum formula

arr = [1, 2, 4, 5]

n = len(arr) + 1

res = n * (n+1) // 2

print(res-sum(arr))

# Move Zeros to End
# [0,1,0,3,12] → [1,3,12,0,0]

lst = [0,1,0,3,12]
pos = 0
for i in lst:
    if i != 0:
        lst[pos] = i
        pos += 1
    
for i in range(pos, len(lst)):
    lst[i] = 0

print(lst)


def find_second_largest(numbers):
    # Handle edge case - need at least 2 numbers
    if len(numbers) < 2:
        return None
    
    # Initialize both with first two numbers properly
    if numbers[0] > numbers[1]:
        largest = numbers[0]
        second_largest = numbers[1]
    else:
        largest = numbers[1]
        second_largest = numbers[0]
    
    # Start checking from index 2 onwards
    for i in range(2, len(numbers)):
        num = numbers[i]
        
        if num > largest:
            # New largest found!
            second_largest = largest  # Old largest becomes 2nd
            largest = num
        elif num > second_largest and num != largest:
            # Not largest, but bigger than current second_largest
            second_largest = num
    
    return second_largest

# Test
numbers = [3, 7, 2, 9, 1, 5]
result = find_second_largest(numbers)
print(f"Second largest: {result}")
# Output: Second largest: 7



def find_third_largest(numbers):
    # Handle edge case
    if len(numbers) < 3:
        return None
    
    # Step 1: Initialize with first three numbers
    # We need to sort them to know which is 1st, 2nd, 3rd
    first_three = sorted([numbers[0], numbers[1], numbers[2]], reverse=True)
    largest = first_three[0]
    second_largest = first_three[1]
    third_largest = first_three[2]
    
    # Step 2: Check remaining numbers
    for i in range(3, len(numbers)):
        num = numbers[i]
        
        if num > largest:
            # Cascade: largest → second → third
            third_largest = second_largest
            second_largest = largest
            largest = num
            
        elif num > second_largest and num != largest:
            # Cascade: second → third
            third_largest = second_largest
            second_largest = num
            
        elif num > third_largest and num != second_largest and num != largest:
            # Just update third
            third_largest = num
    
    return third_largest

# Test
numbers = [3, 7, 2, 9, 1, 5]
result = find_third_largest(numbers)
print(f"Third largest: {result}")
# Output: Third largest: 5 ✓

# Making It Generic - Finding Kth Largest
# Let's create a function that can find any position (2nd, 3rd, 4th, etc.)!
# Approach 1: Track K Elements (Efficient - O(n*k))

def kth_largest(numbers, k):
    """
    Find the kth largest number.
    k=1 means largest, k=2 means second largest, etc.
    """
    if k > len(numbers) or k < 1:
        return None
    
    # Track top k numbers in a list
    top_k = [float('-inf')] * k
    
    for num in numbers:
        # Check if this number belongs in top k
        if num > top_k[-1]:  # Larger than smallest in top_k
            # Insert in correct position
            top_k[-1] = num
            
            # Bubble it to correct position (keep sorted descending)
            for i in range(k-1, 0, -1):
                if top_k[i] > top_k[i-1]:
                    top_k[i], top_k[i-1] = top_k[i-1], top_k[i]
                else:
                    break
    
    return top_k[-1]  # Return the kth largest (last in our top_k list)


# Test it!
numbers = [3, 7, 2, 9, 1, 5, 8]

print(f"1st largest (max): {kth_largest(numbers, 1)}")  # 9
print(f"2nd largest: {kth_largest(numbers, 2)}")        # 8
print(f"3rd largest: {kth_largest(numbers, 3)}")        # 7
print(f"4th largest: {kth_largest(numbers, 4)}")        # 5
# ```

# **Output:**
# ```
# 1st largest (max): 9
# 2nd largest: 8
# 3rd largest: 7
# 4th largest: 5



def remove_duplicates(numbers):
    if len(numbers) < 0:
        return None
    
    slow = 0

    for fast in range(1, len(numbers)):
        if numbers[fast] != numbers[slow]:
            slow += 1
            numbers[slow] = numbers[fast]
    return slow + 1

# Test
nums = [1, 1, 2, 2, 2, 3, 4, 4, 5]
length = remove_duplicates(nums)
print(f"New length: {length}")
print(f"Array: {nums[:length]}")


def move_zeros(numbers):
    """
    Input: [0, 1, 0, 3, 12]
    Output: [1, 3, 12, 0, 0]
    
    Use two pointers!
    """
    if len(numbers) == 0:
        return 0
    
    pos = 0
    for i in range(len(numbers)):
        if numbers[i] != 0:
            numbers[pos] = numbers[i]
            pos += 1

    for i in range(pos, len(numbers)):
        numbers[i] = 0

# Test
nums = [0, 1, 0, 3, 12]
move_zeros(nums)
print(nums)  # Should be [1, 3, 12, 0, 0]


# Better Solution - Method 2 (Swap - One Pass!)

def move_zeros_swap(numbers):
    """
    One-pass approach using swap
    More elegant and efficient!
    """
    slow = 0  # Position for next non-zero
    
    for fast in range(len(numbers)):
        if numbers[fast] != 0:
            # Swap non-zero with position at slow
            numbers[slow], numbers[fast] = numbers[fast], numbers[slow]
            slow += 1

# Test
nums = [0, 1, 0, 3, 12]
move_zeros_swap(nums)
print(nums)  # [1, 3, 12, 0, 0] ✓



def has_pair_with_sum(numbers, target):
    """
    Two pointer approach - opposite direction
    """
    left = 0
    right = len(numbers) - 1
    
    while left < right:
        current_sum = numbers[left] + numbers[right]
        
        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1
        else:
            right -= 1
    
    return False

# Test
print(has_pair_with_sum([1, 2, 3, 4, 5], 9))   # True (4+5)
print(has_pair_with_sum([1, 2, 3, 4, 5], 10))  # False
print(has_pair_with_sum([1, 3, 5, 7, 9], 12))  # True (3+9)


def three_sum(numbers):
    """
    Input: [-1, 0, 1, 2, -1, -4]
    Output: [[-1, -1, 2], [-1, 0, 1]]
    
    Hint: Sort first, then use two pointers for each number!
    """
    # Your code here
    pass

# Test
nums = [-1, 0, 1, 2, -1, -4]
result = three_sum(nums)
print(result)
# Expected: [[-1, -1, 2], [-1, 0, 1]]



"""---------------------------------------------------------------------------------------------------"""



# Array or list = A collection of elements stored next to each other in memory, accessed using an index.
# An array is a group of values stored together.

# arr = [10, 20, 30, 40]

# print(arr)

# print(arr[0])   # first element
# print(arr[1])   # second element

# print(len(arr)) # length of an array

#Array has 4 elements

#Last index = len(arr) - 1

# print(len(arr) - 1)

# '''What is traversal?

# Visiting each element one by one.'''

# # eg: 
# arr = [10, 20, 30, 40]

# for i in range(len(arr)):
#     print(arr[i])

# """insert 5 at index 0 , 
# so will do right shifting the elements, then we can place 5 at start ( index 0)"""
# arr = [10, 20, 30, 40]

# arr.append(0) # here arr = [10, 20, 30, 40, 0] so at 38 line the range should, menas the shifting should start from index 3
# print(arr)

# size = len(arr)

# for i in range(size-1, 0, -1): # here list iteration will starts from len(arr) = 4-1 is 3, so range(3, 0, -1),  
#     arr[i] = arr[i-1] #and 0 means it should not go till 0 index because if i=0 then below arr[i] = arr[0-1] is not valid, and why -1 is iteraion has to starts from end of list, since we are shifting to right side

# arr[0] = 5 # adding 5 at index 0

# print(arr)

# arr = [0, 10, 0, 20, 30, 0, 40, 0]
# normal method
# print(arr)
# non_zero = []
# count = 0
# for i in range(len(arr)):
#     if arr[i] != 0:
#         non_zero.append(arr[i])
#     else:
#         count += 1
# print(count)
# sd = non_zero + count * [0]
# print(sd)
# by bubble sorting below method (moving zeros to end)
# size = len(arr)

# for i in range(size):
#     for j in range(0, size - i -1):
#         if arr[j] == 0 and arr[j+1] !=0:
#             arr[j], arr[j+1] = arr[j+1], arr[j]

# print(arr)



# insertion at given index

lst = [10,20,30]
pos = 0
size = len(lst)

# lst.append(0)

# for i in range(size, pos, -1):
#     lst[i] = lst[i-1]

# lst[pos] = 5

# print(lst)

# deletion at any position by given index

# lst = [10,20,30]
# pos = 0
# size = len(lst)

# pos = 0

# for i in range(pos, size-1):
#     lst[i] = lst[i+1]
# lst.pop()

# print(lst)

# search element in empty array
# arr = []

# if len(arr) >= 1:
#     print("will do program")
# else:
#     print("Arr is empty")

# find an duplicate element in arr
# arr = [10,20,30,10,40]
# frq_dict = {}

# for i in arr:
#     if i in frq_dict:
#         frq_dict[i] += 1
#     else:
#         frq_dict[i] = 1

# print(frq_dict)    

# write an armstrong number for user given input

user_input = int(input("Enter num: "))

def armstrong_num(user_input):
    nums = [int(i) for i in str(user_input)]
    cube_power = len(nums)
    sum_of_cube = sum(i ** cube_power for i in nums)
    return user_input == sum_of_cube
    
if armstrong_num(user_input):
    print("given number is an armstrong_num", user_input)
else:
    print("its not an armstrong_num")