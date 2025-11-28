#Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

def aumentar(preço=0, taxa=0):
    return preço + (preço * taxa / 100)


def dobro(preço=0):
    return preço * 2

def metade(preço=0):
    return preço / 2

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')