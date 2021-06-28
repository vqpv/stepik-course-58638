import numpy as np
import numpy.linalg as alg


A_list = np.array([[1, 1, 1], [-1 / 3, 1, 0], [0, -1 / 3, 1]])
B_list = np.array([2970, 180, 130])

x = np.dot(alg.inv(A_list), B_list)

print(f'{x[0]:4.0f} р., {x[1]:4.0f} р., {x[2]:4.0f} р.')
