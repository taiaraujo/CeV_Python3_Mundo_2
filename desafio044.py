""" DESAFIO 044
    calculando condições pagamento
    ENTRADA: preço da compra e condição de pagamento
    SAIDA: condição escolhida e valor final da compra / valor das parcelas
    CONDIÇÃO: forma de pagamento """
valorC = float(input('Informe o valor da compra: '))
print('*'*5, 'CONDIÇÃO DE PAGAMENTO', '*'*5)
formaP = int(input('[1] >>> À VISTA NO DINHEIRO OU CARTÃO'
                   '\n[2] >>> À VISTA NO CARTÃO'
                   '\n[3] >>> 2X NO CARTÃO'
                   '\n[4] >>> 3X ou + NO CARTÃO\n >>> '))
if formaP == 1:
    nValor = valorC - (valorC*0.1)
    print('Valor da compra: {}\nVocê obteve 10% de desconto por ser à vista'
          '\nValor final: {}'.format(valorC, nValor))
elif formaP == 2:
    nValor = valorC - (valorC * 0.05)
    print('Valor da compra: {}\nVocê obteve 5% de desconto por ser à vista'
          'Valor final: {}'.format(valorC, nValor))
elif formaP == 3:
    print('Valor da compra: {}\nCompra parcelada em 2x no cartão\n'
          'Valor da parcela: {}'.format(valorC, valorC/2))
elif formaP == 4:
    parcelaC = int(input('Confirme o número de parcelas: '))
    nValor = valorC + (valorC*0.2)
    print('Valor da compra: {}\nCompra parcelada {}x no cartão com juros de 20%\n'
          'Valor final da compra: {}\n'
          'Valor da parcela: {}'.format(valorC, parcelaC, nValor, nValor/parcelaC))
else:
    print('CONDIÇÃO DE PAGAMENTO INEXISTENTE')
print('Volte Sempre!')



