print('--TABUADA--')

num = int(input('Digite um número de 0 a 9: '))

i = 1
for i in range(0, 10):
    i += 1
    print(f'{num} x {i} = {num*i}')
