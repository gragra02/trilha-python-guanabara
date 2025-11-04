# Crie um programa que leia uma frase qualquer e diga se ela é um palíndromo, desconsiderando os espaços.

frase = str(input('Digite uam frese: ')).strip().upper()
palavra = frase.split()
juntar = ''.join(palavra)
inverso = ''
for letra in range(len(juntar) -1, -1, -1):
    inverso += juntar[letra]
if inverso == juntar:
    print(f'Sua frase foi "{inverso}" e e yemos um palimndromo')
else:
    print('Não é um palindro')