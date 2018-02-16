# DESAFIO 036
# Aprovar empréstimo bancário para a compra de um casa
# ENTRADA: valor da casa / salário do comprador / anos de parcelamento
# SAÍDA: status do empréstimo / valor da parcela
# CONDIÇÃO: parcela não pode exceder de 30% do salário do comprador

print('===//'*20)
print('Bem vindo(a) a simulação de empréstimo ')
print('===//'*20)
vc = float(input('Informe o valor da casa: '))
sal = float(input('Informe seu salário: '))
an = int(input('Em quantos anos você pretende financiar: '))
parcela = vc / (an*12)
if parcela > sal*0.3:
    print('Seu empréstimo não foi aprovado! Valor da parcele excedeu 30% do seu salário')
else:
    print('Parabéns! Seu empréstimo foi aceito\nValor da parcela: {:.2f}'.format(parcela))
