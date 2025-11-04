#O mesmo professor do desafio 19 quer sortear a ordem de apresentação de trabalhos dos alunos.
# Faça um programa que leia o nome dos quatro alunos e mostre a ordem sorteada.
#import random
from random import shuffle
n1 = (input('Digite o nome do primeiro aluno: '))
n2 = (input('Digite o nome do segundo aluno: '))
n3 = (input('Digite o nome do terceeiro aluno: '))
n4 = (input('Digite o nome do quarto aluno: '))
nomes = [n1, n2, n3, n4]
#lista = random.shuffle(nomes)
lista = shuffle(nomes)
print('A ordem de apresentação será:')
print(nomes)
