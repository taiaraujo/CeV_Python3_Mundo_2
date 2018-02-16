# DESAFIO 041
# categoria para Confereração Nacional de Natação
# ENTRADA: ano de nascimento
# SAÍDA: categoria do atleta
# CONDIÇÃO: idade<=9 mirim / 9<idade<=14 infantil / 14<idade<=19 junior / idade==20 sênior / idade > 20 master
from datetime import date
anoN = int(input('Informe o seu ano de nascimento: '))
idade = date.today().year - anoN
print('{} anos'. format(idade))
print('Sua categoria é:', end=" ")
if idade <= 9:
    print('Mirim')
elif 9 < idade <= 14:
    print('Infantil')
elif 14 < idade <= 19:
    print('Junior')
elif idade == 20:
    print('Sênior')
else:
    print(' Master')
