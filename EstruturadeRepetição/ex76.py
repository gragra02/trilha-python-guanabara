#Crie um programa que tenha uma tupla única com nomes de produtos e seus respectivos preços,
#na sequência. No final, mostre uma listagem de preços, organizando os dados em forma tabular.
lista = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Caneta', 3.00, 'Estojo', 7.50, 'Transferidor', 5.00, 'Compasso', 9.99, 'Mochila', 120.00, 'Livro', 34.90)
print('-' * 40)
print(f'{"LISTA DE PREÇOS":^40}')
print('-' * 40)
for pos in range(0, len(lista)):
    if pos % 2 == 0:
        print(f"{lista[pos]:.<30}", end=' ' )
    else:
        print(f'R$ {lista[pos]:>7.2f}')
print('-' * 40)
