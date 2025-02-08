# Receba a quantidade de dinheiro, em reais, que uma pessoa tem para fazer uma viagem ao exterior. Receba, também, o valor da cotação do dólar do dia. Calcule e apresente o valor convertido em dólares.

reais = float(input('Quantidade de reais: '))
cotacao_dolar = float(input('Cotação do dólar: '))
conversao = reais/cotacao_dolar

print(f'R${reais} são USD{conversao}')