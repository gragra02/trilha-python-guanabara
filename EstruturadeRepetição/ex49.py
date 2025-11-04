#Refaça o DESAFIO 009, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.
num = int(input('Digite uma número para ver a tabuada:  '))
for n in range (1, 11):
    print (f'{num:2d} x {n:2d} = {num*n:2d}')

