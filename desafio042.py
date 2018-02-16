# DESAFIO 042
# refazer o desafio 035 do mundo 1
# ENTRADA: 3 lados de um possíve triângulo
# SAÍDA: status/ tipo de triângulo
# CONDIÇÃO: matemática
a = float(input('Informe o lado a: '))
b = float(input('Informe o lado b: '))
c = float(input('Informe o lado c: '))
sub = b - c
# garante o modulo da subtração >> sub = |b - c|
if sub < 0:
    sub = sub * (-1)
soma = b + c
if sub < a < soma:
    print('forma um triângulo', end=' ')
    if a == b == c:
        print('equilátero')
    elif a != b != c != a:
        print('escaleno')
    else:
        print('isósceles')
else:
    print('não forma triangulo')
