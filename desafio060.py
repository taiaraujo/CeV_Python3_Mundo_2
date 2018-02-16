"""
DESAFIO 060
FATORIAL
"""
f = 1
fat = int(input('Informe um valor: '))
while fat > 0:
    print('{}'.format(fat), end=" ")
    print(' x ' if fat > 1 else ' = ', end=" ")
    f *= fat
    fat -= 1
print(' {}'.format(f))
