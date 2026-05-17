import numpy as np # type: ignore

# =============================================================================
# NumPy Array Accessing & Slicing
# =============================================================================
# This file covers how to access and slice NumPy arrays.
# Each section introduces a concept with a clear explanation of:
#   - What it does
#   - How indexing works (with visual diagrams)
#   - Examples across 1D, 2D, and 3D arrays


# -----------------------------------------------------------------------------
# 1D Array — Accessing Elements by Index
# -----------------------------------------------------------------------------
# A 1D array is a flat sequence of elements — like a simple list.
# Indexing starts at 0.
#
# Visualize it as:
#   Index →  [0]  [1]  [2]  [3]  [4]
#   Value →   1    2    3    4    5

array = np.array([1, 2, 3, 4, 5])

print(array)       # [1 2 3 4 5]
print(array[0])    # 1
print(array[1])    # 2
print(array[2])    # 3
print(array[3])    # 4
print(array[4])    # 5


# -----------------------------------------------------------------------------
# 2D Array — Accessing Elements by [row][column]
# -----------------------------------------------------------------------------
# A 2D array is like a table with rows and columns.
# Use array[row][col] or array[row, col] to access a specific element.
#
# Visualize it as:
#         Col→  [0]  [1]  [2]
#   Row [0] →    1    2    3
#   Row [1] →    4    5    6
#   Row [2] →    7    8    9

array = np.array([[1, 2, 3],
                  [4, 5, 6],
                  [7, 8, 9]])

print(array)       # [[1 2 3]
                   #  [4 5 6]
                   #  [7 8 9]]

# --- Access entire rows ---
print(array[0])    # [1 2 3]  → Row 0
print(array[1])    # [4 5 6]  → Row 1
print(array[2])    # [7 8 9]  → Row 2

# --- Access individual elements [row][col] ---
print(array[0][0]) # 1
print(array[0][1]) # 2
print(array[0][2]) # 3
print(array[1][0]) # 4
print(array[1][1]) # 5
print(array[1][2]) # 6
print(array[2][0]) # 7
print(array[2][1]) # 8
print(array[2][2]) # 9


# -----------------------------------------------------------------------------
# 3D Array — Accessing Elements by [depth][row][column]
# -----------------------------------------------------------------------------
# A 3D array adds a "depth" dimension — like a stack of 2D tables/layers.
# Use array[depth][row][col] to access a specific element.
#
# Shape (3, 3, 3) means:
#   → 3 layers (depth)   → accessed by first index
#   → 3 rows per layer   → accessed by second index
#   → 3 cols per row     → accessed by third index
#
# Visualize it as 3 stacked grids:
#   Layer [0]:          Layer [1]:          Layer [2]:
#    1   2   3          10  11  12          19  20  21
#    4   5   6          13  14  15          22  23  24
#    7   8   9          16  17  18          25  26  27

array = np.array([[[1,  2,  3],  [4,  5,  6],  [7,  8,  9]],
                  [[10, 11, 12], [13, 14, 15], [16, 17, 18]],
                  [[19, 20, 21], [22, 23, 24], [25, 26, 27]]])

print(array)
# [[[ 1  2  3]
#   [ 4  5  6]
#   [ 7  8  9]]
#
#  [[10 11 12]
#   [13 14 15]
#   [16 17 18]]
#
#  [[19 20 21]
#   [22 23 24]
#   [25 26 27]]]

# --- Access entire layers (depth index) ---
print(array[0])    # [[ 1  2  3] [ 4  5  6] [ 7  8  9]]   → Layer 0
print(array[1])    # [[10 11 12] [13 14 15] [16 17 18]]   → Layer 1
print(array[2])    # [[19 20 21] [22 23 24] [25 26 27]]   → Layer 2

# --- Access rows within a layer [depth][row] ---
print(array[0][0]) # [1 2 3]    → Layer 0, Row 0
print(array[0][1]) # [4 5 6]    → Layer 0, Row 1
print(array[0][2]) # [7 8 9]    → Layer 0, Row 2
print(array[1][0]) # [10 11 12] → Layer 1, Row 0
print(array[1][1]) # [13 14 15] → Layer 1, Row 1
print(array[1][2]) # [16 17 18] → Layer 1, Row 2
print(array[2][0]) # [19 20 21] → Layer 2, Row 0
print(array[2][1]) # [22 23 24] → Layer 2, Row 1
print(array[2][2]) # [25 26 27] → Layer 2, Row 2

