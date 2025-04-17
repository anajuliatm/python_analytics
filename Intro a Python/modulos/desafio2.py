from math import hypot
cato = float(input('Cateto Oposto: '))
cata = float(input('Cateto Adjacente: '))
hipotenusa = hypot(cato, cata)
print(f'Um triangulo com lados {cato} e {cata}')
print(f'Tem hipotenusa igual a {hipotenusa}')
