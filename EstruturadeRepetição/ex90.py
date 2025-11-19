#Crie um programa que leia nome e duas notas de vários alunos e guarde tudo em uma lista composta. 
# No final, mostre um boletim contendo a média de cada um e permita que o usuário possa mostrar as notas de cada aluno individualmente.
ficha = []
dados = []
cont = 0
while True:
    nome = str(input('Nome:  '))
    n1 = float(input('Nota 1: '))
    n2 = float(input('Nota 2: '))
    media = (n1 + n2) / 2
    ficha.append([nome, [n1, n2], media])
    cont += 1
    resp = str(input('Quer continuar [S/N]? ')).upper().strip()[0]
    if resp == 'N':
        break
    dados.clear()
print('-=' * 30)
print(f'{"Nº":<4}{"NOME":<10}{"MÉDIA":>8} ')
print('-=' * 30)
for i, a in enumerate(ficha):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8}')
while True:
    print('-' * 30)
    opc = int(input('Mostrar notas de qual aluno? (999 para sair:  '))
    if opc == 999:
        break
    if opc <= len(ficha) - 1:
        print(f'Notas de {ficha[opc][0]} são {ficha[opc][1]}')
print('<<< VOLTE SEMPRE>>>')