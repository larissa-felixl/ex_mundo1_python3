nome = str(input('Digite seu nome: ')).strip()
print('Seu nome em letras maiusculas é {}'.format(nome.upper()))
print('Seu nome em letras minusculas é {}'.format(nome.lower()))
print('Seu nome ao todo tem {} letras'.format(len(nome)- nome.count(' ')))
separa = nome.split()
print('O seu primeiro nome é {}, e a quantidade de letras que ele contém é {}'.format(separa[0],len(separa[0])))
#Crie um programa que leia o nome completo de uma pessoa e mostre: 
#- O nome com todas as letras maiúsculas e minúsculas.
#- Quantas letras ao todo (sem considerar espaços).
#- Quantas letras tem o primeiro nome.