# Crie um programa que leia o nome completo de uma pessoa e mostre:
# - O nome com todas as letras maiúsculas e minúsculas.
# - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços).
# - Quantas letras tem o primeiro nome.

frase = (input('Digite seu nome completo: '))
print(frase.upper())
print(frase.lower())
print(len(frase) - frase.count(' '))
separa = frase.split()
print(len(separa[0]))

