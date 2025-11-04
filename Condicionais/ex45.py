#Crie um programa que faça o computador jogar Jokenpô com você.
import random
import time

itens = ('Pedra', 'Papel', 'Tesoura'   )
computador = random.randint(0, 2)
print('''Suas opções:
[0] Pedra
[1] Papel
[2] Tesoura''')
jogador = int(input('Qual é a sua jogada? '))
print('JO')
time.sleep(1)  
print('KEN')
time.sleep(1)
print('PÔ!!!')
print('-=' * 11)
print(f'Computador jogou {itens[computador]}')
print(f'Jogador jogou {itens[jogador]}')
print('-=' * 11)
if computador == 0: #Computador jogou Pedra
    if jogador == 0:
        print('EMPATE!')
    elif jogador == 1:
        print('JOGADOR VENCE!')
    elif jogador == 2:
        print('COMPUTADOR VENCE!')
    else:
        print('Jogada inválida! Você perdeu!')
elif computador == 1: #Computador jogou Papel
    if jogador == 0:
        print('COMPUTADOR VENCE!')
    elif jogador == 1:
        print('EMPATE!')
    elif jogador == 2:
        print('JOGADOR VENCE!')
    else:
        print('Jogada inválida! Você perdeu!')
elif computador == 2: #Computador jogou Tesoura
    if jogador == 0:
        print('JOGADOR VENCE!')
    elif jogador == 1:
        print('COMPUTADOR VENCE!')
    elif jogador == 2:
        print('EMPATE!')
    else:
        print('Jogada inválida! Você perdeu!')
#– O primeiro valor é maior – O segundo valor é maior – Não existe valor maior, os dois são iguais


