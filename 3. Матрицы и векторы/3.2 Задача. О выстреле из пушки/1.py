import numpy as np


def get_trend(x, a):
    return a[0] * (x ** 2) + (a[1] * x) + a[2]


x_array = np.array(input().split(), dtype=float)
h_array = np.array(input().split(), dtype=float)


_a = np.polyfit(x_array, h_array, 2)
h_zero = get_trend(0, _a)
h_target = get_trend(float(input()), _a)

ans = ('yes' if abs(float(input()) - h_target) <= 0.5 else 'no')

print(f'h0 = {h_zero:6.2f}, {ans:2s}')
