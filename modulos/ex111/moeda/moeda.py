# Adicione o módulo moeda.py criado nos desafios anteriores, uma função chamada resumo(), que mostre na tela algumas informações geradas pelas funções
#  que já temos no módulo criado até aqui.

def aumentar(preço=0, taxa=0):
    return preço + (preço * taxa / 100)
'''
->Calcula o aumento de um preço, retornando o resultado com ou sem formatação.
    

'''


def dobro(preço=0):
    return preço * 2

def metade(preço=0):
    return preço / 2

def moeda(preço=0, moeda='R$'):
    return f'{moeda}{preço:>.2f}'.replace('.', ',')


def diminuir(preço=0, taxa=0):
    return preço - (preço * taxa / 100)

def resumo(preço=0, taxa_aumento=20, texa_reducao=12):
    print('-' *40)
    print('RESUMO DO VALOR'.center(40))
    print('-' *40)
    print(f'Preço analisado: \t{moeda(preço)}')
    print(f'Dobro do preço: \t{moeda(dobro(preço))}')
    print(f'Metado do preço: \t{moeda(metade(preço))}')
    print(f'{taxa_aumento}% de aumento: \t{moeda(aumentar(preço, taxa_aumento))}')
    print(f'{texa_reducao}% de redução: \t{moeda(diminuir(preço, texa_reducao))}')
    print('-' *40)