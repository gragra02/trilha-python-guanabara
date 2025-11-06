#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10. 
# Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final quantos palpites foram necessários para vencer.
import random
from time import sleep
cont = 0
print('Vou pensar em um número entre 0 e 10. Tente adivinhar! ')
numero_pc = random.randint(0 , 10)
acertou = False
while not acertou:
    numero_usuario = int(input('Em que número eu pensei? '))
    cont += 1
    print('Estou pensando...')
    sleep(3)
    if numero_usuario < numero_pc:
        print('Errou, é mais. ')
    elif numero_usuario > numero_pc:
        print('É menos')
    else:
        acertou = True
        print(f'Parabéns voc acertou! Eu pensei no número \033[33m{numero_pc}\033[m e você \033[32m{cont}\033[m tentativas')