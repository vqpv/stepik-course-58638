import numpy as np


path = np.array(input().split(), dtype=int)
speed = np.array(input().split(), dtype=int)
start = int(input())
end = int(input())

sum_p = sum(path[start:end + 1])
sum_p_s = sum(path[start:end + 1] / speed[start:end + 1])

print(f'S = {sum_p:3d} км, T = {sum_p_s:5.2f} час, V = {sum_p / sum_p_s:5.2f} км/ч')
