n = int(input('Digite um número de 0 a 9999: '))
u = n // 1 % 10
d = n // 10 % 10
c = n // 100 % 10
m = n // 1000 % 10 
print('O número da casa dos milhares é o {}'.format(m))
print('O número da casa das centenas é o {}'.format(c))
print('O número da casa das dezenas é o {}'.format(d))
print('O número da casa das unidades é o {}'.format(u))
#: Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.