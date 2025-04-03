print('--- Localiza ---')

km = float(input('KM Percorrido : '))
dias = int(input('Dias Alugado: '))

preco = (dias * 60) + (0.15 * km)

print(f'O preço da locação é de R${preco:.2f}')
