# Aprimore o desafio anterior, mostrando no final:     
# A) A soma de todos os valores pares digitados.         
# B) A soma dos valores da terceira coluna.
# C) O maior valor da segunda linha.        

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
soma_pares = 0
somater = 0
maiors = 0
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))
print('=-' * 30)
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
        if matriz[l][c] % 2 == 0:
            soma_pares += matriz[l][c]
        if c == 2:
            somater += matriz[l][c]
    print()
    if l == 1:
        for c in range(0, 3):
            if c == 0 or matriz[l][c] > maiors:
                maiors = matriz[l][c]
    print()
    print('=-' * 30)
print(f'A soma de todos os valores pares é {soma_pares}.')
print(f'A soma dos valores da terceira coluna é {somater}.')
print(f'O maior valor da segunda linha é {maiors}.')
print('=-' * 30)

  
