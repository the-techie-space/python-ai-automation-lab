# O(n) - Linear Growth
numbers = [1, 2, 3, 4, 5]  # 5 items

for num in numbers:
    print(num)
# Prints 5 times ✓


# O(n²) - Quadratic Growth  
numbers = [1, 2, 3, 4, 5]  # 5 items

for num1 in numbers:
    for num2 in numbers:
        print(num1, num2)
# Prints 25 times! 😱
```

**Graph visualization:**
```
Operations
    |
1M  |                            * O(n²)
    |                        *
100k|                    *
    |                *
10k |            *
    |        *
1k  |    *
    | *_______________* O(n)
    |_________________
    0   100   500  1000  (n)
```

---

## Big-O Complexity - Complete Picture

Now you understand the basics! Here's the full hierarchy (fastest to slowest):
```
O(1)      - Constant     - "Instant"
O(log n)  - Logarithmic  - "Very fast"
O(n)      - Linear       - "Fast" ✓ You know this!
O(n log n)- Linearithmic - "Pretty good"
O(n²)     - Quadratic    - "Slow" ✓ You know this!
O(n³)     - Cubic        - "Very slow"
O(2ⁿ)     - Exponential  - "Extremely slow"


# O(1) - Constant
def get_first(numbers):
    return numbers[0]  # Always 1 operation!

# O(log n) - Logarithmic (we'll learn this with Binary Search)
# Dividing problem in half each time

# O(n) - Linear
def find_max(numbers):
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num

# O(n²) - Quadratic
def bubble_sort(numbers):
    for i in range(len(numbers)):
        for j in range(len(numbers)):
            # comparison logic
            pass

