#Crie uma tupla preenchida com os 20 primeiros colocados da Tabela do Campeonato Brasileiro de Futebol, na ordem de colocação. Depois mostre:
#a) Os 5 primeiros times.
#b) Os últimos 4 colocados.
#c) Times em ordem alfabética.
#d) Em que posição está o time da São Paulo.

times = ("Palmeiras", "Flamengo", "Cruzeiro", "Mirassol", "Bahia", "Botafogo", "Fluminense", "São Paulo", "Atlético Mineiro", "Vasco da Gama", "Red Bull Bragantino", "Ceará", "Corinthians", "Grêmio", "Internacional", "Vitória", "Santos", "Juventude", "Fortaleza", "Sport")
print('=' *30)
print('OS 5 PRIMEIROS TIMES SÃO: ')
for pos, time in enumerate(times[:5], start=1):
    print(f'O {pos}º é {time}')
print('=' *30)
print('OS 4 ULTIMOS COLOCADOS SÃO: ')
for pos, time in enumerate(times[-4:], start=17):
    print(f'O {pos}º é {time}')
print('=' *30)
print('OS TIMES EM ORDEM ALFABÉTICA SÃO: ')
for time in sorted(times):
    print(f' - {time}', end=' ')
print('\n')
print('=' * 30)
print(f'O São Paulo está na {times.index("São Paulo") + 1}ª posição.')