import numpy as np


a = np.array(input().split(), dtype=float)
h = np.array(input().split(), dtype=float)

v = 1 / 3 * h * a ** 2
s = 2 * a * (0.25 * a ** 2 + h ** 2) ** 0.5

print(f'Vmax: {np.argmax(v):2d}, {max(v):8.2f}, Smin: {np.argmin(s):2d}, {min(s):8.2f}')
