#Faça um programa que leia nome e peso de várias pessoas, guardando tudo em uma lista. No final, mostre:
# A) Quantas pessoas foram cadastradas.  
# B) Uma listagem com as pessoas mais pesadas. 
# C) Uma listagem com as pessoas mais leves.
pessoa = []
dados = []
while True:
    dados.append(str(input('Nome: ')))
    dados.append(float(input('Peso: ')))
    pessoa.append(dados[:])
    dados.clear()
    resposta = str(input('Quer continuar? [S/N]: ')).upper().strip()[0]
    if resposta == 'N':
        break
maispeso = menospeso = pessoa[0][1]
for p in pessoa:
    if p[1] > maispeso:
        maispeso = p[1]
    if p[1] < menospeso:
        menospeso = p[1]
print (f'A quantidade de pessoa é {len(pessoa)}')
print(f'O maior peso foi {maispeso} ')
print(f'O menor peso foi {menospeso}')