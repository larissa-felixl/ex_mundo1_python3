dis = int(input('Me diga a distância do percurso que você quer fazer(em km/h), para eu poder calcular o provavel preço da passagem: '))
d200 = dis*0.50
d201 = dis*0.45
if dis <= 200:
    print('Provalvelmente o valor da sua passagem seria de R${}!'.format(d200))
else:
    print('provavelmente o preço da sua passagem seria de R${}!'.format(d201))
#Desenvolva um programa que pergunte a distância de uma viagem em Km. Calcule o preço da passagem, cobrando R$0,50 por Km para viagens de até 200Km e R$0,45 parta viagens mais longas.
