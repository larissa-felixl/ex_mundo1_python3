l1 = int(input('Me diga o valor de um dos lados do triângulo que você quer formar: '))
l2 = int(input('Me diga o valor de outro lado: '))
l3 = int(input('Me diga agora o valor do último lado: '))
if l1 > (l2+l3) and l2 > (l1+l3) and l3 > (l2+l1):
    print('Esse triângulo obdece a lei de formação, que diz que a soma de dois lados é sempre menor que o terceiro lado.')
else:
    print('Com essas medidas para os lados nunca se conseguiria ser formado um triângulo :( ')
#Desenvolva um programa que leia o comprimento de três retas e diga ao usuário se elas podem ou não formar um triângulo.