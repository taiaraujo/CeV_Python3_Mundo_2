"""
DESAFIO 054
MOSTRAR QUANTIDADE DE PESSOAS COM MAIOR E MENOR IDADE
"""
from datetime import date
maiorI = 0
menorI = 0
for i in range(0, 7):
    anoN = int(input('Informe o ano de nascimento da {}ª pessoa: '.format(i+1)))
    idade = date.today().year - anoN
    if idade < 21:
        menorI += 1
    else:
        maiorI += 1
print('{} pessoas não atigiram a maioridade e {} já são maiores'.format(menorI, maiorI))
