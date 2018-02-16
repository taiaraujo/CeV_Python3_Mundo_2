laco = 's'
cont = 0
while laco == 's':
    num = int(input('Informe {}º valor: '.format(cont+1)))
    if cont == 0:
        maiorN = num
        menorN = num
        soma = num
    else:
        soma += num
        if maiorN < num:
            maiorN = num
        if menorN > num:
            menorN = num
    cont += 1
    laco = str(input('Deseja continuar [s/n]: '))
print('Média dos números digitados: {:.1f}\n'
      'Maior número: {}\n'
      'Menor número: {}'.format(soma/cont, maiorN, menorN))
