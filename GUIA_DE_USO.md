# 📋 GUIA DE USO - Sistema de Estoque Automatizado

## 🎯 **VISÃO GERAL**
Sistema completo de controle de estoque com automação Selenium para cadastro em massa de produtos.

---

## 📁 **ARQUIVOS DO SISTEMA**

### **Principais:**
- `login.html` - Tela de login do sistema
- `estoque.html` - Sistema principal de estoque
- `estoque_produtos.csv` - Base de dados dos produtos
- `automacao_estoque.py` - Automação Selenium

### **Dados:**
- `produtos_ecommerce_completo.csv` - Backup completo (118 produtos)
- `produtos_ecommerce.csv` - Versão reduzida (20 produtos)

---

## 🚀 **COMO USAR**

### **1. USO MANUAL (Interface Web)**

#### **Passo 1: Login**
```bash
# Abrir no navegador:
file:///C:/Projetos Git/Automação de sistemas/login.html

# Credenciais:
Usuário: sergio sena
Senha: 123
```

#### **Passo 2: Acessar Sistema**
- Após login → Redireciona para `estoque.html`
- Dashboard mostra métricas em tempo real

#### **Passo 3: Cadastrar Produtos**
**Campos obrigatórios:**
- **Código**: EST001, EST002... (único)
- **Nome**: Nome do produto
- **Categoria**: Dropdown (Eletrônicos, Roupas, Casa, Saúde, Esportes)
- **Fornecedor**: Nome do fornecedor
- **Estoque Atual**: Quantidade em estoque
- **Estoque Mínimo**: Alerta de reposição
- **Preço Custo**: Valor de compra
- **Preço Venda**: Valor de venda
- **Localização**: Ex: A1-P2 (corredor-prateleira)

**Campo opcional:**
- **Validade**: Formato dd/mm/aaaa

---

### **2. USO AUTOMATIZADO (Selenium)**

#### **Pré-requisitos:**
```bash
# Instalar Selenium (se não instalado):
pip install selenium

# Verificar se Edge está instalado (já vem no Windows)
```

#### **Executar Automação:**
```bash
# Navegar para pasta:
cd "C:\Projetos Git\Automação de sistemas"

# Executar automação:
python automacao_estoque.py
```

#### **O que a automação faz:**
1. **Abre Edge** automaticamente
2. **Faz login** (sergio sena / 123)
3. **Navega** para sistema de estoque
4. **Cadastra 10 produtos** do CSV automaticamente
5. **Gera datas** de validade inteligentes
6. **Fecha navegador** ao final

---

## 📊 **DASHBOARD - MÉTRICAS**

### **Cards informativos:**
- **Total Produtos**: Quantidade cadastrada
- **Estoque Baixo**: Produtos próximos ao mínimo
- **Valor Total**: Soma do valor em estoque
- **Produtos Críticos**: Abaixo do estoque mínimo

### **Lista de produtos:**
- **Cores por status**:
  - 🔵 **Normal**: Estoque adequado
  - 🟡 **Baixo**: Próximo ao mínimo
  - 🔴 **Crítico**: Abaixo do mínimo

---

## 🗂️ **ESTRUTURA DOS DADOS**

### **CSV de Estoque (estoque_produtos.csv):**
```csv
codigo,produto,categoria,fornecedor,estoque_atual,estoque_minimo,preco_custo,preco_venda,localizacao,validade
EST001,iPhone 15 Pro,Eletronicos,Apple Inc,25,5,4500.00,5999.99,A1-P1,16/12/2025
```

### **Categorias disponíveis:**
- **Eletronicos**: Garantia 2-3 anos
- **Roupas**: Sem validade
- **Casa**: Garantia 1-2 anos  
- **Saude**: Validade 6 meses - 2 anos
- **Esportes**: Garantia 1-1.5 anos

---

## ⚙️ **CONFIGURAÇÕES**

### **Alterar quantidade de produtos:**
```python
# No arquivo automacao_estoque.py, linha 67:
if contador >= 10:  # Alterar para quantidade desejada
```

### **Alterar credenciais:**
```python
# No arquivo automacao_estoque.py, linhas 35-38:
usuario_field.send_keys("seu_usuario")
senha_field.send_keys("sua_senha")
```

### **Personalizar datas:**
```python
# No arquivo automacao_estoque.py, função gerar_data_validade():
# Alterar ranges de dias por categoria
```

---

## 🔧 **SOLUÇÃO DE PROBLEMAS**

### **Erro: "Selenium não encontrado"**
```bash
pip install selenium
```

### **Erro: "Edge não encontrado"**
- Edge já vem no Windows 10/11
- Verificar se está atualizado

### **Erro: "Arquivo CSV não encontrado"**
- Verificar se `estoque_produtos.csv` está na pasta
- Executar comando na pasta correta

### **Campos não preenchidos:**
- Verificar se IDs dos campos HTML estão corretos
- Aumentar delays no código se necessário

---

## 📈 **PRÓXIMOS PASSOS**

### **Melhorias possíveis:**
1. **Relatórios**: Exportar dados para Excel
2. **Movimentação**: Entrada/saída de produtos
3. **Alertas**: Email quando estoque baixo
4. **Backup**: Salvar dados em banco
5. **Multi-usuário**: Diferentes níveis de acesso

### **Integração:**
- **ERP**: Conectar com sistemas existentes
- **API**: Criar endpoints REST
- **Mobile**: App para consulta
- **BI**: Dashboards avançados

---

## 📞 **SUPORTE**

**Para dúvidas ou problemas:**
1. Verificar este guia primeiro
2. Testar manualmente antes da automação
3. Conferir logs no console do Python
4. Validar estrutura do CSV

**Sistema testado em:**
- Windows 10/11
- Edge (versão atual)
- Python 3.8+
- Selenium 4.x