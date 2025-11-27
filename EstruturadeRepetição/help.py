# ==AULAS DE HELP==
# def contador (i, f, p):
#     """
#     -> Faz uma contagem e mostra na tela.
#     :param i: início da contagem
#     :param f: fim da contagem
#     :param p: passo da contagem
#     :return: sem retorno
#     """
#     c = i
#     while c <= f:
#         print(f'{c} ', end='')
#         c += p
#     print('FIM!')

# contador(1, 10, 1)

# help(contador)

#== PARAMETROS OPÇONAIS ==
# def somar(a=0, b=0, c=0):
#     s = a + b + c
#     print(f'A soma é {s}')

# somar(5, 2, 6)
# somar(5, 9)
# somar(b=4, c=1)

# #== ESCOPO DE VARIÁVEIS ==
# def teste():
#     x = 8
#     print(f" Nessa função a variável n vale {n}") #Escopo global
#     print(f'Nessa função a variável x vale {x}')# Escopo local


# #Programa principal
# n = 2
# print(f'No programa principal a variável n vale {n}')
# teste()

# def função():
#     n1 = 8
#     print(f'N1 dentro vale {n1}') 

# n1 = 5
# print(f'Fora o n1 vale {n1}')
# função()  # <- CHAMA A FUNÇÃO AQUI

# == USANDO O RETURN ==
# def somar(a=0, b=0, c=0):
#     s = a + b + c
#     return s

# r1 = somar(3, 2, 5)
# r2 = somar(2, 2)
# r3 = somar(1)
# print(f'A soma dos valores valem {r1}, {r2} e {r3}')

def par(n=0):
    if n % 2 == 0:
        return True
    else:
        return False
    
num = int(input(('Digite um número: ')))
if par(num):
    print('É par')
else:
    print('É ímpar')