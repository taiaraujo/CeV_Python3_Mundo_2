# DESAFIO 050
# soma de 6 numeros pares
s = 0
for i in range(0, 6):
    num = int(input('Informe um valor: '))
    if num % 2 == 0:
        s += num
print('Soma dos numeros inteiros: {}'.format(s))
