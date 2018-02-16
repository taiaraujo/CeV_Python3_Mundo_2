# DESAFIO 037
# CONVERSÃO PARA DIFERENTES BASES NUMERICAS
# ENTRADA: numero inteiro qualquer / escolha da base
# SAÍDA: numero convertido
# CONDIÇÃO: se 1: binário / se 2: octal / se 3: hexadecimal

num = int(input('Informe um número inteiro: '))
op = int(input('Escolha qual base de conversão digite:\n[1] >> Binário'
               '\n[2] >> Octal\n[3] >> Hexadecimal\n: '))
if op == 1:
    conv = bin(num)
    print('O número {} foi converto para Binário. Resultado: {}'.format(num, conv[2:]))
elif op == 2:
    conv = oct(num)
    print('O número {} foi converto para octal. Resultado: {}'.format(num, conv[2:]))
elif op == 3:
    conv = hex(num)
    print('O número {} foi converto para Hexadecimal. Resultado: {}'.format(num, conv.upper()[2:]))
else:
    print('ESCOLHA INVÁLIDA!')
