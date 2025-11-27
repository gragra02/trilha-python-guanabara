#Aprimore o desafio 93 para que ele funcione com vários jogadores, incluindo um sistema de visualização 
# de detalhes do aproveitamento de cada jogador.

jogador = {}
partidas = []
times = []
while True:
    jogador.clear()
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantodas partidas {jogador['nome']} jogou? '))
    partidas.clear()
    for c in range(0, tot):
        partidas.append(int(input(f' Quantos gols na partida {c+1}? ')))
    jogador['gols'] = partidas[:]
    print('-='*30)
    jogador ['total'] = sum(partidas)
    times.append(jogador.copy())
    while True:
        resp = str(input('Quere continuar? [S/N] ')).upper().strip()
        if resp in 'SN':
            break
        print('Erro! Por favor, digite apenas S ou N.')
    if resp == 'N':
        break
print('-='*30)
print('cod ', end='')
for i in jogador.keys():
    print(f'{i:<15}', end='')
print()
print('-' * 40)
for i, v in enumerate(times):
    print(f'{i:>3}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 40)