#Crie um programa que gerencie o aproveitamento de um jogador de futebol. O programa vai ler o nome do jogador e quantas partidas ele
#  jogou. Depois vai ler a quantidade de gols feitos em cada partida. 
# No final, tudo isso será guardado em um dicionário, incluindo o total de gols feitos durante o campeonato.
jogador = {}
partidas= []
jogador['nome'] = str(input('Nome do jogador: '))
tot = int(input(f'Quantodas partidas {jogador['nome']} jogou? '))
for c in range(0, tot):
    partidas.append(int(input(f' Quantos gols na partida {c+1}? ')))
jogador['gols'] = partidas[:]
print('-='*30)
jogador ['total'] = sum(partidas)
print(jogador)
print('-='*30)
print(f' O jogador {jogador['nome']} jogou {tot} partidas, com um total de {jogador['total']} gols.')
print('-='*30)
print(f'O jogador {jogador['nome']} jogou {tot} partidas')
for i, v in enumerate(jogador['gols']):
    print(f'  => Na partida {i+1}, fez {v} gols.')
print(f'Foi um total de {jogador['total']} gols.')
print('-='*30)