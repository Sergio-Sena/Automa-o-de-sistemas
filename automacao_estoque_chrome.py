from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.options import Options
import csv
import time
import os
from datetime import datetime, timedelta
import random

def automacao_estoque_chrome():
    """
    Automação do sistema de estoque usando Chrome
    """
    print("=== AUTOMAÇÃO SISTEMA DE ESTOQUE (CHROME) ===")
    
    # Configurar Chrome
    chrome_options = Options()
    chrome_options.add_argument("--start-maximized")
    # chrome_options.add_argument("--incognito")  # Descomente para modo incógnito
    
    # Inicializar driver Chrome
    driver = webdriver.Chrome(options=chrome_options)
    wait = WebDriverWait(driver, 10)
    
    try:
        # 1. Abrir página de login
        login_path = os.path.abspath("login.html")
        driver.get(f"file:///{login_path}")
        print("1. Página de login carregada")
        
        # 2. Fazer login
        print("2. Fazendo login...")
        
        # Aguardar campos aparecerem
        usuario_field = wait.until(EC.presence_of_element_located((By.ID, "username")))
        senha_field = driver.find_element(By.ID, "password")
        login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
        
        # Preencher e submeter
        usuario_field.clear()
        usuario_field.send_keys("sergio sena")
        
        senha_field.clear()
        senha_field.send_keys("123")
        
        login_btn.click()
        
        # 3. Aguardar alert e aceitar
        time.sleep(1)
        try:
            alert = driver.switch_to.alert
            alert.accept()
            print("3. Login realizado!")
        except:
            print("3. Sem alert de login")
        
        # 4. Navegar para sistema de estoque
        time.sleep(2)
        estoque_path = os.path.abspath("estoque.html")
        driver.get(f"file:///{estoque_path}")
        print("4. Sistema de estoque carregado")
        
        # 5. Aguardar página carregar
        time.sleep(2)
        
        # 6. Cadastrar produtos do CSV
        cadastrar_produtos_estoque(driver, wait)
        
    except Exception as e:
        print(f"Erro: {e}")
    
    finally:
        # Fechar navegador
        print("7. Fechando navegador...")
        time.sleep(3)
        driver.quit()
    
    print("=== AUTOMAÇÃO CONCLUÍDA ===")

def cadastrar_produtos_estoque(driver, wait):
    """
    Cadastra produtos no sistema de estoque
    """
    print("5. Iniciando cadastro de produtos no estoque...")
    
    contador = 0
    
    with open('estoque_produtos.csv', 'r', encoding='utf-8') as arquivo:
        reader = csv.DictReader(arquivo)
        
        for produto in reader:
            if contador >= 5:  # Limitar a 5 produtos para teste Chrome
                break
                
            codigo = produto['codigo']
            nome = produto['produto']
            categoria = produto['categoria']
            fornecedor = produto['fornecedor']
            estoque_atual = produto['estoque_atual']
            estoque_minimo = produto['estoque_minimo']
            preco_custo = produto['preco_custo']
            preco_venda = produto['preco_venda']
            localizacao = produto['localizacao']
            validade = produto['validade']
            
            print(f"Cadastrando produto {contador + 1}/5: {codigo} - {nome}")
            
            try:
                # Aguardar campos estarem disponíveis
                codigo_field = wait.until(EC.element_to_be_clickable((By.ID, "produto-codigo")))
                nome_field = driver.find_element(By.ID, "produto-nome")
                categoria_field = driver.find_element(By.ID, "produto-categoria")
                fornecedor_field = driver.find_element(By.ID, "produto-fornecedor")
                estoque_atual_field = driver.find_element(By.ID, "produto-estoque-atual")
                estoque_minimo_field = driver.find_element(By.ID, "produto-estoque-minimo")
                preco_custo_field = driver.find_element(By.ID, "produto-preco-custo")
                preco_venda_field = driver.find_element(By.ID, "produto-preco-venda")
                localizacao_field = driver.find_element(By.ID, "produto-localizacao")
                validade_field = driver.find_element(By.ID, "produto-validade")
                
                # Preencher campos
                codigo_field.clear()
                codigo_field.send_keys(codigo)
                time.sleep(0.3)
                
                nome_field.clear()
                nome_field.send_keys(nome)
                time.sleep(0.3)
                
                # Selecionar categoria
                categoria_select = Select(categoria_field)
                categoria_select.select_by_value(categoria)
                time.sleep(0.3)
                
                fornecedor_field.clear()
                fornecedor_field.send_keys(fornecedor)
                time.sleep(0.3)
                
                estoque_atual_field.clear()
                estoque_atual_field.send_keys(estoque_atual)
                time.sleep(0.3)
                
                estoque_minimo_field.clear()
                estoque_minimo_field.send_keys(estoque_minimo)
                time.sleep(0.3)
                
                preco_custo_field.clear()
                preco_custo_field.send_keys(preco_custo)
                time.sleep(0.3)
                
                preco_venda_field.clear()
                preco_venda_field.send_keys(preco_venda)
                time.sleep(0.3)
                
                localizacao_field.clear()
                localizacao_field.send_keys(localizacao)
                time.sleep(0.3)
                
                # Preencher validade - 3 opções disponíveis
                data_validade = gerar_data_validade(categoria, validade)
                if data_validade:
                    validade_field.clear()
                    validade_field.send_keys(data_validade)
                    time.sleep(0.3)
                    print(f"  Validade: {data_validade}")
                
                print(f"  Campos preenchidos para: {nome}")
                
                # Submeter formulário
                submit_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
                submit_btn.click()
                
                # Aguardar alert de sucesso
                time.sleep(2)
                try:
                    alert = wait.until(EC.alert_is_present())
                    alert_text = alert.text
                    print(f"  Alert: {alert_text}")
                    alert.accept()
                    print(f"  Produto {contador + 1} cadastrado com sucesso!")
                except:
                    print(f"  Sem alert - verificar se foi cadastrado")
                
                contador += 1
                time.sleep(1)  # Pausa entre produtos
                
            except Exception as e:
                print(f"  Erro ao cadastrar produto {contador + 1}: {e}")
                break
    
    print(f"6. Cadastro concluído! {contador} produtos processados.")

def gerar_data_validade(categoria, validade_csv):
    """
    Gera data de validade baseada em 3 estratégias:
    1. Usar data do CSV se existir
    2. Gerar automaticamente por categoria
    3. Usar data do sistema + offset
    """
    
    # Opção 1: Usar data do CSV se existir e for válida
    if validade_csv and validade_csv.strip() and validade_csv != "":
        return validade_csv
    
    # Opção 2: Gerar por categoria (mais realista)
    hoje = datetime.now()
    
    if categoria == "Eletronicos":
        # Eletrônicos: 2-3 anos de garantia
        dias = random.randint(730, 1095)  # 2-3 anos
    elif categoria == "Roupas":
        # Roupas: sem validade, retorna None
        return None
    elif categoria == "Casa":
        # Casa: 1-2 anos de garantia
        dias = random.randint(365, 730)  # 1-2 anos
    elif categoria == "Saude":
        # Saúde: 6 meses a 2 anos
        dias = random.randint(180, 730)  # 6 meses - 2 anos
    elif categoria == "Esportes":
        # Esportes: 1 ano de garantia
        dias = random.randint(365, 545)  # 1-1.5 anos
    else:
        # Padrão: 1 ano
        dias = 365
    
    # Opção 3: Data do sistema + offset (formato brasileiro)
    data_futura = hoje + timedelta(days=dias)
    return data_futura.strftime("%d/%m/%Y")

if __name__ == "__main__":
    automacao_estoque_chrome()