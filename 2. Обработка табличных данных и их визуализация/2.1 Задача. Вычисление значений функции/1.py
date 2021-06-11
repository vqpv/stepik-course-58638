def compute_income(deposit, interest_rate, amount_months):
    return deposit * ((1 + (interest_rate / (12 * 100))) ** amount_months)


x, k, n = float(input()), float(input()), int(input())

s = compute_income(x, k, n)

print(round(s - x))
