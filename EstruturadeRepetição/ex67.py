#Faça um programa que mostre a tabuada de vários números, um de cada vez, para cada valor digitado pelo usuário.
#O programa será interrompido quando o número solicitado for negativo.

while True:
    print("=-" * 30)
    num = int(input("Digite um númeoro para ver sua tabuada: "))
    print("=-" * 30)
    if num < 0:
        break
    for n in range(1, 11):
        print(f"{num} x {n:2} = {num*n}")
    print("=-" * 30)
    print(f"TABUADA DE {num} completada")
print("PROGRAMA TABUADA FINALIZADO")
print("=-" * 30)
    