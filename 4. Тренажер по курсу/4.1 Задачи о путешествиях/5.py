from math import cos
from math import pi

H = int(input())
T = int(input())
t = float(input())

print(f'Высота = {(H / 2) * (1 - cos(2 * pi * t / T)):6.2f} м' if 0 <= t <= T else 'error')
