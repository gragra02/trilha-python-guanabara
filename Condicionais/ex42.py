#💡 Refaça o DESAFIO 035 dos triângulos, acrescentando o recurso de mostrar que tipo de triângulo 
# será formado:
#– Equilátero: todos os lados iguais – Isósceles: dois lados iguais – Escaleno: todos os lados diferentes7

r1 = float(input('Digite o comprimento da primeira reta: '))
r2 = float(input('Digite o comprimento da segunda reta: '))
r3 = float(input('Digite o comprimento da terceira reta: '))
if r1 < r2 + r3 and r2 < r1 + r3 and r3 < r1 + r2:
    print('As retas podem formar um triângulo.')
    if r1 == r2 == r3:
        print('O triângulo é Equilátero.')
    elif r1 == r2 or r1 == r3 or r2 == r3:
        print('O triângulo é Isósceles.')
else:
    print('\033[1;31;43mAs retas não podem formar um triângulo\033[m')