preço = float(input('Digite o preço do produto R$ '))
novo_preço = preço - (preço*5/100)
print(f'O preço do produto com desconto de 5% é de R$ {novo_preço:.2f}')