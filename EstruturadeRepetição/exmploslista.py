# #LISTAS#
# pessoas = [["Pedro", 25], [ "Maria", 30], ["João", 18]]
# print(pessoas[0][1], pessoas[1][1],pessoas[2][1])  # Acessa o primeiro elemento da lista

#CÓPIA DE LISTA#

# teste = list()
# teste.append('Grazi')
# teste.append('45')
# galera = list()
# #galera.append(teste)
# galera.append(teste[:]) #para copia devo usar [:]
# teste [0] = 'Maria'
# teste [1] = '30'
# galera.append(teste[:])
# print(galera)

# galera =  [['João', 18], ['Ana', 20], ['Joaquim', 13], ['Maria', 30]]
# print(galera[1], galera[2][0])
# for p in galera:
#     print(p[0])

galera = list()
dado = list()
totmai = totmen = 0
for c in range(0, 3):
    dado.append(str(input('Nome:')))
    dado.append(int(input('Idade:')))
    galera.append(dado[:])
    dado.clear()

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade.')
        totmai +=1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen +=1
print(f'Temos {totmai} maiores e {totmen} menores de idade.')

        
