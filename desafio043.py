# DESAFIO 041
# calcular IMC
# ENTRADA: peso e altura
# SAÍDA: status
# CONDIÇÃO: tabela IMC
from time import sleep
print('*'*7, ' CALCULANDO IMC ', '*'*7)
altura = float(input('Informe sua altura: '))
peso = float(input('Informe se peso: '))
imc = peso / altura ** 2
print('Calculando...')
sleep(3)
if imc < 18.5:
    print('Você está abaixo do peso recomendado')
elif 18.5 <= imc < 25:
    print('Você está com o peso recomendado')
elif 25 <= imc < 30:
    print('Você está com sobrepeso')
elif 30 <= imc < 40:
    print('Obesidade')
else:
    print('Obesidade mórbida')
