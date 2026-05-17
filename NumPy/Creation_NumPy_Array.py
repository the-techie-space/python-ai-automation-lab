import numpy as np # type: ignore

# =============================================================================
# NumPy Array Creation & Manipulation
# =============================================================================
# This file covers the most common ways to create NumPy arrays.
# Each section introduces a new function with a clear explanation of:
#   - What it does
#   - Its syntax and parameters
#   - Examples across 1D, 2D, and 3D arrays


# -----------------------------------------------------------------------------
# 1D Array (Single Dimension)
# -----------------------------------------------------------------------------
# A 1D array is a flat sequence of elements — like a simple list.
# Visualize it as a single row: [1, 2, 3, 4, 5]

my_list_single = np.array([1, 2, 3, 4, 5])

print(my_list_single)   # Output: [1 2 3 4 5]


# -----------------------------------------------------------------------------
# 2D Array (Two Dimensions) — 3×3 Matrix
# -----------------------------------------------------------------------------
# A 2D array is like a table with rows and columns.
# Visualize it as a grid:
#   Row 0 → [1, 2, 3]
#   Row 1 → [4, 5, 6]
#   Row 2 → [7, 8, 9]

my_list_two_dim = np.array([[1, 2, 3],
                             [4, 5, 6],
                             [7, 8, 9]])

print(my_list_two_dim)
# Output:
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]


# -----------------------------------------------------------------------------
# 3D Array (Three Dimensions) — 3×3×3 Matrix
# -----------------------------------------------------------------------------
# A 3D array adds a "depth" dimension — like a stack of 2D tables/layers.
# Visualize it as multiple grids stacked on top of each other.
#
# Shape (3, 3, 3) means:
#   → 3 layers (depth)
#   → each layer has 3 rows
#   → each row has 3 columns

my_list_three_dim = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                               [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                               [[1, 2, 3], [4, 5, 6], [7, 8, 9]]])

print(my_list_three_dim)
# Output:
# [[[1 2 3]
#   [4 5 6]
#   [7 8 9]]
#
#  [[1 2 3]
#   [4 5 6]
#   [7 8 9]]
#
#  [[1 2 3]
#   [4 5 6]
#   [7 8 9]]]

print(my_list_three_dim.shape)  # Output: (3, 3, 3) → 3 layers, 3 rows, 3 cols


# -----------------------------------------------------------------------------
# np.zeros() — Create an Array Filled with Zeros
# -----------------------------------------------------------------------------
# Use this when you need a blank/placeholder array initialized to 0.
# Very common in machine learning to initialize weights or buffers.
#
# Syntax:
#   np.zeros(shape, dtype=float, order='C')
#
# Parameters:
#   shape  → int or tuple of ints — defines the size of each dimension
#   dtype  → data type of elements (default: float64 → shows as 0.)
#   order  → memory layout: 'C' = row-major (default), 'F' = column-major

# 1D — 3 zeros
zeroNp = np.zeros(3)
print(zeroNp)           # Output: [0. 0. 0.]
#                                       ↑ dot means float (float64 by default)

# 2D — 3×3 grid of zeros
zeroNp = np.zeros((3, 3))
print(zeroNp)
# Output:
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]

# 3D — 3×3×3 block of zeros
zeroNp = np.zeros((3, 3, 3))
print(zeroNp)
# Output:
# [[[0. 0. 0.]
#   [0. 0. 0.]
#   [0. 0. 0.]]
#  [[0. 0. 0.]
#   [0. 0. 0.]
#   [0. 0. 0.]]
#  [[0. 0. 0.]
#   [0. 0. 0.]
#   [0. 0. 0.]]]

# Using dtype=int → removes the decimal point, gives integer zeros
zeroNp = np.zeros(3, dtype=int)
print(zeroNp)           # Output: [0 0 0]
#                                       ↑ no dot → integer


# -----------------------------------------------------------------------------
# np.ones() — Create an Array Filled with Ones
# -----------------------------------------------------------------------------
# Identical to np.zeros() in syntax, but fills with 1 instead of 0.
# Useful for initializing arrays where 1 is the neutral/starting value.
#
# Syntax:
#   np.ones(shape, dtype=float, order='C')

# 1D — 3 ones
onesNp = np.ones(3)
print(onesNp)           # Output: [1. 1. 1.]

# 2D — 3×3 grid of ones
onesNp = np.ones((3, 3))
print(onesNp)
# Output:
# [[1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]]

# 3D — 3×3×3 block of ones
onesNp = np.ones((3, 3, 3))
print(onesNp)
# Output:
# [[[1. 1. 1.]
#   [1. 1. 1.]
#   [1. 1. 1.]]
#  [[1. 1. 1.]
#   [1. 1. 1.]
#   [1. 1. 1.]]
#  [[1. 1. 1.]
#   [1. 1. 1.]
#   [1. 1. 1.]]]

