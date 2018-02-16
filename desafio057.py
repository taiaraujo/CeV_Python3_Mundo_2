"""
DESAFIO 057
"""
sexo = str(input('Informe seu sexo: [f/m]: ')).strip()[0]
while sexo not in 'MmFf':
    sexo = str(input('Tente novamente! Digite seu sexo [f/m]: '))
print('sexo: ', sexo)
