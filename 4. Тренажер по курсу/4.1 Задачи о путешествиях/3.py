distances = [int(i) for i in input().split()]
cars = [int(i) for i in input().split()]

bill = 0

for i, _ in enumerate(cars):
    av_cars = cars[i] / distances[i]
    if av_cars <= 30:
        bill += 1
    elif 31 <= av_cars <= 60:
        bill += 1.5
    elif 61 <= av_cars <= 120:
        bill += 3
    elif av_cars > 120:
        bill += 4.5

print(f'Длина пути: {sum(distances):3d} км, оплата: {bill:5.2f} S$')
