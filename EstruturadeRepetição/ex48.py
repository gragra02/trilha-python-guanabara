#Faça um programa que calcule a soma entre todos os números que são múltiplos de três
#  e que se encontram no intervalo de 1 até 500.
# for s in range (1, 501):

#     if s % 3 == 0:
#         print(s)

s=0
cont = 0
for c in range (3,501,6):
   if c % 3 == 0:
      s += c
      cont += 1
print (s)
print (cont) 