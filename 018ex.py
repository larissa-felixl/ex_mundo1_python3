import math
angulo = float(input('Me diga o valor do ângulo que vocẽ deseja descobrir o SENO, COSENO e a TANGENTE: '))
seno = math.sin(math.radians(angulo))
cos = math.cos(math.radians(angulo))
tan = math.tan(math.radians(angulo))
print('o valor do seno, cosseno e tangente,respectivamente, para o ângulo {} é {:.3f}, {:.3f}, {:.3f}'.format(angulo, seno, cos, tan))
#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.