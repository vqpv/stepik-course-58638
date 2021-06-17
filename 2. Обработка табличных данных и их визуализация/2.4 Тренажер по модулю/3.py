consumed_energy = [int(i) for i in input().split()]
n = float(input())
a = float(input())
b = float(input())

summa = 0

for value in consumed_energy:
    if value <= n:
        summa += value * a
    else:
        summa += (n * a) + (value - n) * b

print(f'Сумма:   {sum(consumed_energy)} кВт ч, стоимость {summa:7.2f} руб')
