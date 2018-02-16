while True:
    num = int(input('Informe um valor para a tabuada: '))
    if num < 0:
        break
    else:
        print('-'*12)
        for i in range(0, 11):
            print('{} x {} = {}'.format(num, i, num*i))
        print('-'*12)
