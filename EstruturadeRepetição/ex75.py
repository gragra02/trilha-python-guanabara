#: Desenvolva um programa que leia quatro valores pelo teclado e guarde-os em uma tupla. No final, mostre:
#A) Quantas vezes apareceu o valor 9.
#B) Em que posição foi digitado o primeiro valor 3.
#C) Quais foram os números pares.
num = ((int(input("Digite um número: "))), int((input("Digite outro número: "))), int(input("Digite outro número: ")), int(input("Digite mais um número: ")))
print(f'Os números digitados foram: {num}')
print(f'O numero 9 apareceu {num.count(9)} vezes' )
if 3 in num:
    print(f'O numero 3 apareceu na posição {num.index(3) + 1}º posição' )
else:
    print('O numero 3 não foi digitado: ')
print('Os números pares digitados foram: ', end='')
for n in num:
    if n % 2 == 0:
        print(n, end=' ')