# --- Access individual elements [depth][row][col] ---
print(array[0][0][0]) # 1
print(array[0][0][1]) # 2
print(array[0][0][2]) # 3
print(array[0][1][0]) # 4
print(array[0][1][1]) # 5
print(array[0][1][2]) # 6
print(array[0][2][0]) # 7
print(array[0][2][1]) # 8
print(array[0][2][2]) # 9

print(array[1][0][0]) # 10
print(array[1][0][1]) # 11
print(array[1][0][2]) # 12
print(array[1][1][0]) # 13
print(array[1][1][1]) # 14
print(array[1][1][2]) # 15
print(array[1][2][0]) # 16
print(array[1][2][1]) # 17
print(array[1][2][2]) # 18

print(array[2][0][0]) # 19
print(array[2][0][1]) # 20
print(array[2][0][2]) # 21
print(array[2][1][0]) # 22
print(array[2][1][1]) # 23
print(array[2][1][2]) # 24
print(array[2][2][0]) # 25
print(array[2][2][1]) # 26
print(array[2][2][2]) # 27


# =============================================================================
# PRACTICAL EXAMPLES — Array Manipulation using ones() & zeros()
# =============================================================================


# -----------------------------------------------------------------------------
# Example 1: Border Matrix (3×3) — ones with zero in center
# -----------------------------------------------------------------------------
# Goal: Create this pattern using np.ones() and then modify the center:
#   [1, 1, 1]
#   [1, 0, 1]
#   [1, 1, 1]
#
# Step 1: Create a 3×3 matrix of all ones
# Step 2: Set the center element [1,1] to 0

onesNp = np.ones((3, 3))
print(onesNp)
# [[1. 1. 1.]
#  [1. 1. 1.]
#  [1. 1. 1.]]

onesNp[1, 1] = 0   # Set center element to 0

print(onesNp)
# [[1. 1. 1.]
#  [1. 0. 1.]
#  [1. 1. 1.]]


# -----------------------------------------------------------------------------
# Example 2: Border Matrix (5×5) — ones border, zeros inside, 9 in center
# -----------------------------------------------------------------------------
# Goal: Create this pattern using slicing to embed a zeros block:
#   [1, 1, 1, 1, 1]
#   [1, 0, 0, 0, 1]
#   [1, 0, 9, 0, 1]
#   [1, 0, 0, 0, 1]
#   [1, 1, 1, 1, 1]
#
# Step 1: Create a 5×5 matrix of all ones
# Step 2: Create a 3×3 matrix of all zeros, set center to 9
# Step 3: Embed the zeros matrix into the inner 3×3 region of the ones matrix
#         using advanced slicing: onesNp[1:4, 1:4]

onesNp = np.ones((5, 5))
print(onesNp)
# [[1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]
#  [1. 1. 1. 1. 1.]]

zerosNp = np.zeros((3, 3))
print(zerosNp)
# [[0. 0. 0.]
#  [0. 0. 0.]
#  [0. 0. 0.]]

zerosNp[1, 1] = 9   # Set center of zeros matrix to 9
print(zerosNp)
# [[0. 0. 0.]
#  [0. 9. 0.]
#  [0. 0. 0.]]

# Embed zerosNp into the inner 3×3 region of onesNp using slicing
# onesNp[1:4, 1:4] selects rows 1,2,3 and cols 1,2,3
onesNp[1:4, 1:4] = zerosNp
print(onesNp)
# [[1. 1. 1. 1. 1.]
#  [1. 0. 0. 0. 1.]
#  [1. 0. 9. 0. 1.]
#  [1. 0. 0. 0. 1.]
#  [1. 1. 1. 1. 1.]]


# =============================================================================
# ARRAY SLICING — Extracting Sub-sections
# =============================================================================
# Slicing lets you extract a portion of an array without copying elements one
# by one. It is one of the most powerful features of NumPy.
#
# Syntax:  array[start:stop:step]
#
#   start → index of first element to include (default: 0)
#   stop  → index to stop at (EXCLUSIVE — this element is NOT included)
#   step  → how many elements to skip (default: 1)
#
# For 2D/3D: array[rows_slice, cols_slice] or array[depth, rows, cols]


# -----------------------------------------------------------------------------
# 2D Array Slicing — Extracting a Sub-matrix
# -----------------------------------------------------------------------------
# Array properties:
#   .ndim  → number of dimensions
#   .size  → total number of elements
#   .shape → tuple showing (rows, cols) or (depth, rows, cols)

