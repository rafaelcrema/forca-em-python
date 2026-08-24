import random
from palavras import facil, medio, dificil

lista_palavras = []
jogar = 0


VERDE = '\033[32m'
VERMELHO = '\033[31m'
RESET = '\033[0m'


while jogar == 0:

    tentativas = 5

    letra_escolhidas = []
    letras_erradas = []

    dificuldade = input('''
Escolha a dificuldade:
[1] Facil
[2] Médio
[3] Difícil 
>.''')


    if dificuldade == '1':
        lista_palavras = facil
    elif dificuldade == '2':
        lista_palavras = medio
    elif dificuldade == '3':
        lista_palavras = dificil
    else:
        print('Escolha invalida!')
        continue

    palavra_escolhida = random.choice(lista_palavras).strip()

    while tentativas > 0:

        palavra_oculta = ''

        letra_escolhida = input('\nDigite uma letra: ')
        letra_escolhidas.append(letra_escolhida)

        for i in palavra_escolhida:
            if i in letra_escolhidas:
                palavra_oculta += f'{VERDE}{i}{RESET} '
            else:
                palavra_oculta += '- '

        print(palavra_oculta.strip(),end=' ')

        if letra_escolhida not in palavra_escolhida:
            letras_erradas.append(letra_escolhida)
            tentativas -= 1
            print(f'Você errou, você tem {VERDE}{tentativas}{RESET} tentativas')
        print('Letras Erradas', end=' ')

        for letra in letras_erradas:
            print(f'{VERMELHO}{letra}{RESET}', end=' ')

        if '-' not in palavra_oculta:
            print(f'\nVocê acertou! A palavra é {palavra_escolhida}\n')
            break

        elif tentativas == 0:
            print(f'\n{VERMELHO}Você perdeu{RESET}\nA palavra escolhida era {VERDE}{palavra_escolhida}{RESET}\n')
            break

    jogar_denovo = input('''
Quer jogar De novo?
[0] Sim
[1] Parar
''')

    if jogar_denovo == '0':
        jogar = 0
    else:
        break
