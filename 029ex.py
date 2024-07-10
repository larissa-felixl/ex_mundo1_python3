v = int(input('Me diga a velocidade que seu carro está em km/h: '))
if v <= 80:
    print('Você está dirrigindo em uma velocidade descente! Continue assim! Tenha um bom dia!')
else:
    print('Com essa velocidade vocẽ vai provavelmente ser mutado!')
    va = v - 80
    multa = va*7
    print('E o valor da sua multa será de R${}.'.format(multa))
# Escreva um programa que leia a velocidade de um carro. Se ele ultrapassar 80Km/h, mostre uma mensagem dizendo que ele foi multado. A multa vai custar R$7,00 por cada Km acima do limite.