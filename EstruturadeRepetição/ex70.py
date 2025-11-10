#Exercício Python 070: Crie um programa que leia o nome e o preço de vários produtos. O programa deverá perguntar se o usuário vai continuar ou não. No final, mostre:
#A) qual é o total gasto na compra.
#B) quantos produtos custam mais de R$1000.
#C) qual é o nome do produto mais barato. 

print('{:-^40}'.format ( "LOJA DA GRAZI"))
pMenor = tot = promais = promenor = cont = 0
barato = " "
while True:
    prod = str(input("Nome do Produto: ")) 
    preco = float(input("Preço: R$ " ))
    cont += 1
    tot += preco
    if preco > 1000:
        promais += 1
    if cont == 1 or preco < promenor:
        promenor = preco
        barato = prod
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N]  ")).upper().strip()[0]
        print("-=" * 30)
    if resp == "N":
        break
print(f"O preço total da compra foi R${tot:.2f}")
print(f"Temos {promais} produtos que custam mais de R$1000.00")
print(f"O produto mais barato foi {prod} que custa R${promenor:.2f}")