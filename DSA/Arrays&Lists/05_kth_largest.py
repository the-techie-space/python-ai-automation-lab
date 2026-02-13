"""
Arrays & Lists - Finding Kth Largest Element
============================================
Learn to find 2nd largest, 3rd largest, or any Kth largest element
"""

# ============================================================================
# PROBLEM: FIND SECOND LARGEST
# ============================================================================
"""
Challenge: Find the second largest number in ONE pass
Cannot sort (would be O(n log n))
Must do in O(n) time
"""

def find_second_largest(arr):
    """
    Find second largest element in array
    
    Args:
        arr: List of numbers
    
    Returns:
        int/None: Second largest element or None if not exists
    
    Time: O(n), Space: O(1)
    
    Logic:
        Track two variables: largest and second_largest
        For each number:
            - If bigger than largest → cascade values
            - Else if bigger than second_largest → update it
    """
    # Edge case
    if len(arr) < 2:
        return None
    
    # Initialize with first two numbers
    if arr[0] > arr[1]:
        largest = arr[0]
        second_largest = arr[1]
    else:
        largest = arr[1]
        second_largest = arr[0]
    
    # Process remaining elements
    for i in range(2, len(arr)):
        num = arr[i]
        
        if num > largest:
            # New largest found! Old largest becomes second
            second_largest = largest
            largest = num
        elif num > second_largest and num != largest:
            # Not largest, but bigger than current second
            second_largest = num
    
    return second_largest

# Test
print("--- Find Second Largest ---")
test_cases = [
    [3, 7, 2, 9, 1, 5],
    [10, 10, 10],
    [5, 5, 4, 4, 3],
    [100],
]

for arr in test_cases:
    result = find_second_largest(arr)
    print(f"Array: {arr}")
    print(f"Second largest: {result}\n")

# ============================================================================
# PROBLEM: FIND THIRD LARGEST
# ============================================================================
"""
Extension: Now track THREE variables
Same logic, more cascading
"""

def find_third_largest(arr):
    """
    Find third largest element in array
    
    Args:
        arr: List of numbers
    
    Returns:
        int/None: Third largest element or None if not exists
    
    Time: O(n), Space: O(1)
    
    Cascading Logic:
        New largest:  third ← second ← largest ← new
        New second:   third ← second ← new
        New third:    third ← new
    """
    # Edge case
    if len(arr) < 3:
        return None
    
    # Initialize with first three numbers (sorted)
    first_three = sorted([arr[0], arr[1], arr[2]], reverse=True)
    largest = first_three[0]
    second_largest = first_three[1]
    third_largest = first_three[2]
    
    # Process remaining elements
    for i in range(3, len(arr)):
        num = arr[i]
        
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
print("\n--- Find Third Largest ---")
test_arr = [3, 7, 2, 9, 1, 5, 8]
result = find_third_largest(test_arr)
print(f"Array: {test_arr}")
print(f"Third largest: {result}")
print(f"Expected: 5 (9, 8, 5 are top 3)")

# ============================================================================
# GENERIC SOLUTION: Kth LARGEST
# ============================================================================
"""
Problem: Can we find ANY Kth largest? (2nd, 3rd, 4th, 10th, etc.)
Solution: Track K largest elements in a list!
"""

def kth_largest(arr, k):
    """
    Find the Kth largest element
    k=1 means largest, k=2 means second largest, etc.
    
    Args:
        arr: List of numbers
        k: Position (1-indexed)
    
    Returns:
        int/None: Kth largest element or None if invalid
    
    Time: O(n*k), Space: O(k)
    
    Strategy:
        Maintain a sorted list of top K elements
        For each new number, check if it belongs in top K
        Use "bubble" to keep list sorted
    
    Example with k=3:
        arr = [3, 7, 2, 9, 1, 5, 8]
        
        Initially: top_k = [-∞, -∞, -∞]
        
        Process 3: [-∞, -∞, 3]
        Process 7: [-∞, 3, 7]
        Process 2: [2, 3, 7]
        Process 9: [3, 7, 9]
        Process 1: [3, 7, 9] (1 < 3, skip)
        Process 5: [5, 7, 9]
        Process 8: [7, 8, 9]
        
        3rd largest = 7 ✓
    """
    # Validation
    if k > len(arr) or k < 1:
        return None
    
    # Initialize with negative infinity
    top_k = [float('-inf')] * k
    
    for num in arr:
        # Check if this number belongs in top K
        if num > top_k[-1]:  # Larger than smallest in top_k
            # Insert it
            top_k[-1] = num
            
            # Bubble it to correct position (keep sorted descending)
            for i in range(k - 1, 0, -1):
                if top_k[i] > top_k[i - 1]:
                    top_k[i], top_k[i - 1] = top_k[i - 1], top_k[i]
                else:
                    break  # Already in correct position
    
    return top_k[-1]  # Return the kth largest (last in our top_k list)

