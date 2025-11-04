#Elabore um programa que calcule o valor a ser pago por um produto, considerando o seu preço normal e a condição de pagamento:
#– à vista dinheiro/cheque: 10% de desconto 
# - à vista no cartão: 5% de desconto 
# – em até 2x no cartão: preço normal 
# – 3x ou mais no cartão: 20% de juros

preço = float(input("Digite o preço do produto: R$ " ))
print('''QUAL A FORMA DE PAGAMENTO?
      
    [1] À vista, dinheiro, cheque 
    [2] À vista no cartão
    [3] 2x no cartão 
    [4] 3x ou mais no cartão''')
opção = int(input("Digite a opção desejada (1/2/3/4): "))
if opção == 1 :
    total = preço - (preço * 10 / 100)
    print(f"O valor a ser pago é R$ {total :.2f} com 10% de desconto.")
elif opção == 2 :
    total = preço - (preço * 5 / 100)
    print(f"O valor a ser pago é R$ {total :.2f} com 5% de desconto.")
elif opção == 3 :
    total = preço
    parcela  = total / 2
    print(f"O valor a ser pago é {total :.2f} em 2x de R$ {parcela :.2f} sem juros")
elif opção <= 4: 
    qt_parcela = int(input("Quantas parcelas você quer pagar: "))
    total = preço + (preço * 20/100)
    parcela = total / qt_parcela
    print(f"O valor a ser pago é {total :.2f} com juros, em {qt_parcela}x de R$ {parcela :.2f}")    
else:
    print('Opção errada de pagamento, tente novamente!')                                  