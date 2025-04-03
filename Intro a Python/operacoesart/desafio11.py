print('-- TINTAS --')

largura = float(input('Largura da sua parede em metros: '))

altura = float(input('altura da sua parede em metros: '))

area = largura * altura

tintaL = area / 2

print(f'A área da sua parede é de {area} m2')

print(f'Você precisará de {tintaL: .2f}L de tinta')

resto = tintaL % 2
int(tintaL)
if resto >= 1:
    print(f'\nCompre {tintaL+resto}L para não faltar! ;)')
else:
    print(f'\nCompre {tintaL+1}L para não faltar! ;)')
