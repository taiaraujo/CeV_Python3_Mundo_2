"""
DESAFIO 051
PROGRESSÃO ARITMETICA (PA)
ENTRADA: primeiro termo e a razão
SAÍDA: os 10 primeiros termos da PA
"""
p1 = int(input('Informe o primeiro termo da PA: '))
r = int(input('Informe a razão da PA: '))
for n in range(1, 11):
    pa = p1 + (n-1) * r
    print('termo[{}]: {}'.format(n, pa))
