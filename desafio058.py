"""
DESAFI 058
MELHORAR O DESAFIO 028
DESCOBRIR O NUMERO QUE O PC "PENSOU"
"""
from random import randint
pc = randint(1, 10)
c = 0
t = 0
while c != pc:
    c = int(input('Qual foi o número que o compuador pensou? '))
    if c == pc:
        print('PARABÉNS VC ACERTOU')
    else:
        if c > pc:
            print('Menos... ', end='')
        if c < pc:
            print('Mais... ', end='')
        print('Tente mais uma vez ')
        t += 1
print('Computador pensou: {}\n E vc precisou de {} tentativas'.format(pc, t))
