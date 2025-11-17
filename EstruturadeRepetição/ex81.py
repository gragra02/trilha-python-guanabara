#Crie um programa que vai ler vários números e colocar em uma lista.
#Depois disso, mostre:
# A) Quantos números foram digitados. 
# B) A lista de valores, ordenada de forma decrescente. 
# C) Se o valor 5 foi digitado e está ou não na lista.
lista = list()
while True:
    v = int(input('Digite um valor: '))
    r = (input('Quer continuar? [S/N] ')).upper().strip()[0]
    lista.append(v)
    if r == 'N':
        break
print(f'Você digitou {len(lista)} números.')
print(f'A lista em ordem decrescente é {sorted(lista, reverse=True)}')
if 5 in lista:
    print('O valor 5 esta na lista')
else:
    print('O valor 5 não está na lista')