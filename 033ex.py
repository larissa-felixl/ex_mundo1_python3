primeiro = int(input('Me diga um número: '))
segundo = int(input('Me diga outro número: '))
terceiro = int(input('Me diga só mais um número: '))

maior = primeiro
if (segundo>maior):
    maior = segundo
if (terceiro>maior):
    terceiro = maior
print('O maior entre esses três números que você me deu é o {}!'.format(maior))

menor = primeiro
if (segundo<menor):
    menor = segundo
if (terceiro<menor):
    menor = terceiro
print('O menor número dessa sequência é o {}!'.format(menor))
#Faça um programa que leia três números e mostre qual é o maior e qual é o menor.
