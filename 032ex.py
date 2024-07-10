#from datetime import date
#ano = date.today().year
ano = int(input('Me diga o ano em que você nasceu: '))
if ano%4 == 0 and ano%100 !=100 or ano%400 ==0:
    print('Nossa você nasceu em um ano bissexto, tomara que não tenho sido no dia 29 de fevereiro!')
else:
    print('Legal vocasceu em um ano não bissexto!')
#Faça um programa que leia um ano qualquer e mostre se ele é bissexto.
