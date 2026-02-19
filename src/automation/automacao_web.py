import pyautogui
from time import sleep
import csv

def automacao_sistema_web():
    """
    Automação do sistema web de cadastro de produtos
    Baseado no app.py original, adaptado para navegador
    """
    
    print("=== AUTOMAÇÃO SISTEMA WEB ===")
    
    # 1. Minimizar IDE
    print("1. Minimizando IDE...")
    pyautogui.click(1747, 31, duration=1)
    sleep(1)
    
    # 2. Abrir navegador (ícone na barra de tarefas ou desktop)
    print("2. Abrindo navegador...")
    # Coordenadas do ícone do navegador
    pyautogui.click(1070, 1053, duration=1)  # Navegador
    sleep(3)  # Aguardar navegador abrir
    
    # 2.1. Clique adicional no navegador
    print("2.1. Clique adicional no navegador...")
    pyautogui.click(951, 626, duration=1)  # Clique adicional
    sleep(1)
    
    # 3. Navegar para o arquivo login.html
    print("3. Navegando para login.html...")
    pyautogui.hotkey('ctrl', 'l')  # Focar na barra de endereços
    sleep(0.5)
    pyautogui.hotkey('ctrl', 'a')  # Selecionar tudo na barra
    sleep(0.3)
    pyautogui.press('delete')  # Deletar conteúdo selecionado
    sleep(0.3)
    pyautogui.hotkey('ctrl', 'a')  # Selecionar novamente (garantia)
    sleep(0.2)
    pyautogui.write('file:///C:/Projetos%20Git/Automa%C3%A7%C3%A3o%20de%20sistemas/login.html')
    pyautogui.press('enter')
    sleep(3)  # Aguardar página carregar
    
    # 4. Fazer login
    print("4. Fazendo login...")
    # Coordenadas dos campos de login
    pyautogui.click(839, 535, duration=1)  # Campo usuário
    pyautogui.write("sergio sena")
    sleep(0.5)
    
    pyautogui.click(840, 583, duration=1)  # Campo senha  
    pyautogui.write("123")
    sleep(0.5)
    
    pyautogui.click(948, 640, duration=1)  # Botão login
    sleep(2)  # Aguardar alert aparecer
    
    # 4.1. Clicar OK no alert de login
    print("4.1. Clicando OK no alert...")
    pyautogui.click(1226, 291, duration=1)  # Botão OK
    sleep(2)  # Aguardar redirecionamento
    
    print("5. Login realizado! Iniciando cadastro de produtos...")
    
    # 3. Cadastrar produtos (primeiros 20 do CSV)
    cadastrar_produtos_csv()
    
    # 6. Fechar navegador
    print("6. Fechando navegador...")
    pyautogui.click(1881, 27, duration=1)  # Fechar navegador
    sleep(1)
    
    print("=== AUTOMAÇÃO CONCLUÍDA ===")

