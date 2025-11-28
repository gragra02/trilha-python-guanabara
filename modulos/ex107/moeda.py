#Crie um módulo chamado moeda.py que tenha as funções incorporadas aumentar(), diminuir(), dobro() e metade(). 
# Faça também um programa que importe esse módulo e use algumas dessas funções.

def aumentar(preço=0, taxa=0):
    return preço + (preço * taxa / 100)


def dobro(preço=0):
    return preço * 2

def metade(preço=0):
    return preço / 2