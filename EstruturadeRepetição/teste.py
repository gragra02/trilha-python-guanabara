# ...existing code...
print("CADASTRE UMA PESSOA")
print("-=" * 30)
maior = 0
menor = 0
masc = 0
femi = 0
while True:
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").upper().strip()
    while sexo == "" or sexo[0] not in ("M", "F"):
        sexo = input("Digite apenas M ou F. Sexo [M/F]: ").upper().strip()
    sexo = sexo[0]

    if idade >= 18:
        maior += 1
    else:
        menor += 1 

    if sexo == "M":
        masc += 1
    else:
        femi += 1

    opção = input("Quer continuar? [S/N]: ").upper().strip()
    while opção == "" or opção[0] not in ("S", "N"):
        opção = input("Digite apenas S ou N. Quer continuar? [S/N]: ").upper().strip()
    if opção[0] == "N":
        break

print(f"Total de pessoas com mais de 18 anos: {maior}")
print(f"O total de homens: {masc}")
print(f"O total de mulheres: {femi}")
# ...existing code...