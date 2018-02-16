# DESAFIO 038
# COMPARAR DOIS NUMEROS
# ENTRADA: dois números inteiros
# SAÍDA: status da relação dos números
# CONDIÇÃO: maior e menor / iguais

n1 = int(input('Informe um número: '))
n2 = int(input('Informe outro número: '))
if n1 > n2:
    print('Primeiro valor [{}] é maior que o segundo valor [{}]'.format(n1, n2))
elif n1 < n2:
    print('Segundo valor [{}] é maior que o Primeiro valor [{}]'.format(n2, n1))
else:
    print('Primeiro valor {} é igual ao segundo valor {}'.format(n1, n2))