"""
DESAFIO 053
VERIFICAR PALÍNDROMO
"""
p = ''
entrada = str(input('Insira a frase: ')).strip()
frase = entrada.split()
for i in range(0, len(frase)):
    p += frase[i]
contD = len(p)-1
vf = 0
for i in range(0, len(p)):
    print('p[{}]:{} p[{}]: {}'.format(i, p[i], contD, p[contD]))
    if p[i] == p[contD]:
        vf += 1
    contD -= 1
if vf == len(p):
    print('Frase: {} é um Políndromo'.format(entrada))
else:
    print('Frase: {} NÃO é um Políndromo'.format(entrada))

