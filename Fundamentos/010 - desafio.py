larg = float(input('Qual a largura da sua parede?'))
alt = float(input('Qual a altura da sua parede?'))
area = larg*alt
print(f'A sua parede tem a dimensão de {larg}x{alt} e sua área é de {area}m².')

tinta = area / 2
print(f'Para pintar essa parede, você precisará de {tinta} litros de tinta.')