twoDim = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])
print(twoDim)
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

print(twoDim.ndim)  # 2  → 2 dimensions (rows and columns)
print(twoDim.size)  # 9  → 3 rows × 3 cols = 9 total elements

# --- Example: Extract bottom-right 2×2 sub-matrix ---
# Goal: Get [[5, 6], [8, 9]]
#
# Visual breakdown:
#   Rows:    1:3 → index 1 and 2 (row 1 = [4,5,6], row 2 = [7,8,9])
#   Columns: 1:3 → index 1 and 2 (col 1 and col 2)
#
#         Col→  [0]  [1]  [2]
#   Row [0] →    1    2    3
#   Row [1] →    4   [5]  [6]   ← selected
#   Row [2] →    7   [8]  [9]   ← selected

print(twoDim[1:3, 1:3])
# [[5 6]
#  [8 9]]


# -----------------------------------------------------------------------------
# 2D Array Slicing — Larger Array with Negative Indexing
# -----------------------------------------------------------------------------
# Negative indices count from the END of the array:
#   -1 → last element
#   -2 → second to last element
#
# Array:
#   [[ 1  2  3  4  5]
#    [ 6  7  8  9 10]
#    [11 12 13 14 15]
#    [16 17 18 19 20]
#    [21 22 23 24 25]]
#
# Goal: Extract [[12, 13], [17, 18]]
#
# Steps:
#   1. Check shape → (5, 5), ndim → 2
#   2. Target rows: index 2 and 3  → use 2:-1  (row 2 up to but not last)
#   3. Target cols: index 1 and 2  → use 1:-2  (col 1 up to but not last 2)

sliceArray = np.arange(1, 26).reshape(5, 5)
print(sliceArray)
# [[ 1  2  3  4  5]
#  [ 6  7  8  9 10]
#  [11 12 13 14 15]
#  [16 17 18 19 20]
#  [21 22 23 24 25]]

print(sliceArray.ndim)   # 2
print(sliceArray.size)   # 25
print(sliceArray.shape)  # (5, 5)

print(sliceArray[2:-1, 1:-2])
# [[12 13]
#  [17 18]]
#
# Breakdown:
#   Rows  2:-1 → from row index 2 up to (not including) last row → rows 2 & 3
#   Cols  1:-2 → from col index 1 up to (not including) last 2 cols → cols 1 & 2


# -----------------------------------------------------------------------------
# 3D Array — Creation with Incrementing Numbers
# -----------------------------------------------------------------------------
# To create a 3D array with incrementing numbers, use np.arange() + .reshape()
#
# Formula:  total elements = depth × rows × cols
# For shape (3, 3, 3) → 3 × 3 × 3 = 27 elements
#
# np.arange(start, stop) → stop is EXCLUSIVE
# To get numbers 1 to 27 → use arange(1, 28)

threeDim = np.arange(1, 28).reshape(3, 3, 3)
print(threeDim)
# [[[ 1  2  3]
#   [ 4  5  6]
#   [ 7  8  9]]
#
#  [[10 11 12]
#   [13 14 15]
#   [16 17 18]]
#
#  [[19 20 21]
#   [22 23 24]
#   [25 26 27]]]

print(threeDim.ndim)   # 3
print(threeDim.size)   # 27
print(threeDim.shape)  # (3, 3, 3)


# -----------------------------------------------------------------------------
# 3D Array Slicing — Selecting Specific Columns Across All Layers
# -----------------------------------------------------------------------------
# Syntax for 3D slicing:  array[depth_slice, row_slice, col_slice]
#
#   :   → select ALL (no restriction)
#   0:3:2 → from index 0 to 3, step 2 → selects indices 0 and 2 (odd positions)
#
# Goal: Extract columns at index 0 and 2 (every other column) from all layers
#
# Breakdown of threeDim[:, :, 0:3:2]:
#   depth  → :      = all 3 layers
#   rows   → :      = all 3 rows
#   cols   → 0:3:2  = col 0 and col 2 (step 2 skips col 1)

print(threeDim[:, :, 0:3:2])
# [[[ 1  3]
#   [ 4  6]
#   [ 7  9]]
#
#  [[10 12]
#   [13 15]
#   [16 18]]
#
#  [[19 21]
#   [22 24]
#   [25 27]]]
