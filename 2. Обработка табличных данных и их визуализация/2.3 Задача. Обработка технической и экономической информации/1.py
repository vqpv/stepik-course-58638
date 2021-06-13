def compute_payment(t, s, n, k):
    return (s / n) + (s - (t - 1) * (s / n)) * (k / (12 * 100))


_s, _n, _k = int(input()), int(input()), int(input())
payment_sum = 0

for _t in range(1, _n + 1):
    payment_sum += compute_payment(_t, _s, _n, _k)
    print(f'{_t:2d} месяц - {compute_payment(_t, _s, _n, _k):8.2f} руб')

print(f'Доход банка - {payment_sum - _s:6.2f} руб')
