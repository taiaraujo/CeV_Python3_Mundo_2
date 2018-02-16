# DESAFIO 039
# identificar tempo de alistamento militar
# ENTRADA: ano de nascimento
# SAÍDA: status / anos que faltam / anos que passaram
from datetime import date
anoN = int(input('Informe o ano de seu nascimento: '))
idade = date.today().year - anoN
if idade < 18:
    print('Você ainda não pode se alistar! Faltam {} anos.'.format(18-idade))
elif idade == 18:
    print('Ano de alistamento para você. Boa Sorte!')
elif idade > 18:
    print('Voce não pode mais se alistar! Passaram-se {} anos.'.format(idade-18))
