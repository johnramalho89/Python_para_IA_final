import numpy as np

array1 = np.array([1, 2, 3, 5, 6])

array2 = np.array([
    [[1.5, 2.8, 3.9]],
    [[1.5, 2.0, 3.5]]
])

print("array1.ndim:", array1.ndim)
print("array2.ndim:", array2.ndim)

print("array1.shape:", array1.shape)
print("array2.shape:", array2.shape)

print("array1.size:", array1.size)
print("array2.size:", array2.size)

print("array1.dtype:", array1.dtype)
print("array2.dtype:", array2.dtype)

print("array1.itemsize:", array1.itemsize)
print("array2.itemsize:", array2.itemsize)
