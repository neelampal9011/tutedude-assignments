import numpy as np

arr1 = np.arange(1, 11)
arr2 = np.arange(1, 10).reshape(3, 3)
arr3 = np.array([10, 20, 30, 40, 50])

print("1D Array (1-10):")
print(arr1)
print("Shape:", arr1.shape)
print("Data Type:", arr1.dtype)

print("2D Array (3x3):")
print(arr2)
print("Shape:", arr2.shape)
print("Data Type:", arr2.dtype)

print("Array from List:")
print(arr3)
print("Shape:", arr3.shape)
print("Data Type:", arr3.dtype)
