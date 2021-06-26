import numpy as np


r = np.array(input().split(), dtype=float)
i = np.array(input().split(), dtype=float)

R = 1 / (sum(1 / r))

print(f'R = {R:6.3f} Ом, I = {sum(i):6.3f} А, U = {(sum(i) * R):6.3f} В')
