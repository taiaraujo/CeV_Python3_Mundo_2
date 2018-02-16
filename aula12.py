# CONDIÇÕES ANINHADAS
nome = str(input('Qual seu nome? '))
if nome == 'Gustavo':
    print('Que nome bonito')
elif nome == 'Pedro' or nome == "Maria" or nome == 'Paulo':
    print('Seu nome é bem popular no Brasil')
elif nome in 'Ana Claúdia Jéssica Juliana':
    print('Belo nome feminino')
else:
    print('Seu nome é em normal')
print('Tenha um bom dia')