# Test
print("\n" + "="*60)
print("GENERIC Kth LARGEST SOLUTION")
print("="*60)

test_arr = [3, 7, 2, 9, 1, 5, 8]
print(f"Array: {test_arr}\n")

for k in range(1, 6):
    result = kth_largest(test_arr, k)
    print(f"{k}th largest: {result}")

print(f"\nSorted for verification: {sorted(test_arr, reverse=True)}")

# ============================================================================
# ALTERNATIVE: Using Python's heapq (Production Code)
# ============================================================================
"""
For production code, use Python's built-in heap!
Much cleaner and optimized
"""

import heapq

def kth_largest_heap(arr, k):
    """
    Find Kth largest using min-heap
    
    Time: O(n log k), Space: O(k)
    
    Why this works:
        Min-heap of size k keeps the k largest elements
        The root (minimum) of this heap is the kth largest!
    """
    if k > len(arr) or k < 1:
        return None
    
    # Create min-heap of size k
    heap = []
    
    for num in arr:
        if len(heap) < k:
            heapq.heappush(heap, num)
        elif num > heap[0]:  # num is larger than smallest in heap
            heapq.heapreplace(heap, num)  # Replace and re-heapify
    
    return heap[0]  # Root is the kth largest

# Test
print("\n--- Using Python's heapq (Better!) ---")
test_arr = [3, 7, 2, 9, 1, 5, 8]
print(f"Array: {test_arr}\n")

for k in range(1, 6):
    result = kth_largest_heap(test_arr, k)
    print(f"{k}th largest: {result}")

# ============================================================================
# VISUALIZING THE DIFFERENCE
# ============================================================================

print("\n" + "="*60)
print("COMPARISON OF APPROACHES")
print("="*60)

comparison = """
1. MANUAL METHOD (Our Implementation)
   ├─ Pros: Learn the algorithm, no imports
   ├─ Cons: More code, O(n*k) time
   └─ Use: Educational purposes, interviews

2. HEAPQ METHOD (Python's Built-in)
   ├─ Pros: Clean, O(n log k) time, reliable
   ├─ Cons: Need to understand heaps
   └─ Use: Production code, real projects

3. SORT METHOD (Simplest)
   ├─ Code: sorted(arr, reverse=True)[k-1]
   ├─ Pros: One line, very simple
   ├─ Cons: O(n log n), wasteful for large arrays
   └─ Use: Small arrays, quick prototypes
"""

print(comparison)

# ============================================================================
# PRACTICE PROBLEMS
# ============================================================================

print("\n--- Related Problems to Practice ---")
problems = """
Easy:
✓ Find maximum element
✓ Find second maximum
✓ Find minimum and maximum

Medium:
✓ Kth largest element (this problem!)
✓ Kth smallest element
✓ Top K frequent elements
✓ Find median in stream

Hard:
✓ Sliding window maximum
✓ Merge K sorted arrays
"""
print(problems)

# ============================================================================
# KEY TAKEAWAYS
# ============================================================================
"""
FINDING Kth LARGEST:

APPROACH 1: Track K Variables
✓ Time: O(n), Space: O(1)
✓ Messy for large K
✓ Good for K=2,3

APPROACH 2: Track K Elements
✓ Time: O(n*k), Space: O(k)
✓ Scalable to any K
✓ Our generic solution

APPROACH 3: Min-Heap (Best!)
✓ Time: O(n log k), Space: O(k)
✓ Use heapq in Python
✓ Production-ready

APPROACH 4: Sort (Simple)
✓ Time: O(n log n), Space: O(1)
✓ Quick but inefficient
✓ Use for small data

WHEN TO USE EACH:
- K is small (2-3): Manual tracking
- K is medium (4-10): Our generic or heap
- K is large or dynamic: Heap only
- One-time operation: Just sort!
"""