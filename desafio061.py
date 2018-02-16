"""
DESAFIO 061
REFAZER O DESAFIO 051
PROGRESSÃO ARITMETICA (PA)
ENTRADA: primeiro termo e a razão
SAÍDA: os 10 primeiros termos da PA
"""
p1 = int(input('Informe o primeiro termo da PA: '))
r = int(input('Informe a razão da PA: '))
n = 1
t = 10
while n < t + 1:
    pa = p1 + (n-1) * r
    print('{}'.format(pa), end=' ')
    n += 1
    if n == t + 1:
        t = int(input('\n Mais quantos termos: '))
        if t != 0:
            t += n - 1