# dtype=int → integer ones (no decimal)
onesNp = np.ones(3, dtype=int)
print(onesNp)           # Output: [1 1 1]

# order='F' → Fortran (column-major) memory layout
# The OUTPUT looks the same, but internally data is stored column by column.
# This matters for performance in certain mathematical operations.
onesNp = np.ones((4, 3), dtype=int, order='F')
print(onesNp)
# Output:
# [[1 1 1]
#  [1 1 1]
#  [1 1 1]
#  [1 1 1]]


# -----------------------------------------------------------------------------
# np.arange() — Create an Array with a Range of Values
# -----------------------------------------------------------------------------
# Works just like Python's built-in range(), but returns a NumPy array.
# Great for generating sequences of numbers quickly.
#
# Syntax:
#   np.arange(start, stop, step)
#
# Parameters:
#   start → where to begin (default: 0, inclusive)
#   stop  → where to end (exclusive — this value is NOT included)
#   step  → increment between values (default: 1)

# Basic range: 0 to 9 (stop=10 is excluded)
arange = np.arange(10)
print(arange)           # Output: [0 1 2 3 4 5 6 7 8 9]

# Range with step: start=0, stop=10, step=2 → every 2nd number
stepRange = np.arange(0, 10, 2)
print(stepRange)        # Output: [0 2 4 6 8]
#                                   ↑ starts at 0, jumps by 2, stops before 10


# -----------------------------------------------------------------------------
# np.random.randint() — Create an Array of Random Integers
# -----------------------------------------------------------------------------
# Generates random integer values within a given range.
# Each call produces different values (truly random each time).
#
# Syntax:
#   np.random.randint(low, high=None, size=None, dtype=int)
#
# Parameters:
#   low   → minimum value (inclusive)
#   high  → maximum value (exclusive) — if omitted, range is [0, low)
#   size  → shape of the output array (int for 1D, tuple for 2D/3D)

# Single random integer between 0 and 9
randomInt = np.random.randint(10)
print(randomInt)        # Output: a single random number e.g. 7

# 1D Array — 5 random integers between 1 and 9
randomDim = np.random.randint(1, 10, 5)
print(randomDim)        # Output: e.g. [3 7 1 9 4]

# 2D Array — 5×5 grid of random integers between 1 and 9
randomDim = np.random.randint(1, 10, (5, 5))
#                              ↑   ↑   ↑
#                             low high  shape (5 rows, 5 cols)
print(randomDim)
# Output: e.g.
# [[4 7 2 9 1]
#  [3 6 8 5 2]
#  [7 1 4 3 9]
#  [2 8 6 1 7]
#  [5 3 9 4 6]]


# -----------------------------------------------------------------------------
# np.full() — Create an Array Filled with a Specific Value
# -----------------------------------------------------------------------------
# Unlike np.zeros() or np.ones(), np.full() lets YOU choose what value
# to fill the entire array with.
#
# Syntax:
#   np.full(shape, fill_value, dtype=None, order='C')
#
# Parameters:
#   shape      → int or tuple — size of each dimension
#   fill_value → the constant value to fill every element with
#   dtype      → data type (auto-detected from fill_value if not specified)

# 1D — single element filled with 5
fullNp = np.full(1, 5)
print(fullNp)           # Output: [5]

# 2D — 2×2 grid filled with 5
fullNp = np.full((2, 2), 5)
print(fullNp)
# Output:
# [[5 5]
#  [5 5]]

# 3D — 2×2×2 block filled with 5
fullNp = np.full((2, 2, 2), 5)
print(fullNp)
# Output:
# [[[5 5]
#   [5 5]]
#  [[5 5]
#   [5 5]]]



# -----------------------------------------------------------------------------
# np.linspace() — Create an Array of Evenly Spaced Values
# -----------------------------------------------------------------------------
# Unlike np.arange() which steps by a fixed INCREMENT, np.linspace() steps
# by whatever it takes to produce exactly N evenly-spaced values between
# a start and end point (both INCLUSIVE by default).
#
# Syntax:
#   np.linspace(start, stop, num=50, endpoint=True, retstep=False, dtype=None)
#
# Parameters:
#   start    → first value in the sequence (inclusive)
#   stop     → last value in the sequence (inclusive by default)
#   num      → how many values to generate (default: 50)
#   endpoint → if True (default), 'stop' IS included as the last element
#   retstep  → if True, also returns the step size used

# Generate 5 evenly-spaced numbers between 1 and 10
linearNp = np.linspace(1, 10, 5)
print(linearNp)
# Output: [ 1.    3.25  5.5   7.75 10.  ]
#           ↑                          ↑
#         start                       stop (both included)
#
# Step size = (10 - 1) / (5 - 1) = 9 / 4 = 2.25


