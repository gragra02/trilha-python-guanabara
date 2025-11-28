import uteis

n1 = float(input('Digite o primeiro número: '))
n2 = float(input('Digite o segundo número: '))
m = uteis.media(n1, n2)
print(f'A média entre {n1} e {n2} é {m}')

r = int(input('Digite um número para calcular a raiz quadrada: '))
raiz = uteis.raiz(r)
print(f'A raiz quadrada de {r} é {raiz}')