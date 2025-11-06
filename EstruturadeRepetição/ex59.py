#Crie um programa que leia dois valores e mostre um opcao na tela
from time import sleep

print('=======CALCULADORA========')
n1 = int(input('Digite o um número: '))
print('=-'*15)
n2 = int(input('Digite outro número: '))
print('=-'*15)
opcao = 0
while opcao != 5:
    print (
    '[1] Somar\n'
    '[2] Multiplicar \n'
    '[3] Maior \n'
    '[4] Novos número\n' 
    '[5] Sair do programa \n' )
    opcao = int(input('Digite uma opção: '))
    print('=-'*15)
    if opcao == 1:
        soma = n1 + n2
        print(f'Soma  {n1} + {n2} = {soma}')
    elif opcao == 2:
        mult = n1 * n2
        print(f'A muntiplicação de {n1} X {n2} = {mult}')
    elif opcao == 3:
        if n1 > n2:
            print(f'O número maior é {n1}')
        else:
            print(f'O número maior é {n2}')
    elif opcao == 4:
        n1 = int(input('Primeiro número: '))
        n2 = int(input('Segundo número: '))
    elif opcao == 5:
        print('Finalizar...')
    else:
        print('Opção invalida, Digite novamente')
    sleep(2)    
    print('=-'*15)
print('Programa finalizado')
