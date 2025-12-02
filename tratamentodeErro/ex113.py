#Reescreva a função leiaInt() que fizemos no desafio 104, incluindo agora a possibilidade da digitação de um número de tipo inválido. 
# Aproveite e crie também uma função leiaFloat() com a mesma funcionalidade.

def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: Por favor, digite novamente um número inteiro válido.\033[m')
            continue
        except( KeyboardInterrupt):
            print('\n\033[0;31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n
        

def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: Por favor, digite novamente um número real válido.\033[m')
            continue
        except(KeyboardInterrupt):
            print('\n\033[0;31mO usuário preferiu não digitar esse número.\033[m')
            return 0
        else:
            return n


num = leiaInt("Digite um número inteiro: ")
numf = leiaFloat("Digite um número real: ")
print(f'O número inteiro digitado foi {num} e o real foi {numf}.')
