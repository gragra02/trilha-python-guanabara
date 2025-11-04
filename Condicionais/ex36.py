#Escreva um programa para aprovar o empréstimo bancário para a compra de uma casa.
#O programa vai perguntar o valor da casa, o salário do comprador e em quantos anos ele vai pagar.
#Calcule o valor da prestação mensal, sabendo que ela não pode exceder 30% do salário ou então o 
# empréstimo será negado.

valor_casa = float(input('Qual o valor da casa que você deseja comprar? R$ '))
salario = float(input('Qual o seu salário? R$ '))
anos = int(input('Em quantos anos você pretende pagar a casa?'))
prestação = valor_casa / (anos * 12)
porcentagem = salario * 0.30
if prestação <= porcentagem:
    print(f'Emprestimo aprovado! Sua prestação mensal será de R$ {prestação:.2f} durante {anos} anos.')
else:
    print(f'Emprestimo negado! Sua pretação mensal de R$ {prestação:.2f} e execde 30% do seu salário.')
