#Crie um programa que tenha a função leiaInt(), que vai funcionar de forma semelhante ‘a função input() do Python, só que fazendo a validação para aceitar apenas um 
# valor numérico. Ex: n = leiaInt(‘Digite um n: ‘)


# PRIMEIRA OPÇÃO
# def leiaInt(msg):
#     while True:
#         n = input(msg)
#         if n.isnumeric():
#             return int(n)
#         else:
#             print("\033[0;31mDigite novamente. Apenas números são aceitos!\033[m")


# numero = leiaInt("Digite um número: ")
# print(f"Você digitou o número {numero}.")


def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = str(input(msg))
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print("\033[0;31mDigite novamente. Apenas números são aceitos!\033[m")
        if ok:
            break
    return valor
    

n = leiaInt("Digite um número: ")
print(f"Você digitou o número {n}.")
