#Desenvolva um programa que leia o primeiro termo e a razão de uma PA.
#No final, mostre os 10 primeiros termos dessa progressão.

primeiro = int(input('Primeiro termo: '))
razão = int(input('Digite a razão: '))
decimo = primeiro + (10 - 1)* razão
for c in range(primeiro, decimo + 1, razão):
    print(c, end=' -> ')
print('Acabou')
