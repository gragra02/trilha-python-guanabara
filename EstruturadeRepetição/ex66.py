#Crie um programa que leia números inteiros pelo teclado. O programa só vai parar quando o usuário digitar o valor 999, que é a condição de parada.
#No final, mostre quantos números foram digitados e qual foi a soma entre elas (desconsiderando o flag).

print("=-" * 30)
soma = cont = 0
while True:
    num = int(input("Digite um valor: (999 para parar) "))
    if num == 999:
        break
    soma += num
    cont += 1
    
print("=-" * 30)
print(f"Você digitou {cont} números e a soma entre eles foi {soma}")
print("=-" * 30)