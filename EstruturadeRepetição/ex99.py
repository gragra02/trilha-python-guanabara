# Faça um programa que tenha uma função chamada maior(), que receba vários parâmetros com valores inteiros. Seu programa tem que analisar
# todos os valores e dizer qual deles é o maior.

#==SOLUÇÃO 1==
# def maior (*valores):
#     print('Analisando valores...')
#     print(f'Foram informado {len(valores)} valores.')
#     print(f'O maior valor informado foi {max(valores)}')
#     print('=' * 30)

# maior(2, 9, 4, 5, 7, 1)
# maior(1, 2)
# maior(6, 3, 8, 5)
# maior()
# maior(6, 9, 12)

#==SOLUÇÃO 2==

def maior(*valores):
    cont = maior = 0
    print('=' * 30)
    print('Analisando valores...')
    for valor in valores:
        print(f'{valor} ', end='')
        if cont == 0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        cont += 1
    print(f'Foram informados {cont} valores ao todo.')
    print(f'O maior valo informado foi {maior}')

maior(2, 9, 4, 5, 7, 1)
maior(1, 2)
maior(6, 3, 8, 5)
maior()
maior(6, 9, 12)
