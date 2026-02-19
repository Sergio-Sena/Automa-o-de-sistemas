import pyautogui
from time import sleep

# Automação completa do sistema
print("Iniciando automação...")

# 1. Minimizar tela da IDE
print("Minimizando IDE...")
pyautogui.click(1753, 32, duration=1)
sleep(1)
# 2. Abrir aplicação
print("Abrindo aplicação...")
pyautogui.doubleClick(58, 700, duration=1)
sleep(3)  # Aguardar app carregar

# 3. Cadastrar novo usuário
print("Cadastrando novo usuário...")
pyautogui.click(917, 646, duration=1)  # Botão cadastrar usuário
sleep(1)

# 4. Digitar nome do usuário
pyautogui.click(946, 627, duration=1)  # Campo nome
pyautogui.write("sergio sena")
sleep(1)

# 5. Digitar senha
pyautogui.click(948,582, duration=1)  # Campo senha
pyautogui.write("123")
sleep(1)
# 6. Confirmar cadastro
pyautogui.click(913,625, duration=1)  # Botão cadastrar
sleep(2)  # Aguardar processamento

# 7. Fazer login - digitar usuário
print("Fazendo login...")
pyautogui.click(957, 542, duration=1)  # Campo usuário login
pyautogui.write("sergio sena")
sleep(1)

# 8. Digitar senha do login
pyautogui.click(958, 578, duration=1)  # Campo senha login
pyautogui.write("123")
sleep(1)
# 9. Clicar em entrar
pyautogui.click(826,633, duration=1)  # Botão entrar
sleep(3)  # Aguardar login processar

print("Login realizado com sucesso!")

# 4- extrair produto
# Definir coordenadas dos campos
x_produto, y_produto = 533, 523
x_quantidade, y_quantidade = 529, 563
x_preco, y_preco = 530, 599

print("Iniciando cadastro de produtos...")
with open('produtos_ecommerce.csv', 'r', encoding='utf-8') as arquivo:
    linhas = arquivo.readlines()
    # Pular cabeçalho
    for linha in linhas[1:]:
        dados = linha.strip().split(',')
        nome_produto = dados[0]
        preco = dados[2]
        estoque = dados[3]
        
        print(f"Cadastrando: {nome_produto}")
        
        # Clicar e digitar produto
        pyautogui.click(x_produto, y_produto, duration=1)
        pyautogui.write(nome_produto)
        sleep(0.5)
        
        # Clicar e digitar quantidade (estoque)
        pyautogui.click(x_quantidade, y_quantidade, duration=1)
        pyautogui.write(estoque)
        sleep(0.5)
        
        # Clicar e digitar preço
        pyautogui.click(x_preco, y_preco, duration=1)
        pyautogui.write(preco)
        sleep(0.5)
        
        # Clicar em registrar
        pyautogui.click(417, 834, duration=1)
        
        # Aguardar antes do próximo produto
        sleep(2)

print("Cadastro de produtos concluído!")

# Feito automação
# Agora migrar para aws
