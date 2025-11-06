#Melhore o DESAFIO 61, perguntando para o usuário se ele quer mostrar mais alguns termos. 
#O programa encerrará quando ele disser que quer mostrar 0 termos.
print("Gerador de PA")
print("-=" * 10)
primeiro = int(input('Primeiro termo: '))
razão = int(input('Digite a razão: '))
termo = primeiro
cont = 1
mais = 10
total = 0
while mais != 0:
    total += mais
    while cont <= total:
        print(f"{termo} -> ", end=" ")
        termo += razão
        cont += 1
    print("PAUSA")
    mais = int(input(("Quatos termos quer mostrar: ")))
print(f"PA finalizada com {total} termos mostrados.")