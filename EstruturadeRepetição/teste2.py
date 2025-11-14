valores = []
while True:
    v = int(input('Digite um valor: '))
    valores.append(v)
    print('Valor adicionado com sucesso...')
    r = ''
    while r not in 'SN':
        r = input('Quer continuar? [S/N] ').upper().strip()[0]
    if r == 'N':
        break
print (sorted(valores))
