"""
DESAFIO 059
CALCULADORA SIMPLES
"""
cal = 's'
num1 = float(input('Insira o primeiro número: '))
num2 = float(input('Insira o segundo número: '))

while cal == 's':
    print('=--'*4, ' CALCULADORA ', '--='*4)
    print('=--'*4, '    MENU     ', '--='*4)
    print('[1] somar\n'
          '[2] multiplicar\n'
          '[3] maior\n'
          '[4] novos números\n'
          '[5] sair do programa\n')
    i = int(input('>>> '))
    if i == 1:
        print('{} + {} = {}'. format(num1, num2, num1+num2))
    elif i == 2:
        print('{} x {} = {}'. format(num1, num2, num1*num2))
    elif i == 3:
        if num1 > num2:
            print('Maior valor: {}'.format(num1))
        else:
            print('Maior valor: {}'.format(num2))
    elif i == 4:
        num1 = float(input('Insira o primeiro número: '))
        num2 = float(input('Insira o segundo número: '))
    elif i == 5:
        cal = 'x'
    else:
        print('Opção Inválida!!!')
