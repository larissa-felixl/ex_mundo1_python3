frase = str(input('Digite uma frase qualquer: ')).upper().strip()
print('A letra "A" aperece {} vezes na frase.'.format(frase.count('A')))
print('A primeira ocorrencia da letra "A" na frase acontece na posição {}.'.format(frase.find('A')+1))
print('A última ocorrencia da letra "A" é na posição {}.'.format(frase.rfind('A')+1))
#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra "A", em que posição ela aparece a primeira vez e em que posição ela aparece a última vez.
