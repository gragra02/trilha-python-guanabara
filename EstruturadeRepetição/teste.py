nome = input('Digite o nome que tenha a letra A: ')
while 'A' not in nome.upper():
    nome = input('Dados inválidos! Digite novamente: ')
print(f'O nome {nome} foi registrado com sucesso!')
