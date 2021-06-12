from math import atan
from math import pi


def compute_population(t):
    return (172 / 45) * ((pi / 2) - atan((2000 - t) / 45))


years_str_list = input().split()

for year in years_str_list:
    print(f'{int(year):5d} - {compute_population(int(year)):6.3f} миллиард(ов)')
