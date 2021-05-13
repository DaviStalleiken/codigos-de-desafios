from random import randint
from time import sleep
num = int(input('Pensarei em um número entre 0 e 5, tente adivinhá-lo: '))
print('Analisando o número escolhido...')
sleep(1)
sorteado = randint(0, 5)
if num == sorteado:
    print(f'Você ganhou!')
else:
    print(f'O número que pensei era {sorteado}, tente novamente.')
