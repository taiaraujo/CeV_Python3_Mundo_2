import emoji
import random
# PEDRA: print(emoji.emojize(":punch:", use_aliases=True))
# PAPEL: print(emoji.emojize(":punch:", use_aliases=True))
# TESOURA: print(emoji.emojize(":v:", use_aliases=True))
# Jokenpô
# DESAFIO 045
# Programadora: Taia Araújo
endgame_false = True

while (endgame_false): 
    print('\n', '#'*17, '\n', '*'*3, ' JOKENPÔ ', '*'*3, '\n', '#'*17, '\nESCOLHA: ')
    print(emoji.emojize("[1] PEDRA: :punch:", use_aliases=True))
    print(emoji.emojize("[2] PAPEL: :raised_hand:", use_aliases=True))
    print(emoji.emojize("[3] TESOURA: :v:", use_aliases=True))
    jog = int(input('>>> '))
    pc = random.randint(1, 3)
    print('JOGADOR X COMPUTADOR')
    # MOSTRAR ESCOLHA DO JOGADOR
    if jog == 1:
        print(emoji.emojize("   :punch:", use_aliases=True), end='    ')
    elif jog == 2:
        print(emoji.emojize("   :raised_hand:", use_aliases=True), end='    ')
    elif jog == 3:
        print(emoji.emojize("   :v:", use_aliases=True), end='    ')
    else:
        print(emoji.emojize('PERDEU, ESCOLHA INVÁLIDA :no_good:', use_aliases=True))
    # MOSTRAR ESCOLHA DO PC
    if pc == 1:
        print(emoji.emojize("     :punch:", use_aliases=True))
    elif pc == 2:
        print(emoji.emojize("     :raised_hand:", use_aliases=True))
    elif pc == 3:
        print(emoji.emojize("     :v:", use_aliases=True))
    # JOGO DE FATO
    if jog != pc:
        endgame_false = False
        if jog == 1 and pc == 2:
            print("COMPUTADOR GANHOU")
        elif jog == 1 and pc == 3:
            print("VOCÊ GANHOU")
        elif jog == 2 and pc == 1:
            print("VOCÊ GANHOU ")
        elif jog == 2 and pc == 3:
            print("COMPUTADOR GANHOU")
        elif jog == 3 and pc == 1:
            print("COMPUTADOR GANHOU")
        elif jog == 3 and pc == 2:
            print("VOCÊ GANHOU")
    else:
        print('EMPATE')
