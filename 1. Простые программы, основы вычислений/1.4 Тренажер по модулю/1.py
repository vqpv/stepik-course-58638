v = float(input())

if v <= 0:
    print('error')

elif v <= 7.8:
    print('0')

elif 7.8 < v < 11.2:
    print('1')

elif 11.2 <= v <= 16.4:
    print('2')

elif v > 16.4:
    print('3')
