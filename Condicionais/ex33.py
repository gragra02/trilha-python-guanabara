#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
n1 = int(input('Digite o primeiro número: '))
n2 = int(input('Digite o segundo número: '))
n3 = int(input('Digite o terceiro número: '))

#Vereificar o menor número
menor = n1
if n2 <= n1  and n2 <= n3:
    menor = n1
if n3 <= n1 and n3 <= n2:
    menor = n3

#Verificar o maior número
maior = n1
if n2 >= n1 and n2 >= n3:
    maior = n2
if n3 >= n1 and n3 >= n2:
    maior = n3
print(f'O menor número é: {menor}')
print(f'O maior número é: {maior}')

menor = min(n1, n2, n3)
maior = max(n1, n2, n3)
print(menor)
print(maior)