# -----------------------------------------------------------------------------
# np.asarray() — Convert Input to a NumPy Array (No-Copy if Already an Array)
# -----------------------------------------------------------------------------
# Similar to np.array(), but smarter: if the input is already a NumPy array
# with a matching dtype, it returns a VIEW (not a new copy), saving memory.
#
# Syntax:
#   np.asarray(a, dtype=None, order=None)
#
# Parameters:
#   a     → input data: list, tuple, or existing NumPy array
#   dtype → desired data type (optional; inferred if not given)
#   order → memory layout: 'C' (row-major) or 'F' (column-major)
#
# KEY CONCEPT:
#   asarray() on a list      → always creates a new array
#   asarray() on an ndarray  → returns a VIEW (shared memory!)
#                              changes to the view WILL affect the original

# Example 1: Converting a plain Python list
my_list = [1, 2, 3, 4, 5]
array = np.asarray(my_list)
print(array)                # Output: [1 2 3 4 5]

# Example 2: asarray() on an existing NumPy array — VIEW behaviour
orgArr = np.array([1, 2, 3, 4, 5])
newArr = np.asarray(orgArr)    # newArr is a VIEW of orgArr
print(orgArr)               # Output: [1 2 3 4 5]
print(newArr)               # Output: [1 2 3 4 5]

newArr[0] = 10              # Modify the view…
print(newArr)               # Output: [10  2  3  4  5]
print(orgArr)               # Output: [10  2  3  4  5]  ← original CHANGED too!
#                                       ↑ shared memory — both point to same data


# -----------------------------------------------------------------------------
# np.copy() — Create a True Independent Copy of an Array
# -----------------------------------------------------------------------------
# Use np.copy() when you need to work on a duplicate and DO NOT want changes
# to affect the original array.
#
# Syntax:
#   np.copy(a, order='K')
#
# Parameters:
#   a     → the source array to copy
#   order → memory layout of the copy ('K' = keep original order)
#
# KEY CONCEPT:
#   copy() allocates brand-new memory — the original and copy are independent.
#   Changing one will NEVER affect the other.

orgArr = np.array([1, 2, 3, 4, 5])
newArr = np.copy(orgArr)       # newArr is a completely separate copy

print(orgArr)               # Output: [1 2 3 4 5]
print(newArr)               # Output: [1 2 3 4 5]

newArr[0] = 10              # Modify the copy…
print(newArr)               # Output: [10  2  3  4  5]
print(orgArr)               # Output: [ 1  2  3  4  5]  ← original UNCHANGED
#                                               ↑ independent memory — safe!

# ┌─────────────────────────────────────────────────────────┐
# │  asarray() vs copy() — Quick Comparison                 │
# │                                                         │
# │  np.asarray(arr)  → VIEW   — fast, shares memory        │
# │  np.copy(arr)     → COPY   — safe, independent memory   │
# └─────────────────────────────────────────────────────────┘


# -----------------------------------------------------------------------------
# np.eye() — Create a 2D Array with Ones on a Diagonal
# -----------------------------------------------------------------------------
# Returns a 2D array (matrix) where a specific diagonal is filled with 1s
# and all other positions are 0s.
# Unlike np.identity(), np.eye() allows RECTANGULAR matrices (rows ≠ cols).
#
# Syntax:
#   np.eye(N, M=None, k=0, dtype=float, order='C')
#
# Parameters:
#   N  → number of ROWS
#   M  → number of COLUMNS (default: same as N → square matrix)
#   k  → diagonal offset:
#          k = 0  → main diagonal (default)
#          k > 0  → shift diagonal above main (upper diagonal)
#          k < 0  → shift diagonal below main (lower diagonal)

# Default: 3×3 square, ones on the main diagonal (k=0)
eye = np.eye(3)
print(eye)
# Output:
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# k=1 → super-diagonal (one step ABOVE main diagonal)
eye = np.eye(3, k=1)
print(eye)
# Output:
# [[0. 1. 0.]
#  [0. 0. 1.]
#  [0. 0. 0.]]

# k=-1 → sub-diagonal (one step BELOW main diagonal)
eye = np.eye(3, k=-1)
print(eye)
# Output:
# [[0. 0. 0.]
#  [1. 0. 0.]
#  [0. 1. 0.]]

# Rectangular: 5 rows, 4 columns (non-square is only possible with np.eye)
eye = np.eye(5, 4)
print(eye)
# Output:
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]
#  [0. 0. 0. 0.]]


