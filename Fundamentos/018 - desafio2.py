#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno,
#  cosseno e tangente desse ângulo.

#import math
#angulo = float(input('Digite o ângulo que você deseja: '))
#seno = math.sin(math.radians(angulo))
#print(f'O ângulo de {angulo} tem o SENO de {seno:.2}')
#cosseno = math.cos(math.radians(angulo))
#print(f'O angulo de {angulo} tem o COSSENO de {cosseno:.2}')
#tangente = math.tan(math.radians(angulo))
#print(f'O angulo de {angulo} tem a TANGENTE de {tangente:.2}')

from math import radians, sin, cos, tan
angulo = float(input('Digite o ângulo que você deseja:'))
seno = sin(radians(angulo))
print(f'O ângulo de {angulo} tem o SENO de {seno:.2f}')
cosseno = cos(radians(angulo))
print(f'O angulo de {angulo} tem o COSSENO de {cosseno:.2f}')
tangente = tan(radians(angulo))
print(f'O angulo de {angulo} te a TANGENTE de {tangente:.2f}')
