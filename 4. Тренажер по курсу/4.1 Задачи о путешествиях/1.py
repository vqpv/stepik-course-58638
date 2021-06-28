k, p, s = float(input()), float(input()), float(input())

price_by_plane = k * 3
price_by_car = p * (s / 100) * 12 * 2

if (k <= 0) or (p <= 0) or (s <= 0):
    print('error')
else:
    print(round(min(price_by_plane, price_by_car), 2))
