"""
DESAFIO 056
GRUPO DE 4 PESSOAS
ENTRADA: NOME, IDADE E SEXO
SAÍDA: MÉDIA DE IDADE, NOME DO HOMEM MAIS VELHO E QUANTIDADE DE MULHES ABAIXO DE 20 ANOS
"""
mediaI = 0
qtm20 = 0
hv = 0
for i in range(0, 4):
    nome = str(input('Informe o nome da {} pessoa: '.format(i+1)))
    idade = int(input('Informe a idade da {} pessoa: '.format(i+1)))
    sexo = str(input('Informe o sexo [F] ou [M] da {} pessoa: '.format(i+1)))
    mediaI += idade
    if sexo == 'F' and idade < 20:
        qtm20 += 1
    if sexo == 'M' and hv < idade:
        nomeH = nome
print('A média de idade do grupo: {}'
      'O nome do homem mais velho: {}'
      ' Quantidade de mulhes abaixo de 20 anos: {}'.format(mediaI/4, nomeH, qtm20))

