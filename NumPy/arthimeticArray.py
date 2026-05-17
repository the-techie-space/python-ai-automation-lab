import numpy as np # type: ignore


#scalar arthimetics 

array = np.array([1,2,3])

print(array) # [1 2 3]
print(array + 2) # [3 4 5]
print(array - 2) # [-1 0 1]
print(array * 2) # [2 4 6]
print(array / 2) # [0.5 1.  1.5]
print(array ** 2) # [1 4 9]

#vectorised math functions 


print(np.sqrt(array))
print(np.pi)

radii = array

print(np.pi * radii ** 2)

values = np.array([1,2,3.23,4.69,5.99])

print(values.round())
print(np.floor(values))
print(np.ceil(values))


#Element wise operations

array1 = np.array([1,2,3])
array2 = np.array([4,5,6])

#Note for these operations dimensions and size should be same

print(array1 + array2) # [5 7 9]
print(array1 - array2) # [-3 -3 -3]
print(array1 * array2) # [ 4 10 18]
print(array1 / array2) # [0.25 0.4  0.5 ]
print(array1 ** array2) # [  1  32 729]


#comparisons operations

rank = np.array([11,34,56,22,77,1,5,2,8,77,100,95,69])


#generally it returns the true or false for that value that what we see
print(rank > 50) # [False False  True False  True False False False False  True  True  True
  
# to see actual value we need to filter using this method
print(rank[rank > 50]) # [56 77 77 100 95 69]

#maniplation
rank[rank >10] = 0
print(rank)


#Broadcasting

#broadcasting is a mechanism that allows NumPy to perform operations on arrays of different shapes and sizes.
#it is a way to perform operations on arrays of different shapes and sizes.
# it should match condition like 
# 1) dimension have same size 
# 2) ONE OF THE dimension have size 1


arr1 = np.array([[1,2,3,4]])
arr2 = np.array([[1],[2],[3],[4]])

print(arr1.shape) # (1, 4)
print(arr2.shape) # (4, 1)

# arr1 is (1,4) and arr2 is (4,1)
#we have satisfied condition like 1 is present in each one of dimention
# it will broadcast the arr1 to (4,4) and arr2 to (4,4)
# then it will perform the operation

print(arr1 * arr2) 
# [[ 1  2  3  4]
# [ 2  4  6  8]
# [ 3  6  9 12]
# [ 4  8 12 16]]

arr1 = np.array([[1,2,3,4]])
arr2 = np.array([[1],[2],[3]])

print(arr1.shape) # (1, 4)
print(arr2.shape) # (3, 1)

# arr1 is (1,4) and arr2 is (3,1)
#we have satisfied condition like 1 is present in each one of dimention
# it will broadcast the arr1 to (3,4) and arr2 to (3,4)
# then it will perform the operation

print(arr1 * arr2) 
# [[ 1  2  3  4]
# [ 2  4  6  8]
# [ 3  6  9 12]]

arr1 = np.array([[1,2,3,4],[5,6,7,8]])
arr2 = np.array([[1],[2],[3]])

print(arr1.shape) # (2, 4)
print(arr2.shape) # (3, 1)

# arr1 is (2,4) and arr2 is (3,1)
#here no condition is satisfied hence we cant perform broadcasting
# it will broadcast the arr1 to (3,4) and arr2 to (3,4)
# then it will perform the operation

#print(arr1 * arr2)  -> Error



#Aggregation functions = summerize the data and return single value

arrayAgg = np.array([1,2,3,4,5])

print(arrayAgg.sum()) # 15
print(arrayAgg.mean()) # 3.0
print(arrayAgg.min()) # 1
print(arrayAgg.max()) # 5
print(arrayAgg.std()) # 1.4142135623730951
print(arrayAgg.var()) # 2.0
print(arrayAgg.argmin()) # 0
print(arrayAgg.argmax()) # 4
print(arrayAgg.cumsum()) # [ 1  3  6 10 15]
print(arrayAgg.cumprod()) # [  1   2   6  24 120]


#filter advance

rank = np.array([11,34,56,22,77,1,5,2,8,77,100,95,69])

print(rank[rank > 50]) # [56 77 77 100 95 69]

print(rank > 50) # [False False  True False  True False False False False  True  True  True
  

#here we are not preserving false data or filtered data to do that we use where

output = np.where(rank > 50, rank, 0)
print(output) # [ 0  0 56  0 77  0  0  0  0 77 100 95 69] # preserving false data



