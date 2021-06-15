t_0 = input().split()
t_12 = input().split()
t_a = float(input())

for i in range(len(t_0)):
    if (float(t_0[i]) + float(t_12[i])) / 2 > t_a:
        print(i)
