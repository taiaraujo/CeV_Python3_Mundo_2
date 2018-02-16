"""
DESAFIO 063
FIBONACCI
"""
n1 = 0
n2 = 1
c = 0
t = int(input('Informe o número de termos para FIBONACCI: '))
print('{} {}'.format(n1, n2), end='')
while c < t-2:
    f = n1 + n2
    n1 = n2
    n2 = f
    c += 1
    print(' {}'.format(f), end='')
