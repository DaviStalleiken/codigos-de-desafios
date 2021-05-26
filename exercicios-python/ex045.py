from random import randint
from time import sleep
itens = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)
print('''OPÇÕES
[0] Pedra
[1] Papel
[2] Tesoura''')
jogada = int(input('Qual é a sua jogada? '))
print('JO!')
sleep(1)
print('KEN!')
sleep(1)
print('PO!')
sleep(1)
print(f'-=' * 11)
print(f'Computador jogou {itens[pc]}')
print(f'Jogador jogou {itens[jogada]}')
print(f'-=' * 11)

if pc == 0:             #Pc = Pedra
    if jogada == 0:
        print('Empate!')
    elif jogada == 1:
        print('Você venceu!')
    elif jogada == 2:
        print('Você perdeu!')
    else:
        print('Jogada \033[31minválida\033[m')
elif pc == 1:           #Pc = Papel
    if jogada == 0:
        print('Você perdeu!')
    elif jogada == 1:
        print('Empate!')
    elif jogada == 2:
        print('Você venceu!')
    else:
        print('jogada \033[31minválida\033[m')
elif pc == 2:           #Pc = Tesoura
    if jogada == 0:
        print('Você venceu!')
    elif jogada == 1:
        print('Você perdeu!')
    elif jogada == 2:
        print('Empate!')
    else:
        print('jogada \033[31minválida\033[m')
