altura = float(input('Digite a altura da sua parede: '))
largura = float(input('Digite a largura da sua parede: '))
area = float(altura*largura)
quantidadeTinta = float(area/2) 
print(f'Sua parede tem dimensão de {altura}x{largura} e area de {area}m², a quantidade de latas de tinta necessária para pintar essa parede(se for usada uma lata de tinta pra cada 2 metros quadrados) é {quantidadeTinta}')
#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta necessária para pintá-la, sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.