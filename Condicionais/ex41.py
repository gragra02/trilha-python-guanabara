#A Confederação Nacional de Natação precisa de um programa que leia o ano de nascimento de um atleta e mostre sua categoria, de acordo com a idade:
#– Até 9 anos: MIRIM – Até 14 anos: INFANTIL – Até 19 anos: JUNIOR – Até 20 anos: SÊNIOR – Acima: MASTER
from datetime import date
nascimento = int(input('Data de nascimento do atleta:'))
data_atual = date.today().year
idade = data_atual - nascimento
if idade <= 9:
    print(f'O atleta é da cateria MIRIM com idade de {idade} anos')
elif idade <= 14:
    print(f'O atleta é da categoria INFANTIL com idade de {idade} anos')
elif idade <= 19:
    print(f'O atleta é da categoria JUNIOR com idade de {idade} anos')
elif idade <= 20:
    print(f'O atleta é da categoria SÊNIOR com idade de {idade} anos')
else:
    print(f'O atleta é da categoria MASTER com idade de {idade} anos')
