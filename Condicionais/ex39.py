#Faça um programa que leia o ano de nascimento de um jovem e informe, de acordo com sua idade:
#– Se ele ainda vai se alistar ao serviço militar. – Se é a hora de se alistar. – Se já passou do tempo do alistamento.
#Seu programa também deverá mostrar o tempo que falta ou que passou do prazo.

from datetime import date
ano_nascimento = int(input('Digite o ano do seu nascimento: '))
ano_atual = date.today().year
idade = ano_atual - ano_nascimento
if idade < 18:
    saldo = 18 - idade
    ano_alistamento = ano_atual + saldo
    print(f'Você tem {idade} anos. Ainda faltam {saldo} anos para o alistamento militar. Seu alistamento será em {ano_alistamento}.')
elif idade == 18:
    print(f'Você tem {idade} anos. Está na hora de se alistar ao serviço militar!  ')
else:
    saldo = idade - 18
    ano_alistamento = ano_atual - saldo
    print(f'Você tem {idade} anos. Já passou {saldo} anos do prazo de alistamento militar. Seu alistamento foi em {ano_alistamento}.')