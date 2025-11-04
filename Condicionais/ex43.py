#💡 Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu IMC e mostre seu status, 
# de acordo com a tabela abaixo:
#– Abaixo de 18.5: Abaixo do Peso – Entre 18.5 e 25: Peso ideal – 25 até 30: Sobrepeso – 30 até 40: Obesidade – Acima de 40: Obesidade mórbida

peso = float(input("Digite seu peso em kg: "))
altura = float(input("Digite sua altuma em metros: "))
IMC = peso / (altura ** 2)
print(f"Sei IMC é : {IMC :.2f}")
if IMC < 18.5:
    print("Status: Abaixo do Peso")
elif 18.5 <= IMC < 25:
    print("Status: Peso ideal")
elif 25 <= IMC < 30:
    print("Status: Sobrepeso")
elif 30 <= IMC < 40:
    print("Status: Obesidade")
else:
    print("Status: Obesidade mórbida")
