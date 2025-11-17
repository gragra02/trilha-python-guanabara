#  Crie um programa que vai ler vários números e colocar em uma lista.
#  Depois disso, crie duas listas extras que vão conter apenas os valores pares e os valores ímpares digitados, respectivamente.
#  Ao final, mostre o conteúdo das três listas geradas.
lista = list()
pares = list()
impares = list()

while True:
    v = int(input('Digite um valor: '))
    lista.append(v)
    r = input('Quer continuar [S/N]: ').upper().strip()[0]
    if v % 2 == 0:
        pares.append(v)
    else:
        impares.append(v)
    if r == 'N':
        break
print('=' * 30)
print(f'Lista completa: {lista}')
print(f'Lista de pares: {pares}')
print(f'Lista de ímpares: {impares}')

