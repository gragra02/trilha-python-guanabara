#Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para
#o usuário tentar descobrir qual foi o número escolhido pelo computador. 
#O programa deverá escrever na tela se o usuário venceu ou perdeu.

import random
from time import sleep

print('Vou pensar em um número entre 0 e 5. Tente adivinhar!')
numero_pc = random.randint(0 , 5)
numero_usuario = int(input('Em que número eu pensei?'))
print('Estou pensando...')
sleep(3)
if numero_usuario == numero_pc:
    print('Parabéns! Você acertou!')
else:
    print(f'Erroooooou!! Eu pensei no número {numero_pc}')

print('FIM')