dias = int(input('Qual a quantidade de dias que você ficou com o carro? '))
km = float(input(f'Qual a quantidade de quilometros rodados nesses {dias} dias? '))
diaspg = int(dias*60)
kmspg = float(km*0.15)
totalpg = float(diaspg+kmspg)
print(f'O total a pagar pelo o aluguel do carro(considerando que cada dia com ele custa R$60 e cada km rodado custa R$0.15) é {totalpg}')
# Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.