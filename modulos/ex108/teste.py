#Adapte o código do desafio #107, criando uma função adicional chamada moeda() que consiga mostrar os números como um valor monetário formatado.

import moeda

p = float(input('Digite o preço: R$ '))

print('-' * 50)
print(f' A metadde de {moeda.moeda(p)} é {moeda.moeda(moeda.metade(p))}')
print('-' * 50)
print(f' O dobro de {moeda.moeda(p)} é {moeda.moeda(moeda.dobro(p))}')
print('-' * 50)
print(f' Aumentando 10% de {moeda.moeda(p)} temos {moeda.moeda(moeda.aumentar(p, 10))}')
print('-' * 50)