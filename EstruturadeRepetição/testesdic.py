# pessoas = {'nome': 'Graziele', 'idade': 22, 'sexo': 'F'}
# print(pessoas['nome'])
# print(f'O nome é {pessoas['nome']} e a idade é {pessoas['idade']}')
# print(pessoas.keys()) #mostra as chaves
# print(pessoas.values())#mostra os valores
# print(pessoas.items()) #mostra os dois
# pessoas['nome'] = "Maria" #alterando valor
# pessoas['peso'] = 65.5 #adicionando novo valor
# del pessoas['sexo']
# for k, v in pessoas.items():
#     print(k, '=', v)

# brasil = []
# estado1 = {'uf': 'Santa Catarina', 'sigla': 'SC'}
# estado2 = {'uf': 'Pernambuco', 'sigla': 'PE'}
# brasil.append(estado1)#adiciona o dicionario estado1 na lista brasil
# brasil.append(estado2)#adiciona o dicionario estado2 na lista brasil
# print(brasil)
# print(brasil[0]['sigla'])#acessa o primeiro elemento da lista brasil e pega o valor da chave sigla
# print(brasil[1]['uf'])#acessa o segundo elemento da lista brasil e pega o valor da chave uf
# for e in brasil:
#     for k, v in e.items():
#         print(f'O campo {k} tem valor {v}')

estado = dict()
brasil = list()
for c in range(0, 2):
    estado['uf'] = str(input('UF: '))
    estado['sigla'] = str(input('Sigla: '))
    brasil.append(estado.copy()) #faz cópia da lista
for e in brasil:
    for v in e.values():
        print(v, end=' ')
    print()


