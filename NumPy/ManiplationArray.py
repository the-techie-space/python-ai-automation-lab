import numpy as np  # type: ignore

# =============================================================================
# NumPy Array Manipulation
# =============================================================================
# This file covers the most common ways to manipulate the SHAPE and STRUCTURE
# of existing NumPy arrays, without changing the underlying data.
#
# Topics covered:
#   1. ndarray.reshape()     — Rearrange elements into a new shape
#   2. ndarray.flatten()     — Collapse any array into a 1D copy
#   3. ndarray.T / .transpose() — Swap rows and columns (or axes)
#   4. ndarray.swapaxes()    — Swap any two specific axes
#   5. np.concatenate()      — Join arrays along an existing axis
#   6. np.hstack() / vstack() — Shorthand for horizontal/vertical join
#   7. np.flip()             — Reverse elements along an axis
#   8. np.sum()              — Sum elements along an axis


# =============================================================================
# Starter Arrays used throughout this file
# =============================================================================
# We define 1D, 2D, and 3D arrays here once for reference in later sections.

# 1D array — flat sequence of 3 elements
arr = np.array([1, 2, 3])
print(arr)          # Output: [1 2 3]
print(arr.shape)    # Output: (3,)   → 1 dimension, 3 elements

# 2D array — 3 rows × 3 columns
arr2 = np.array([[1, 2, 3],
                 [4, 5, 6],
                 [7, 8, 9]])
print(arr2)         # Output: [[1 2 3] [4 5 6] [7 8 9]]
print(arr2.shape)   # Output: (3, 3)  → 3 rows, 3 columns

# 3D array — 3 layers × 3 rows × 3 columns
arr3 = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                 [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                 [[1, 2, 3], [4, 5, 6], [7, 8, 9]]])
print(arr3)         # Output: 3 stacked 3×3 grids
print(arr3.shape)   # Output: (3, 3, 3) → 3 layers, 3 rows, 3 cols


# -----------------------------------------------------------------------------
# 1. ndarray.reshape() — Change the Shape Without Changing Data
# -----------------------------------------------------------------------------
# reshape() rearranges the same elements into a different shape.
# The total number of elements MUST stay the same — you cannot add or remove
# elements by reshaping.
#
# Syntax:
#   array.reshape(new_shape)
#   array.reshape(rows, cols)          ← for 2D
#   array.reshape(layers, rows, cols)  ← for 3D
#
# KEY RULE:
#   product of new shape dims == total elements in original array
#   e.g. arr has 3 elements → can reshape to (1,3) or (3,1), both have 3 total
#
# KEY CONCEPT: reshape() returns a VIEW whenever possible (shares memory).
#   Changing the reshaped result may change the original — use .copy() if needed.

# --- Reshaping a 1D array (3 elements) ---

# (1, 3) → 1 row, 3 columns
reshape1D = arr.reshape(1, 3)
print(reshape1D)        # Output: [[1 2 3]]
print(reshape1D.shape)  # Output: (1, 3)
print(reshape1D.ndim)   # Output: 2  ← now a 2D array

# (3, 1) → 3 rows, 1 column
reshape1D = arr.reshape(3, 1)
print(reshape1D)
# Output:
# [[1]
#  [2]
#  [3]]
print(reshape1D.shape)  # Output: (3, 1)
print(reshape1D.ndim)   # Output: 2

# --- Reshaping a 2D array (9 elements: 3×3) ---

# (1, 9) → flatten into a single row
reshape2D = arr2.reshape(1, 9)
print(reshape2D)        # Output: [[1 2 3 4 5 6 7 8 9]]
print(reshape2D.shape)  # Output: (1, 9)
print(reshape2D.ndim)   # Output: 2

# (9, 1) → stretch into a single column
reshape2D = arr2.reshape(9, 1)
print(reshape2D)
# Output:
# [[1]
#  [2]
#  ...
#  [9]]
print(reshape2D.shape)  # Output: (9, 1)
print(reshape2D.ndim)   # Output: 2

# --- Reshaping a 3D array (27 elements: 3×3×3) ---

# Keep as 3D but with different distribution
reshape3D = arr3.reshape(3, 3, 3)   # same shape → no-op (27 elements)
print(reshape3D.shape)  # Output: (3, 3, 3)
print(reshape3D.ndim)   # Output: 3

# Reshape into (9, 3, 1) — still 27 elements (9 × 3 × 1 = 27)
reshape3D = arr3.reshape(9, 3, 1)
print(reshape3D.shape)  # Output: (9, 3, 1)
print(reshape3D.ndim)   # Output: 3


