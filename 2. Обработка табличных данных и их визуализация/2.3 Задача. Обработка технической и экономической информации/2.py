from math import atan
from math import pi


def compute_population(t):
    return (172 / 45) * ((pi / 2) - atan((2000 - t) / 45))


years = [1000, 1750, 1800, 1850, 1900, 1950, 1955,
         1960, 1965, 1970, 1975, 1980, 1985, 1990, 1995,
         2000, 2005, 2010, 2011, 2012, 2013, 2014, 2015,
         2016, 2017, 2018, 2019]

population = [0.400, 0.791, 1.000, 1.262, 1.650, 2.519,
              2.756, 3.021, 3.335, 3.692, 4.068, 4.435, 4.831,
              5.264, 5.674, 6.071, 6.344, 6.933, 7.015, 7.100,
              7.162, 7.271, 7.358, 7.444, 7.530, 7.669, 7.763]


first_index, last_index = int(input()), int(input()) + 1

relative_errors = []
selected_years = years[first_index:last_index]
selected_population = population[first_index:last_index]

for index, year in enumerate(selected_years):
    relative_errors.append(abs(((selected_population[index] - compute_population(year)) / selected_population[index]) * 100))

print(f'Погрешность - минимальная, год: {selected_years[relative_errors.index(min(relative_errors))]:4d}, '
      f'максимальная, год: {selected_years[relative_errors.index(max(relative_errors))]:4d}, '
      f'средняя, процент: {sum(relative_errors) / len(relative_errors):6.3f}')
