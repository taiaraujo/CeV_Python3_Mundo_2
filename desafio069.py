"""
DESAFIO 069
ANALISE DE DADOS
"""
cont = 's'
p18 = h = m20 = 0
while True:
    idade = int(input('Informe sua idade: '))
    sexo = str(input('e informe o sexo [F / M]')).strip()[0].lower()
    if idade > 18:
        p18 += 1
    if sexo in 'm':
        h += 1
    if sexo in 'f' and idade < 20:
        m20 += 1
    cont = str(input('Deseja continuar [s/n]: ')).strip()[0].lower()
    if cont not in 's':
        break
print('Tem {} pessoas maiores de 18 anos\n'
      'Tem {} homens\n'
      'Tem {} mulheres com menos de 20 anos'.format(p18, h, m20))
