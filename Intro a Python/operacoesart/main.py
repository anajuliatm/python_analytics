# Além dos comuns temos:
# ** -> Potencia
# // -> divisão inteira
# % -> Resto da divisao
# Ordem de Precedência:
# () -> ** -> *,/,//,% -> +, -
# nome = input('Qual seu nome? : ')
# print('Prazer em te conhecer {:=^10}!'.format(nome))
n1 = int(input("Valor 1: "))
n2 = int(input("Valor 2: "))

print("SOMA = {}".format(n1 + n2))
print("SUBSTRAÇÃO = {}".format(n1 - n2))
print("POTENCIA = {}".format(n1**n2))
print("DIVISÃO = {}".format(n1 / n2))
print("RESTO = {}".format(n1 % n2))
