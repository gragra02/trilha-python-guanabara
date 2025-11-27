
# # ==FUNÇÃO SEM PARAMETRO==
# def lin(): 
#     print('-=' * 30)

# lin()
# print('CURSO EM VIDEO')
# lin()


# # ==FUNÇÃO COM PARAMETRO==
# def mensagem(msg):
#     print('-=' * 30)
#     print(msg)
#     print('-=' * 30)

# mensagem('CURSO EM VIDEO')
# mensagem('Python é muito boom')

# def soma(a, b):
#     print(f'A = {a} e B = {b}')
#     s = a + b
#     print(f'Soma = {s}')

# soma(4, 5)
# soma(8, 9)
# soma(2, 1)

# # ==FUNÇÃO COM PARAMETRO OPCIONAL==
# def contator(*num):
#     tam = len(num)
#     print(f'Recebi os valores {num} com {tam} números')

# contator(2, 6, 7)
# contator(5, 6, )
# contator(1, 2, 9, 5)
# # == FUNÇÕES COM EMPACOTAMENTO DE LISTA==

# def soma(*valores):
#     s = 0
#     for num in valores:
#         s += num
#     print(f'Somando os valores {valores} temos {s}')

# soma(5, 2)
# soma(2, 9, 4)
# soma(6, 7, 8, 9)

# == FUNÇÕES COM LISTA COMO PARÂMETRO==
def dobra(lts):
    pos = 0
    while pos < len(lts):
        lts[pos] *= 2
        pos += 1
valores = [9, 5, 2 , 0, 3]
dobra(valores)
print(valores)