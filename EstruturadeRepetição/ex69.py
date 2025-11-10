#Crie um programa que leia a idade e o sexo de várias pessoas. 
#A cada pessoa cadastrada, o programa deverá perguntar se o usuário quer ou não continuar. No final, 
print("-=" * 30)
print("CADASTRE UMA PESSOA")
print("-=" * 30)
tot18 = totH = totM20 =  0
while True:
    idade = int(input("Idade: "))
    sexo = " "
    while sexo not in "MF":
        sexo = str(input("Sexo [M/F]: ")).upper().strip()[0]
    if idade >= 18:
        tot18 += 1
    if sexo == "M":
        totH += 1
    if sexo == "F" and idade < 20:
        totM20 += 1
    resp = " "
    while resp not in "SN":
        resp = str(input("Quer continuar? [S/N]: ")).upper().strip()[0]
    print("-=" * 30)
    if resp == "N":
        break
print(f"Total de pessoas com mais de 18 anos: {tot18}")
print(f"O total de homens: {totH} ")
print(f"O total de mulheres com menos de 20 anos: {totM20}")

