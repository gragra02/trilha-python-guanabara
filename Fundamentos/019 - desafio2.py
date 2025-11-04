#Um professor quer sortear um dos seus quatro alunos para apagar o quadro. 
# Faça um programa que ajude ele, lendo o nome dos alunos e escrevendo na tela o nome do escolhido.
#import random

from random import choice
n1 = str(input('Digite o nome do primeiro aluno: '))
n2 = (input('Digite o nome do seguundo aluno: '))
n3 = (input ('Digite o nome do terceiro aluno: '))
n4 = (input ('Digite o nome do quarto aluno: '))
lista = [n1, n2, n3, n4]
#escolhido = random.choice(lista)
#print(f'O aluno escolhido foi {escolhido}')
print(f'O aluno escolhido foi {choice(lista)}')
