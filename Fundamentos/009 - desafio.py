num = float(input('Digite um valor para ser convertido em dolar:  '))
cot = float(input('Digite a cotação do dolar hoje:  '))
conv = num / cot 
print(f'Com R${num} você pode comprar U${conv:.2f} dólares hoje.')   