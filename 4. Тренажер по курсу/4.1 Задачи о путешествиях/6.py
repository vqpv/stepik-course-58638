import numpy as np


country = input()
all_tourists = np.array(input().split(), dtype=float)
polynomial_degree = int(input())
tourists_2018 = float(input())
years = np.array(range(2005, 2018), dtype=float)
a = np.polyfit(years, all_tourists, polynomial_degree)
forecast = np.polyval(a, 2018)
relative_error = abs((forecast - tourists_2018) / tourists_2018) * 100

print(f'Страна:{country:>6s}, прогноз:{forecast:6.3f}млн чел, относительная погрешность:{relative_error:4.2f}проц.')
