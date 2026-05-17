# =============================================================================
# Working on NumPy (Numerical Python)
# =============================================================================

# -----------------------------------------------------------------------------
# What is NumPy?
# -----------------------------------------------------------------------------
# NumPy (Numerical Python) is a powerful open-source library for Python.
# It provides support for:
#   - Large, multi-dimensional arrays and matrices
#   - A vast collection of high-level mathematical functions to operate on them
#
# It is the foundation of almost all scientific computing in Python.
# Libraries like Pandas, TensorFlow, and OpenCV are all built on top of NumPy.

# -----------------------------------------------------------------------------
# Installation
# -----------------------------------------------------------------------------
# NumPy is NOT part of Python's standard library, so you need to install it.
# Use pip (Python's package manager) to install it:
#
#   pip install numpy
#
# Once installed, you can import it in your Python script.

# -----------------------------------------------------------------------------
# Importing NumPy
# -----------------------------------------------------------------------------
# By convention, NumPy is always imported with the alias 'np'.
# This is a universal standard across the Python community.

import numpy as np  # type: ignore

# -----------------------------------------------------------------------------
# Why NumPy is Faster than a Python List?
# -----------------------------------------------------------------------------
# At first glance, a NumPy array and a Python list look similar.
# But under the hood, they are very different in how they store and process data.
#
# +----------------+--------------------------------------------------------------+--------------------------------------------------------------+
# | Aspect         | NumPy Array                                                  | Python List                                                  |
# +----------------+--------------------------------------------------------------+--------------------------------------------------------------+
# | Memory Storage | Contiguous block of memory → better cache efficiency         | Pointers to scattered objects → more fragmentation           |
# | Data Types     | Homogeneous (same type) → efficient memory use               | Heterogeneous (mixed types) → higher memory overhead         |
# | Operations     | Vector ops with SIMD (parallel processing)                   | Loop-based ops → slower due to Python's interpreted nature   |
# | Efficiency     | Written in C and optimized → faster numerical execution      | Executed as Python byte-code → generally slower              |
# | Memory Usage   | Less memory (fixed types + contiguous storage)               | More memory (each element is a separate Python object)       |
# | Broadcasting   | Supports broadcasting on arrays of different shapes          | No broadcasting → element-wise ops are less efficient        |
# | Performance    | Better cache utilization → faster access and processing      | Poor cache utilization due to scattered memory allocation    |
# | Functionality  | Rich set of optimized math functions for array operations    | Limited to basic ops, lacks advanced math capabilities       |
# +----------------+--------------------------------------------------------------+--------------------------------------------------------------+


# =============================================================================
# Creating NumPy Arrays
# =============================================================================
# Use np.array() to create a NumPy array from a Python list or tuple.

# -----------------------------------------------------------------------------
# 1D Array (Single Dimension)
# -----------------------------------------------------------------------------
# A 1D array is a flat list of elements — like a single row of values.
# Think of it as a simple number line: [1, 2, 3, 4, 5]

singleDimension = np.array([1, 2, 3, 4, 5])
print(singleDimension)          # Output: [1 2 3 4 5]

# .ndim → Number of Dimensions
# -----------------------------------------------------------------------
# ndim tells you HOW MANY dimensions (axes) the array has.
# A 1D array has 1 axis (just a flat list), so ndim = 1.
# Think of it as: how many levels of brackets [ ] are there?
#   [1, 2, 3]       → 1 level → ndim = 1
#   [[1, 2], [3,4]] → 2 levels → ndim = 2

print(singleDimension.ndim)     # Output: 1

# .shape → Dimensions Breakdown (rows × columns × depth ...)
# -----------------------------------------------------------------------
# shape tells you the SIZE of each dimension as a tuple.
# For a 1D array with 5 elements → shape is (5,)
#   The trailing comma means it's a 1-element tuple (not a mistake!).
#   It means: 5 elements along the only axis.
#
# Pattern:
#   1D → (columns,)          e.g. (5,)
#   2D → (rows, columns)     e.g. (3, 5)
#   3D → (depth, rows, cols) e.g. (2, 3, 5)

print(singleDimension.shape)    # Output: (5,)

# .size → Total Number of Elements
# -----------------------------------------------------------------------
# size gives the TOTAL count of all elements in the array.
# It is simply the product of all values in shape.
# For shape (5,) → size = 5
# For shape (3, 5) → size = 15

print(singleDimension.size)     # Output: 5


# -----------------------------------------------------------------------------
# ndmin → Specify Minimum Number of Dimensions
# -----------------------------------------------------------------------------
# Sometimes you want to force an array to have at least N dimensions.
# Use the ndmin parameter in np.array() to do this.
# This is useful when you need a consistent shape for matrix operations.
#
# Example: wrapping a 1D array into a 2D array using ndmin=2

multiOne = np.array([1, 2, 3, 4, 5], ndmin=2)
print(multiOne)                 # Output: [[1 2 3 4 5]]
#                                          ↑ notice the extra brackets → it's now 2D

print(multiOne.ndim)            # Output: 2  (forced to 2D)
print(multiOne.shape)           # Output: (1, 5)
#                                          ↑  ↑
#                                          |  └─ 5 columns
#                                          └──── 1 row


# -----------------------------------------------------------------------------
# 2D Array (Multi-Dimensional)
# -----------------------------------------------------------------------------
# A 2D array is like a table/matrix with rows and columns.
# Think of it as a spreadsheet: rows going down, columns going across.

multiDimension = np.array([[1, 2, 3],
                            [4, 5, 6],
                            [7, 8, 9]])

print(multiDimension)
# Output:
# [[1 2 3]
#  [4 5 6]
#  [7 8 9]]

print(multiDimension.ndim)      # Output: 2  (2 levels of brackets)
print(multiDimension.shape)     # Output: (3, 3) → 3 rows, 3 columns
print(multiDimension.size)      # Output: 9  → 3 × 3 = 9 total elements


# =============================================================================
# Quick Visual Guide: Dimensions at a Glance
# =============================================================================
# The number of opening brackets [ tells you the number of dimensions.
#
#  1D → [1, 2, 3, 4, 5]
#        ^  → 1 bracket deep → ndim=1 → shape=(5,)
#
#  2D → [[1,2,3], [4,5,6]]
#        ^^  → 2 brackets deep → ndim=2 → shape=(2, 3)  ← 2 rows, 3 cols
#
#  3D → [[[1,2],[3,4]], [[5,6],[7,8]]]
#        ^^^  → 3 brackets deep → ndim=3 → shape=(2, 2, 2)  ← 2 blocks, 2 rows, 2 cols
#
# Shape Formula:
#   1D → (columns,)
#   2D → (rows, columns)
#   3D → (depth, rows, columns)
#   ND → each new dimension adds one more value to the shape tuple
#
# Size Formula:
#   size = shape[0] × shape[1] × shape[2] × ...  (multiply all shape values)
