#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas. 
# No final do programa, mostre: a média de idade do grupo, 
# qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos

soma = 0
mediaidade = 0
maioridadehomem = 0
nomehomemvelho = ''
totmulher20 = 0
for pess in range(1,5):
    print(f'='*5 , pess, 'º PESSOA', '='*5) 
    nome = str(input('Insira o nome: '))
    idade = int(input('Insira a idade: '))
    sexo = (input('Sexo [M/F]: ')).strip()
    soma += idade
    if pess == 1 and sexo in'Mm':
        maioridadehomem = idade
        nomehomemvelho = nome
    if sexo in 'Mm' and idade > maioridadehomem:
        maioridadehomem = idade
        nomehomemvelho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1
media = soma/4
print('='*10)    
print(f'A média da idade é {media}')
print(f'O homem mais velho tem {maioridadehomem} e se chama {nomehomemvelho}')
print(f'Ao total são {totmulher20} mulheres com menos de 20 anos')

    