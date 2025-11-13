# Maior e menor valores em Tupla
from random import randint
numero = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))
print("Os valores sorteados foram: ")
for n in numero:
    print(f'{n}', end=' ')
print(f'\nO maior valor sorteado foi {max(numero)}')
print(f'O menor valor sorteado foi {min(numero)}')