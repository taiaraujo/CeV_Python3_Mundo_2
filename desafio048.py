s = 0
for i in range(1, 501):
    if i % 2 == 1 and i % 3 == 0:
        s += i
print('Soma dos impares multiplos de 3 no intervalo de 1 a 500: {}'.format(s))