def cadastrar_produtos_csv():
    """
    Lê CSV e cadastra os primeiros 20 produtos
    """
    # Coordenadas dos campos da tela de produtos (5 campos)
    x_nome = 452       # Campo nome produto
    y_nome = 540
    
    x_categoria = 469  # Campo categoria
    y_categoria = 623
    
    x_quantidade = 455  # Campo quantidade  
    y_quantidade = 715
    
    x_preco = 1075     # Campo preço
    y_preco = 714
    
    x_descricao = 486  # Campo descrição
    y_descricao = 795
    
    x_botao = 958      # Botão registrar produto
    y_botao = 912
    
    contador = 0
    
    with open('produtos_ecommerce.csv', 'r', encoding='utf-8') as arquivo:
        reader = csv.DictReader(arquivo)
        
        for produto in reader:
            if contador >= 20:  # Limitar a 20 produtos
                break
                
            nome = produto['nome']
            categoria = produto['categoria']
            preco = produto['preco']
            estoque = produto['estoque']
            descricao = produto['descricao']
            
            print(f"Cadastrando produto {contador + 1}/20: {nome}")
            
            # Clicar e preencher nome (com foco garantido)
            pyautogui.click(x_nome, y_nome, duration=1)
            sleep(0.5)  # Aguardar foco no campo
            pyautogui.hotkey('ctrl', 'a')  # Selecionar tudo
            sleep(0.2)
            pyautogui.press('delete')  # Limpar campo
            sleep(0.3)
            # Garantir foco antes de escrever
            pyautogui.click(x_nome, y_nome, duration=0.5)
            sleep(0.2)
            pyautogui.write(nome)
            sleep(1)  # Delay aumentado para garantir
            
            # Clicar e preencher categoria
            pyautogui.click(x_categoria, y_categoria, duration=1)
            sleep(0.5)
            pyautogui.hotkey('ctrl', 'a')
            sleep(0.2)
            pyautogui.press('delete')
            sleep(0.2)
            pyautogui.write(categoria)
            sleep(0.8)
            
            # Clicar e preencher quantidade
            pyautogui.click(x_quantidade, y_quantidade, duration=1)
            sleep(0.5)
            pyautogui.hotkey('ctrl', 'a')
            sleep(0.2)
            pyautogui.press('delete')
            sleep(0.2)
            pyautogui.write(estoque)
            sleep(0.8)
            
            # Clicar e preencher preço
            pyautogui.click(x_preco, y_preco, duration=1)
            sleep(0.5)
            pyautogui.hotkey('ctrl', 'a')
            sleep(0.2)
            pyautogui.press('delete')
            sleep(0.2)
            pyautogui.write(preco)
            sleep(0.8)
            
            # Clicar e preencher descrição
            pyautogui.click(x_descricao, y_descricao, duration=1)
            sleep(0.5)
            pyautogui.hotkey('ctrl', 'a')
            sleep(0.2)
            pyautogui.press('delete')
            sleep(0.2)
            pyautogui.write(descricao)
            sleep(0.8)
            
            # Clicar em registrar
            pyautogui.click(x_botao, y_botao, duration=1)
            sleep(2.5)  # Aguardar processamento (aumentado)
            
            # Clicar OK no alert de sucesso
            pyautogui.click(498, 996, duration=1)
            sleep(1)  # Delay aumentado
            
            contador += 1
            
            # Após o 20º produto, fazer logout
            if contador == 20:
                print("Fazendo logout após 20º produto...")
                # Coordenada do botão logout
                pyautogui.click(958, 950, duration=1)  # Botão logout
                sleep(2)

def capturar_coordenadas():
    """
    Função auxiliar para capturar coordenadas da tela
    Execute esta função para descobrir as coordenadas corretas
    """
    print("Mova o mouse para a posição desejada e pressione Ctrl+C para parar")
    try:
        while True:
            x, y = pyautogui.position()
            print(f"Posição atual: X={x}, Y={y}", end='\r')
            sleep(0.1)
    except KeyboardInterrupt:
        print(f"\nCoordenadas capturadas: X={x}, Y={y}")

def capturar_coordenadas_navegador():
    """
    Guia para capturar coordenadas específicas do navegador
    """
    coordenadas_necessarias = [
        "1. Ícone do navegador (barra de tarefas ou desktop)",
        "2. Campo usuário (tela de login)", 
        "3. Campo senha (tela de login)",
        "4. Botão login",
        "5. Campo nome produto",
        "6. Campo quantidade", 
        "7. Campo preço",
        "8. Botão registrar produto"
    ]
    
    print("=== CAPTURA DE COORDENADAS ===")
    for item in coordenadas_necessarias:
        print(f"\n{item}")
        input("Pressione Enter quando estiver pronto para capturar...")
        capturar_coordenadas()

if __name__ == "__main__":
    # Descomente para capturar coordenadas individuais
    # capturar_coordenadas()
    
    # Descomente para capturar todas as coordenadas necessárias
    # capturar_coordenadas_navegador()
    
    # Execute a automação
    automacao_sistema_web()