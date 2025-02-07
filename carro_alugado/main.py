# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado.

km = float(input('Quantidade de kms rodados: '))
dias = int(input('Quantidade de dias: '))
conta = km * 0.15 + dias * 60

print(f'A conta a pagar do carro alugado é RS{conta}')