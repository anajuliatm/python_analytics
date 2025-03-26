print('Soma')
n1 = int(input('Num 1: '))
n2 = int(input('Num 2: '))
# TIPOS: int, floar, bool e str

soma = n1 + n2

# print('Resultado: ', soma)
print('A soma {0} + {1} é {2}'.format(n1, n2, soma))
# print(type(n2)) - Mostra tipo da variavel

word = str(input('Digite uma palavra: '))
print(word.isnumeric())
# isalpha -> indica se é letra (alphabetic)
# isalphanum -> letra com numero, ou letra, ou numero
# isupper -> ve se a palavra está toda em letra maiuscula
