"""
DESAFIO 064
LER NUMEROS INTEIROS ATÉ O USUARIO DIGITAR 999
"""
n = 0
s = 0
c = 0
while n != 999:
    n = int(input('Digite um número: '))
    if n != 999:
        s += n
        c += 1
print('Foram digitados {} números, e a sua soma é: {}'. format(c, s))
