from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.edge.options import Options
import csv
import time
import os

def automacao_edge():
    """
    Automação usando Edge (já vem no Windows)
    """
    print("=== AUTOMAÇÃO COM EDGE ===")
    
    # Configurar Edge
    edge_options = Options()
    edge_options.add_argument("--start-maximized")
    
    # Inicializar driver Edge
    driver = webdriver.Edge(options=edge_options)
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
        
        # 4. Aguardar redirecionamento para cadastro
        time.sleep(3)
        
        # Aguardar seção de produtos aparecer
        produtos_section = wait.until(EC.visibility_of_element_located((By.ID, "produtos-section")))
        print("4. Seção de produtos carregada")
        
        # 5. Cadastrar produtos
        cadastrar_produtos_edge(driver, wait)
        
    except Exception as e:
        print(f"Erro: {e}")
    
    finally:
        # Fechar navegador
        print("6. Fechando navegador...")
        time.sleep(2)
        driver.quit()
    
    print("=== AUTOMAÇÃO CONCLUÍDA ===")

def cadastrar_produtos_edge(driver, wait):
    """
    Cadastra produtos usando Edge
    """
    print("4. Iniciando cadastro de produtos...")
    
    contador = 0
    
    with open('produtos_ecommerce.csv', 'r', encoding='utf-8') as arquivo:
        reader = csv.DictReader(arquivo)
        
        for produto in reader:
            if contador >= 5:  # Limitar a 5 produtos para teste
                break
                
            nome = produto['nome']
            categoria = produto['categoria']
            preco = produto['preco']
            estoque = produto['estoque']
            descricao = produto['descricao']
            
            print(f"Cadastrando produto {contador + 1}/5: {nome}")
            
            try:
                # Aguardar campos estarem disponíveis e visíveis
                nome_field = wait.until(EC.element_to_be_clickable((By.ID, "produto-nome")))
                
                # Scroll para garantir que o elemento está visível
                driver.execute_script("arguments[0].scrollIntoView();", nome_field)
                categoria_field = driver.find_element(By.ID, "produto-categoria")
                quantidade_field = driver.find_element(By.ID, "produto-quantidade")
                preco_field = driver.find_element(By.ID, "produto-preco")
                descricao_field = driver.find_element(By.ID, "produto-descricao")
                registrar_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")
                
                # Preencher campos usando send_keys (mais confiável)
                nome_field.clear()
                nome_field.send_keys(nome)
                print(f"  Nome: {nome}")
                time.sleep(0.5)
                
                categoria_field.clear()
                categoria_field.send_keys(categoria)
                print(f"  Categoria: {categoria}")
                time.sleep(0.5)
                
                quantidade_field.clear()
                quantidade_field.send_keys(estoque)
                print(f"  Quantidade: {estoque}")
                time.sleep(0.5)
                
                preco_field.clear()
                preco_field.send_keys(preco)
                print(f"  Preco: {preco}")
                time.sleep(0.5)
                
                descricao_field.clear()
                descricao_field.send_keys(descricao)
                print(f"  Descricao: {descricao}")
                time.sleep(0.8)
                
                # Chamar função JavaScript diretamente
                print(f"  Chamando função cadastrarProduto...")
                
                # Chamar a função JavaScript diretamente
                driver.execute_script("""
                    var event = new Event('submit', { bubbles: true, cancelable: true });
                    document.querySelector('form').dispatchEvent(event);
                """)
                print(f"  Evento submit disparado")
                
                # Aguardar alert de sucesso aparecer
                print(f"  Aguardando alert...")
                time.sleep(3)  # Delay maior para alert aparecer
                
                try:
                    alert = wait.until(EC.alert_is_present())
                    alert_text = alert.text
                    print(f"  Alert encontrado: {alert_text}")
                    alert.accept()
                    print(f"  Produto {contador + 1} REALMENTE registrado!")
                except:
                    print(f"  ERRO: Nenhum alert apareceu - produto NÃO foi registrado")
                    # Tentar forçar o clique novamente
                    driver.execute_script("document.querySelector('button[type=\"submit\"]').click();")
                    time.sleep(2)
                    try:
                        alert = driver.switch_to.alert
                        alert.accept()
                        print(f"  Segundo clique funcionou!")
                    except:
                        print(f"  Falha total no cadastro")
                
                contador += 1
                time.sleep(2)  # Delay maior entre produtos
                
            except Exception as e:
                print(f"  Erro: {e}")
                break
    
    # Logout após todos os produtos
    if contador == 5:
        print("5. Fazendo logout após 5 produtos...")
        try:
            logout_btn = driver.find_element(By.CSS_SELECTOR, ".btn-danger")
            logout_btn.click()
            time.sleep(1)
        except Exception as e:
            print(f"Erro no logout: {e}")

if __name__ == "__main__":
    automacao_edge()