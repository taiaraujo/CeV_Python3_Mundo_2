"""
DESAFIO 068
JOGO DE PAR OM IMPAR
"""
from random import randint
cont = 0
pcV = 1
while True:
    pc = randint(1, 5)
    escJ = str(input('[PAR ou IMPAR]? ')).strip()[0].lower()
    numJ = int(input('Informe um número [1 a 5]: '))
    if numJ > 5 or escJ not in 'ip':
        print('Escolha inválida! Tente de novo')
    else:
        soma = pc + numJ
        if soma % 2 == 0:
            if escJ in 'p':
                print('Parabéns!!!! Você ganhou')
                cont += 1
            elif escJ in 'i':
                print('O computador ganhou...')
                pcV = 0
            print('Você jogou {} e o computador jogou {}. Total de {} é PAR'.format(numJ, pc, soma))
        else:
            if escJ in 'i':
                print('Parabéns!!! Você ganhou')
                cont += 1
            elif escJ in 'p':
                print('O computador ganhou...')
                pcV = 0
            print('Você jogou {} e o computador jogou {}. Total de {} é ÍMPAR'.format(numJ, pc, soma))
    if pcV == 0:
        break
print('GAME OVER!\n Você venceu {} vezes.'.format(cont))