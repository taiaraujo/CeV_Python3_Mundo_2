cont = soma = 0
while True:
    num = int(input('Informe um valor [999 para parar]: '))
    if num == 999:
        break
    soma += num
    cont += 1
print('A soma dos {} valores foi {}'.format(cont, soma))
