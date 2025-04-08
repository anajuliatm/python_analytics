import pyautogui
import time
import pandas

# pyautogui.click -> clicar em algum lugar
# pyautogui.press -> apertar uma tecla
# pyautogui.write -> escreve um texto
# pyautogui.hotkey -> aperta uma combinação de teclas
#  pyautogui.PAUSE = 1
pyautogui.PAUSE = 1
# Passo 1: Entrar no sistema da empresa
# abre o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# e digita o site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# espera 3 segundos
time.sleep(3)

# Passo 2: Fazer login
pyautogui.click(x=332, y=317)
# quando for pagina do chrome inteiro é: x=605 e y=378

pyautogui.write("anaju@gmail.com")
pyautogui.press("tab")
pyautogui.write("12345")

# botao que loga
pyautogui.press("tab")
pyautogui.press("enter")

# espera de 3 segundos
time.sleep(3)

# Passo 3: Importar a base de dados


tabela = pandas.read_csv("produtos.csv")
# se não estiver na mesma pasta q seu codigo, tem q digitar todo o caminho

# print(tabela)

# Passo 4: Cadastrar 1 produto
pyautogui.click(x=506, y=215)

codigo = "MOLO000251"
marca = "Logitech"
tipo = "Mouse"
categoria = "1"
preco_unitario = "25.95"
custo = "6.50"
obs = "teste"

pyautogui.write(codigo)
pyautogui.press("tab")
pyautogui.write(marca)
pyautogui.press("tab")
pyautogui.write(tipo)
pyautogui.press("tab")
pyautogui.write(categoria)
pyautogui.press("tab")
pyautogui.write(preco_unitario)
pyautogui.press("tab")
pyautogui.write(custo)
pyautogui.press("tab")
pyautogui.write(obs)
pyautogui.press("tab")  
pyautogui.press("enter")

# Passo 5: Repetir para todos os produtos

#  pyautogui -> fazer automações com python
# pip install pyautogui

# algumas automações são possíveis de rodar em segundo plano
