# Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores
# e qual foi o maior e o menor valores lidos. O programa deve perguntar ao usuário se ele quer ou não continuar a digitar valores.
print("=-" * 30)
soma = cont = 0
resp = "S"
while resp == "S":
    num = int(input("Digite um valor: "))
    cont += 1
    soma += num
    media = soma / cont
    if cont == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
            
    resp = str(input("Quer continuar? [S/N]")).strip().upper()
print(f"Você digitou {cont} a soma é {soma} e a média é {media :.2f} o maior valor é {maior} e o menor valor é {menor}")
