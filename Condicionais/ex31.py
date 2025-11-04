#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da
# passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 
# parta viagens mais longas.

distancia = float(input('Qual a distância da viagem em Km? '))
if distancia <=200:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print(f' A sua viagem terá {distancia:.2f}Km preço da passagem é R$ {preço:.2f}R$')