from random import randint
from time import sleep
n = randint(0,5)
print('Acabei de pensar em um número de 0 até 5!')
print('-=-'*20)
num = int(input('Me diga um número de 0 á 5, para ver se pensamos no mesmo:'))
print('-=-'*20)
print('PROCESSANDO...')
sleep(1.5)
if n == num:
    print('Somos muito gêmeas, pensamos no mesmo número!')

else:
    print('Por favor, melhore, e da proxima vez pense no {}, junto comigo!'.format(n))
# Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou perdeu.