# Um comerciante comprou um produto e quer vendê-lo com um lucro de 45% se o valor da compra for menor que R$ 20,00; caso contrário, o lucro será de 30%. Escreva um programa em Python que receba o valor do produto e exiba o valor da venda.

compra = float(input('Quanto custou? '))

if compra < 20:
  print(f'O valor de venda será {compra * 1.45}')
else:
  print(f'O valor de venda será {compra * 1.3}')
  