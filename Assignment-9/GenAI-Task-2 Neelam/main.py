import numpy as np

A = np.array([10, 20, 30, 40])
B = np.array([1, 2, 3, 4])

print("array A:", A)
print("array B:", B)

print("addition (A + B):", A+B)
print("subtraction (A - B):", A-B)
print("multiplication (A * B):", A*B)
print("division (A / B):", A/B)
print("power (A ** 2):", A**2)

print("addition (A + B):", np.add(A, B))
print("subtraction (A - B):", np.subtract(A, B))
print("multiplication (A * B):", np.multiply(A, B))
print("division (A / B):", np.divide(A, B))
print("power (A ** 2):", np.power(A, 2))
