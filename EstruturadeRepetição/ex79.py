#Crie um programa onde o usuário possa digitar vários valores numéricos e cadastre-os em uma lista. 
#Caso o número já exista lá dentro, ele não será adicionado. 
#No final, serão exibidos todos os valores únicos digitados, em ordem crescente.
valores = []
while True:
    v = int(input('Digite um valor: '))
    valores.append(v)
    print('Valor adicionado com sucesso...')
    r = ''
    while r not in 'SN':
        r = input('Quer continuar? [S/N] ').upper().strip()[0]
    if r == 'N':
        break
print (sorted(valores))
