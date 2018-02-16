"""
DESAFIO 055
MAIOR E MENOR PESO
"""
menorP = float(input('Informe o peso da 1ª pessoa: '))
maiorP = menorP
for i in range(0, 4):
    peso = float(input('Informe o peso da {}ª pessoa: '.format(i+2)))
    if peso > maiorP:
        maiorP = peso
    if peso < menorP:
        menorP = peso
print('O maoir peso informado foi: {} e o menor foi: {}'.format(maiorP, menorP))
