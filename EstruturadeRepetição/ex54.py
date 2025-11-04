# Crie um programa que leia o ano de nascimento de sete pessoas.
# No final, mostre quantas pessoas ainda não atingiram a maioridade e quantas já são maiores.

from datetime import date
data_atual = date.today().year
totmaior = 0
totmenor = 0
for m in range(1, 8):
    anonas = int(input('Digite o ano de nascimento: '))
    idade = data_atual - anonas
    if idade >= 18:
        totmaior += 1
    else:
        totmenor += 1
        
print(f'Tem  {totmaior} pessoar de maior')
print(f'Tem {totmenor} pessoas de menor')