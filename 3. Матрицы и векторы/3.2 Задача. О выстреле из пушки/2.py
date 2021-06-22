import numpy as np


def get_lin(x, a):
    return a[0] * x + a[1]


def get_quad(x, a):
    return a[0] * (x ** 2) + (a[1] * x) + a[2]


def relative_error(y, yr):
    return abs((y - yr) / yr) * 100


x_array = np.array(input().split(), dtype=float)
y_array = np.array(input().split(), dtype=float)

a_lin = np.polyfit(x_array, y_array, 1)
a_quad = np.polyfit(x_array, y_array, 2)

s1 = sum(relative_error(y_array, get_lin(x_array, a_lin)))
s2 = sum(relative_error(y_array, get_quad(x_array, a_quad)))

if s1 < s2:
    print(f'{a_lin[0]:5.3f} {a_lin[1]:5.3f}')
else:
    print(f'{a_quad[0]:5.3f} {a_quad[1]:5.3f} {a_quad[2]:5.3f}')
