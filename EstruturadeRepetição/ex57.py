#Faça um programa que leia o sexo de uma pessoa, mas só aceite os valores ‘M’ ou ‘F’.
# Caso esteja errado, peça a digitação novamente até ter um valor correto.
# sexo = ''
# while sexo != 'F':
#     sexo = str(input('Digite o sexo [M/F]: ')).upper()
# print('Acabou')


sexo = (input('Digite o sexo [F/M]: ')).upper().strip()[0]
while sexo not in 'MmFf':
    sexo = input('Dados invalido! Digite novamente: ').upper().strip()[0]
print(f'Sexo {sexo} registado com sucesso')