# -----------------------------------------------------------------------------
# np.identity() — Create a Square Identity Matrix
# -----------------------------------------------------------------------------
# Returns a SQUARE 2D array with 1s on the main diagonal and 0s elsewhere.
# An identity matrix (often written as I) is fundamental in linear algebra —
# multiplying any matrix by I leaves it unchanged (like multiplying by 1).
#
# Syntax:
#   np.identity(n, dtype=float)
#
# Parameters:
#   n     → size of the square matrix (n × n)
#   dtype → data type of elements (default: float64)
#
# NOTE: np.identity() only supports square matrices and k=0.
#       Use np.eye() if you need a rectangle or a shifted diagonal.

# 3×3 identity matrix
identity = np.identity(3)
print(identity)
# Output:
# [[1. 0. 0.]
#  [0. 1. 0.]
#  [0. 0. 1.]]

# ┌─────────────────────────────────────────────────────────────┐
# │  np.eye() vs np.identity() — Quick Comparison               │
# │                                                             │
# │  np.identity(n)      → always square (n×n), only k=0       │
# │  np.eye(N, M, k)     → can be rectangular, any diagonal k  │
# │                                                             │
# │  Use identity() for strict linear-algebra identity matrices │
# │  Use eye() for more flexible diagonal-matrix creation       │
# └─────────────────────────────────────────────────────────────┘


# -----------------------------------------------------------------------------
# np.diag() — Build a Diagonal Matrix OR Extract a Diagonal
# -----------------------------------------------------------------------------
# np.diag() is a two-way tool: its behaviour depends on the input:
#
#   Input is 1D array → builds a 2D matrix with those values on a diagonal
#   Input is 2D array → extracts diagonal values and returns a 1D array
#
# Syntax:
#   np.diag(v, k=0)
#
# Parameters:
#   v → 1D array (to build diagonal matrix) or 2D array (to extract diagonal)
#   k → diagonal offset (same rules as np.eye):
#         k = 0  → main diagonal
#         k > 0  → above main diagonal
#         k < 0  → below main diagonal

# --- Usage 1: 1D input → Create a diagonal matrix ---
diagArr = np.array([1, 2, 3, 4, 5])
diag = np.diag(diagArr)
print(diag)
# Output:
# [[1 0 0 0 0]
#  [0 2 0 0 0]
#  [0 0 3 0 0]
#  [0 0 0 4 0]
#  [0 0 0 0 5]]
#   ↑ values placed along the main diagonal

# --- Usage 2: 2D input → Extract the main diagonal ---
diagArr = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])
diag = np.diag(diagArr)
print(diag)
# Output: [1 5 9]
#          ↑ ↑ ↑  picks positions [0,0], [1,1], [2,2]

# --- Using k to shift the diagonal ---
diagArr = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

# k=1 → super-diagonal (above main)
diag = np.diag(diagArr, k=1)
print(diag)
# Output: [2 6]
#          ↑ ↑  picks positions [0,1] and [1,2]

# k=-1 → sub-diagonal (below main)
diag = np.diag(diagArr, k=-1)
print(diag)
# Output: [4 8]
#          ↑ ↑  picks positions [1,0] and [2,1]

# --- Combining with np.identity(): extract the diagonal of an identity matrix ---
diagArr = np.identity(4)
print(diagArr)
# Output:
# [[1. 0. 0. 0.]
#  [0. 1. 0. 0.]
#  [0. 0. 1. 0.]
#  [0. 0. 0. 1.]]

diag = np.diag(diagArr)
print(diag)
# Output: [1. 1. 1. 1.]
#          ↑ all main-diagonal values of the identity matrix


# -----------------------------------------------------------------------------
# np.random.choice() — Randomly Sample Elements from an Array
# -----------------------------------------------------------------------------
# Picks one or more elements at random from the given array.
# By default each pick is independent (with replacement).
#
# Syntax:
#   np.random.choice(a, size=None, replace=True, p=None)
#
# Parameters:
#   a       → source array (or int N → treated as np.arange(N))
#   size    → int → number of picks (1D output)
#             tuple → shape of output (e.g. (3, 3) → 2D output)
#             None (default) → returns a single scalar value
#   replace → if True (default), the same element can be picked more than once
#   p       → probability array (must sum to 1); if None, uniform probability

ranArr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])

# Single random pick (returns a scalar)
ran = np.random.choice(ranArr)
print(ran)
# Output: e.g. 3    (a single randomly chosen element)

# 1D sample — pick 3 random elements
ran = np.random.choice(ranArr, size=3)
print(ran)
# Output: e.g. [1 3 5]

# 2D sample — build a 3×3 grid of random picks
ran = np.random.choice(ranArr, size=(3, 3))
print(ran)
# Output: e.g.
# [[7 2 5]
#  [1 9 3]
#  [4 6 8]]
