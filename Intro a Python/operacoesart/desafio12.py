print('Produto com Desconto')

oldPrice = float(input('Valor anterior: R$'))

# newPrice = 0.95 * oldPrice
newPrice = oldPrice - (oldPrice * (5 / 100))

print(f'Agora o produto custa R${newPrice:.2f}')