# -----------------------------------------------------------------------------
# 2. ndarray.flatten() — Collapse Any Array into a 1D Copy
# -----------------------------------------------------------------------------
# flatten() unravels ALL dimensions into a single flat 1D array.
# Unlike reshape(-1), flatten() ALWAYS returns a COPY — so modifying the
# result will NEVER affect the original array.
#
# Syntax:
#   array.flatten(order='C')
#
# Parameters:
#   order → reading order for elements:
#             'C' → row-major (left to right, top to bottom) — default
#             'F' → column-major (top to bottom, left to right)
#
# KEY CONCEPT:
#   flatten() vs reshape(-1)
#     flatten()    → always a copy  (safe to modify)
#     reshape(-1)  → a view if possible  (may affect original)

arr = np.array([[[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
                [[1, 2, 3], [4, 5, 6], [7, 8, 9]]])

print(arr.shape)    # Output: (3, 3, 3)   → 27 elements across 3 dimensions
print(arr.ndim)     # Output: 3

flat = arr.flatten()
print(flat)
# Output: [1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9 1 2 3 4 5 6 7 8 9]
#          ↑ all 27 elements laid out in a single row

print(flat.shape)   # Output: (27,)  → 1 dimension, 27 elements
print(flat.ndim)    # Output: 1


# -----------------------------------------------------------------------------
# 3. ndarray.T / .transpose() — Swap Rows and Columns (or Axes)
# -----------------------------------------------------------------------------
# Transposing flips a matrix so its rows become columns and its columns become
# rows. For higher-dimensional arrays, you can specify a custom axis order.
#
# Syntax:
#   array.T                          ← attribute, simple 2D transpose
#   array.transpose(axes)            ← method, lets you reorder axes freely
#   np.transpose(array, axes)        ← same, but as a standalone function
#
# Parameters (for .transpose()):
#   axes → tuple of ints — the desired NEW order of axes
#           e.g. (2, 1, 0) for a 3D array means:
#                old axis 2 → new axis 0
#                old axis 1 → new axis 1
#                old axis 0 → new axis 2
#
# KEY CONCEPT:
#   .T on a 1D array has NO effect — a 1D array has only one axis to swap.
#   Shape (m, n)  →  after .T  →  Shape (n, m)

# 1D: .T has no visible effect on a 1D array
arr = np.array([1, 2, 3])
transpose = arr.T
print(transpose)        # Output: [1 2 3]  ← unchanged
print(transpose.shape)  # Output: (3,)     ← still 1D

# 2D: classic row-column flip
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(arr)
# Output:
# [[1 2 3]
#  [4 5 6]]
print(arr.shape)    # Output: (2, 3)

transpose = arr.T
print(transpose)
# Output:
# [[1 4]
#  [2 5]
#  [3 6]]
#   ↑ rows became columns, columns became rows
print(transpose.shape)  # Output: (3, 2)   ← shape is also flipped
print(transpose.ndim)   # Output: 2

# 3D: custom axis reordering with .transpose(axes)
arr = np.array([[[1, 2, 3], [4, 5, 6]],
                [[1, 2, 3], [4, 5, 6]]])
#
# Original shape: (2, 2, 3)
#   axis 0 → depth  (2 layers)
#   axis 1 → rows   (2 rows per layer)
#   axis 2 → cols   (3 cols per row)
#
print(arr.shape)    # Output: (2, 2, 3)
print(arr.ndim)     # Output: 3

# .transpose(2, 1, 0) → swap axis 0 and axis 2
# New shape: (3, 2, 2) — old depth becomes new "cols", old cols become new "depth"
transpose = arr.transpose(2, 1, 0)
print(transpose)
# Output:
# [[[1 1]
#   [4 4]]
#  [[2 2]
#   [5 5]]
#  [[3 3]
#   [6 6]]]
print(transpose.shape)  # Output: (3, 2, 2)
print(transpose.ndim)   # Output: 3


# -----------------------------------------------------------------------------
# 4. ndarray.swapaxes() — Swap Any Two Specific Axes
# -----------------------------------------------------------------------------
# swapaxes() is a focused alternative to transpose(): instead of specifying
# the ENTIRE new axis order, you just tell it WHICH TWO axes to swap.
#
# Syntax:
#   array.swapaxes(axis1, axis2)
#
# Parameters:
#   axis1 → first axis to swap
#   axis2 → second axis to swap
#
# KEY CONCEPT:
#   For 2D arrays: swapaxes(0, 1) is identical to .T
#   For 3D arrays: only the two specified axes swap; the rest stay in place.

# 2D example — identical to .T
arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(arr.shape)    # Output: (2, 3)

swapaxis = arr.swapaxes(0, 1)
print(swapaxis)
# Output:
# [[1 4]
#  [2 5]
#  [3 6]]
print(swapaxis.shape)   # Output: (3, 2)  ← axes 0 and 1 swapped

# 3D example — swap axis 0 (depth=2) and axis 2 (cols=3)
multiSwap = np.array([[[1,  2,  3],  [4,  5,  6]],
                      [[7,  8,  9],  [10, 11, 12]]])
print(multiSwap.shape)  # Output: (2, 2, 3)
print(multiSwap.ndim)   # Output: 3

swaped = multiSwap.swapaxes(0, 2)
print(swaped)
# Output:
# [[[ 1  7]
#   [ 4 10]]
#  [[ 2  8]
#   [ 5 11]]
#  [[ 3  9]
#   [ 6 12]]]
print(swaped.shape)     # Output: (3, 2, 2)  ← axis 0 (size 2) ↔ axis 2 (size 3)
print(swaped.ndim)      # Output: 3

# ┌──────────────────────────────────────────────────────────────────┐
# │  .T vs .transpose() vs .swapaxes() — Quick Comparison            │
# │                                                                  │
# │  arr.T              → reverses ALL axes (full flip)              │
# │  arr.transpose(...) → custom full axis reorder — most flexible   │
# │  arr.swapaxes(a, b) → swap exactly two axes — most readable      │
# └──────────────────────────────────────────────────────────────────┘


# -----------------------------------------------------------------------------
# 5. np.concatenate() — Join Arrays Along an Existing Axis
# -----------------------------------------------------------------------------
# concatenate() glues two or more arrays together along a chosen axis.
# All arrays must have the SAME shape except along the concatenation axis.
#
# Syntax:
#   np.concatenate((a1, a2, ...), axis=0)
#
# Parameters:
#   (a1, a2, ...) → tuple of arrays to join — must be compatible shapes
#   axis          → the axis along which to join:
#                     axis=0 → stack VERTICALLY (add more rows)
#                     axis=1 → stack HORIZONTALLY (add more columns)
#
# KEY CONCEPT:
#   Think of axis=0 as "pile these arrays on top of each other" (↓)
#   Think of axis=1 as "place these arrays side by side" (→)

arr1 = np.array([[1, 2, 3],
                 [4, 5, 6]])

arr2 = np.array([[7,  8,  9],
                 [10, 11, 12]])

# axis=0 → stack vertically (add rows)
concat = np.concatenate((arr1, arr2), axis=0)
print(concat)
# Output:
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]
print(concat.shape)     # Output: (4, 3)  ← 2+2=4 rows, 3 cols unchanged
print(concat.ndim)      # Output: 2

# axis=1 → stack horizontally (add columns)
concat = np.concatenate((arr1, arr2), axis=1)
print(concat)
# Output:
# [[ 1  2  3  7  8  9]
#  [ 4  5  6 10 11 12]]
print(concat.shape)     # Output: (2, 6)  ← 2 rows unchanged, 3+3=6 cols
print(concat.ndim)      # Output: 2


# -----------------------------------------------------------------------------
# 6. np.hstack() / np.vstack() — Shorthand Stacking Functions
# -----------------------------------------------------------------------------
# These are convenience wrappers around concatenate() that make the intent
# immediately obvious from the function name.
#
# np.hstack((a, b))  → Horizontal Stack — joins columns (same as axis=1)
# np.vstack((a, b))  → Vertical Stack   — joins rows    (same as axis=0)
#
# Syntax:
#   np.hstack((a1, a2, ...))    ← no axis argument needed
#   np.vstack((a1, a2, ...))    ← no axis argument needed
#
# KEY CONCEPT:
#   hstack = "place arrays side by side"   →→
#   vstack = "pile arrays on top of each"  ↓↓

# hstack → columns grow (side by side)
hArray = np.hstack((arr1, arr2))
print(hArray)
# Output:
# [[ 1  2  3  7  8  9]
#  [ 4  5  6 10 11 12]]
print(hArray.shape)     # Output: (2, 6)
print(hArray.ndim)      # Output: 2

# vstack → rows grow (on top of each other)
vArray = np.vstack((arr1, arr2))
print(vArray)
# Output:
# [[ 1  2  3]
#  [ 4  5  6]
#  [ 7  8  9]
#  [10 11 12]]
print(vArray.shape)     # Output: (4, 3)
print(vArray.ndim)      # Output: 2

# ┌─────────────────────────────────────────────────────────────────────┐
# │  concatenate vs hstack vs vstack — Quick Comparison                 │
# │                                                                     │
# │  np.concatenate((a,b), axis=0) == np.vstack((a, b))  ← same result │
# │  np.concatenate((a,b), axis=1) == np.hstack((a, b))  ← same result │
# │                                                                     │
# │  Use hstack/vstack for clarity; use concatenate when axis varies.   │
# └─────────────────────────────────────────────────────────────────────┘


# -----------------------------------------------------------------------------
# 7. np.flip() — Reverse Elements Along an Axis
# -----------------------------------------------------------------------------
# flip() reverses the order of elements along one or more specified axes.
# It does NOT sort — it simply mirrors the array.
#
# Syntax:
#   np.flip(m, axis=None)
#
# Parameters:
#   m    → the array to flip
#   axis → which axis to flip along:
#            None    → flips ALL axes (full reversal in every direction)
#            axis=0  → reverse the row ORDER (first row ↔ last row)
#            axis=1  → reverse each row's element ORDER (left ↔ right)
#
# KEY CONCEPT:
#   Think of axis=0 as flipping a pancake (↕ upside down)
#   Think of axis=1 as reading each row backwards (↔ left-right mirror)

arr = np.array([[1, 2, 3],
                [4, 5, 6]])
print(arr)
# Output:
# [[1 2 3]
#  [4 5 6]]

# axis=None → flip everything (all dimensions)
flip = np.flip(arr)
print(flip)
# Output:
# [[6 5 4]
#  [3 2 1]]
#   ↑ both rows are reversed AND row order is reversed

# axis=0 → only reverse the row ORDER (flip upside down)
flip = np.flip(arr, axis=0)
print(flip)
# Output:
# [[4 5 6]   ← was row 1, now row 0
#  [1 2 3]]  ← was row 0, now row 1

# axis=1 → only reverse each row's element order (flip left-right)
flip = np.flip(arr, axis=1)
print(flip)
# Output:
# [[3 2 1]   ← row 0 reversed
#  [6 5 4]]  ← row 1 reversed


# -----------------------------------------------------------------------------
# 8. np.sum() — Sum Elements Along an Axis
# -----------------------------------------------------------------------------
# np.sum() adds up elements along a chosen axis, collapsing that axis in the
# output. Choosing the axis carefully controls WHAT gets summed.
#
# Syntax:
#   np.sum(a, axis=None, dtype=None, keepdims=False)
#
# Parameters:
#   a        → input array
#   axis     → which axis to sum along:
#                None       → sum ALL elements → returns a scalar
#                axis=0     → collapse ROWS    → sum down each column
#                axis=1     → collapse COLUMNS → sum across each row
#                axis=(0,1) → collapse both axes at once → grand total scalar
#   dtype    → output data type (default: inferred from input)
#   keepdims → if True, output keeps the same number of dimensions as input
#
# KEY CONCEPT — "axis collapses":
#   Imagine squeezing the array along the chosen axis like an accordion.
#   axis=0  → squeeze all rows into one → output shape loses the first dim
#   axis=1  → squeeze all cols into one → output shape loses the second dim

arr = np.full((10, 3), 5)   # 10×3 array, every element = 5
print(arr)
# Output: 10 rows of [5 5 5]
print(arr.shape)    # Output: (10, 3)
print(arr.ndim)     # Output: 2

# axis=0 → sum each COLUMN across all 10 rows → one value per column
total = np.sum(arr, axis=0)
print(total)        # Output: [50 50 50]   ← 10 rows × 5 = 50, for each of 3 cols
print(total.shape)  # Output: (3,)         ← row dimension collapsed
print(total.ndim)   # Output: 1

# axis=1 → sum each ROW across all 3 columns → one value per row
total = np.sum(arr, axis=1)
print(total)        # Output: [15 15 15 15 15 15 15 15 15 15] ← 3 cols × 5 = 15
print(total.shape)  # Output: (10,)        ← column dimension collapsed
print(total.ndim)   # Output: 1

# axis=(0,1) → sum EVERYTHING → grand total scalar
total = np.sum(arr, axis=(0, 1))
print(total)        # Output: 150          ← 10 × 3 × 5 = 150
print(total.shape)  # Output: ()           ← no dimensions left (scalar)
print(total.ndim)   # Output: 0
