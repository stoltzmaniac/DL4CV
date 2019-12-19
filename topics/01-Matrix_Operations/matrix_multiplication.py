import numpy as np

# Create matrices
x = np.array([[10, 20], [100, -10]])
y = np.array([[5, 10], [-50, 10]])

# Complete operations and print results
print("\nPerforming Matrix Multiplication (dot product) on matrices\n-------------\n")

print(f"Matrices: \n-------\n  x = \n{x} \n\n y = \n{y}\n\n-------\n")

print("Recall that ELEMENT WISE multiplication resulted in:\n-------\n")

print(f"Multiplication of x * y: \n-------\nnp.multiply(x,y):\n{np.multiply(x,y)}\n\n-------\n\n")

print("Whereas the dot product results in...\n")

print(f"The dot product of x and y:\n-------\nnp.dot(x,y):\n{np.dot(x,y)}\n\n-------\n")

