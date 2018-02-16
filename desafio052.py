"""
DESAFIO 052
RECONHECER SE UM NÚMERO É PRIMO
"""
for x in range(0, 2):
    p = 0
    print('\033[30m', end='')
    num = int(input('Informe um número: '))
    for i in range(1, num+1):
        if num % i == 0:
            print('\033[33m', end='')
            p += 1
        else:
            print('\033[31m', end='')
        print(' {}'.format(i), end='')
    print('\n Número {}'.format(num), end='')
    if p == 2:
        print(' é Primo, ele é divisivel apenas por 1 e por ele mesmo')
    else:
        print(' não é primo, ele é divisivel por todos os números destacados acima')
    print('\033[30m', end='')
    print('=--' * 10)