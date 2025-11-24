#Crie um programa que leia nome, sexo e idade de várias pessoas, guardando os dados de cada pessoa em um dicionário e todos os dicionários em uma lista. No final, mostre:
#  A) Quantas pessoas foram cadastradas 
# B) A média de idade C
# ) Uma lista com as mulheres 
# D) Uma lista de pessoas com idade acima da média
pessoas = dict()
galera = []
mulheres = []
galeraidade = []
idademais = []
while True:
    pessoas['nome'] = str(input('Nome: '))
    while True:
        pessoas['sexo'] = str(input('Sexo: ')).upper().strip()
        if pessoas['sexo'] in 'MF':
            break
        print('Erro! Por favor, digite apenas M ou F.')
    pessoas['idade'] = int(input('Idade: '))
    galera.append(pessoas.copy())
    mulheres.append(pessoas['nome'])
    galeraidade.append(pessoas['idade'])
    media = sum(galeraidade)/len(galeraidade)
    while True:
        resp = str(input("Quer continuar? [S/N] ")).upper().strip()
        if resp in 'SN':
            break
        print('Erro! Por favor, digite apenas S ou N.')

    if resp == 'N':
        break
print('=' * 30)        
print(f'A) Foram cadastradas {len(galera)} pessoas')
print(f'B) A media de {media:.2f} anos')
print(f'C) Pessoas com idade acima da média são:', end=' ')
for p in galera:
    if p['idade'] >= media:
        print(f'{p["nome"]} ', end='')
print()       
print(f'D) Os nomes das mulheres cadastradas foram: ')
for p in galera:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()
