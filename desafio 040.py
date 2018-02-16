# DESAFIO 040
# media de um ano
# ENTRADA: duas notas
# SAÍDA: status

n1 = float(input('Informe a primeira nota: '))
n2 = float(input('Informe a segunda nota: '))
m = (n1 + n2) / 2
if m < 5.0:
    print('REPROVADO')
elif 5.0 <= m < 6.9:
    print('RECUPERAÇÃO')
elif m >= 7.0:
    print('APROVADO')
