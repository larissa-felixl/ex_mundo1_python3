salario = float(input('Me diga seu salário meu chefe, para eu ver se consigo te dar um aumento: '))
s1251 = (salario*10)/100
s1250 = (salario*15)/100
if salario > 1250:
    print('Nos meus cálculos seu aumento será no valor de {}, logo seu salário total será {}. '.format(s1251, (salario+s1251)))
else:
    print('Vou conseguir te dar um aumento de {}, seu salário ficará por volta de {}. '.format(s1250, (salario+s1250)))
# Escreva um programa que pergunte o salário de um funcionário e calcule o valor do seu aumento. Para salários superiores a R$1250,00, calcule um aumento de 10%. Para os inferiores ou iguais, o aumento é de 15%.