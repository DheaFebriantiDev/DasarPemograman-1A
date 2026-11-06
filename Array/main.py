import numpy as np

'''arra 1D'''
arr = np.array([1, 2, 3, 4, 5])
print(arr)
print(type(arr))

list = [1, 2, 3, 4, 5]
print(list)
print(type(list))

arr2d = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2d)

arr3d = np.array([ [[1, 2], [3, 4]], [[5,6], [7, 8]], [[9, 10], [11, 12]] ])
print(arr3d)

print(arr.ndim)
print(arr2d.ndim)
print(arr3d.ndim)

print(arr.dtype)
arr1d = np.array([1, 2, 3, 4, 5], dtype="S")
print(arr)
print(arr1d.dtype)