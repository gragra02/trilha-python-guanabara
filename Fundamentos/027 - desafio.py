#Faça um programa que leia o nome completo de uma pessoa, mostrando
#  em seguida o primeiro e o último nome separadamente.
#Ex: Ana Maria de Souza (primeiro = Ana; último = Souza.
nome = input('Digite seu nome completo: ').strip()  # remove espaços nas extremidades
separa = nome.split()
print(f'Primeiro nome: {separa[0]}')
#print(f'Último nome: {separa[-1]}')
print(f'Último nome: {separa[len(separa) - 1]}')