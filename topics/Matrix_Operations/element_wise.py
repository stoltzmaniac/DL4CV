import numpy as np


def print_all(): 

    print("------------------------------------------------------")
    print("[START] - ELEMENT WISE OPERATIONS BETWEEN TWO MATRICES")
    print("------------------------------------------------------")

    # Create matrices
    x = np.array([[10, 20], [100, -10]])
    y = np.array([[5, 10], [-50, 10]])

    print(f"Matrices: \n-------\n  x = \n{x} \n\n y = \n{y}\n\n-------\n")

    print(f"Addition of x + y: \n-------\nnp.add(x,y):\n{np.add(x,y)}\n\n-------\n")

    print(f"Subtraction of x - y: \n-------\nnp.subtract(x,y):\n{np.subtract(x,y)}\n\n-------\n")

    print(f"Multiplication of x * y: \n-------\nnp.multiply(x,y):\n{np.multiply(x,y)}\n\n-------\n")

    print(f"Division of x / y: \n-------\nnp.divide(x,y):\n{np.divide(x,y)}\n\n-------\n")

    print("-------------------------------------------------------")
    print("[FINISH] - ELEMENT WISE OPERATIONS BETWEEN TWO MATRICES")
    print("-------------------------------------------------------")