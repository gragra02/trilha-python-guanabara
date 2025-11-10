#Jogo par ou impar
from random import randint

vitoria = 0
print("-" * 30)
while True:
    jogador = int(input("Digite um númeoro: "))
    print("-" * 30)
    computador = randint(0, 10)
    tot = computador + jogador
    tipo = " "
    while tipo not in "PI":
        tipo = str(input("Par ou Impar? [P/I] ")).upper().strip()[0]
    print(f"Você jogou {jogador} e o computador {computador}. Total de {tot} ", end="")
    print("DEU PAR" if tot % 2 == 0 else "DEU IMPAR")
    if tipo == "P":
        if tot % 2 == 0:
            print("Você venceu! É PAR ")
            print("-" * 30)
            vitoria += 1
        else:
            print("Você perdeu! É IMPAR ")
            print("-" * 30)
            break
    elif tipo == "I":
        if tot % 2 == 1:
            print("Você venceu! É IMPAR ")
            print("-" * 30)
            vitoria += 1
        else:
            print("Você perdeu! É PAR ")
            print("-" * 30)
            break  
    print("Vamos jogar novamente...")
print("-" * 30)       
print (f"FIM DE JOGO!!Você ganhou {vitoria} vezes!")
