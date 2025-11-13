#lanche = ('Hamburguer', 'Suco', 'Pizza', 'Pudim', 'Batata Frita')

#print(lanche[:4])

# for cont in range(0, len(lanche)):
#     print(f"Eu vou comer {lanche[cont]} na posição {cont}")

# for comida in lanche:
#     print(f"Eu vou comer {comida}")

#for pos, comida in enumerate(lanche):
    # print(sorted(lanche))  # Ordena a tupla em ordem alfabética sem alterar a tupla original

# a = (2, 5, 4)
# b = (5, 8, 1, 2)
# c = b + a
# print(c)
# print(sorted(c))  # Ordena a tupla resultante em ordem crescente
# print(c.count(5))  # Conta quantas vezes o valor 5 aparece na tupla c
#print(lanche.index('Pizza', 1))  # Retorna a posição do valor 'Pizza' na tupla


#Listas#

# num = [2, 5, 9, 1] #Lista
# print(num) 
# num[2] = 3 #Alterando o valor da posição 
# print(num)
# num.append(7) #Adicionando um valor no final da lista
# print(num)
# num.sort(reverse=True) #Organizando a lista em ordem decrescente
# print(num)
# num.insert(2, 2) #Inserindo o valor 0 na posição 2
# print(num)
# num.remove(2) #Removendo o valor 2 da lista
# if 4 in num:
#     num.remove(4)
# else:
#     print("O valor 4 não foi encontrado na lista.")
# print(num)
# num.pop() #Removendo o último elemento da lista
# print(num)
# print(f"Essa lista tem {len(num)} elementos. " ) #Mostrando a quantidade de elementos da lista

valores = []
# valores.append(5)
# valores.append(9)
# valores.append(4)
# print(valores)
for cont in range(0, 5):
    valores.append(int(input("Digite um valor: ")))
# for v in valores:
#     print(f'{v}...', end=' ') # formata os números bonitinhos
# print('Fim')
for c, v in enumerate(valores):
    print(f'Na posição {c} está o valor {v}')
print('Cheguei ao final da lista.')

a = [1, 2, 3,  5,]
b = a
print(f'b = {b}')
print(f'a = {a}')
b = a[:]
b.append(4)
print(f'b = {b}')
print(f'a = {a}')