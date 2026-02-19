# 🧪 TESTE DASHBOARD COM AUTOMAÇÃO REAL

## 🚀 **PASSO A PASSO COMPLETO**

### **1. Iniciar Servidor de Automação**
```bash
# Terminal 1 - Iniciar servidor Flask
cd "C:\Projetos Git\Automação de sistemas"
python servidor_automacao.py
```

**Resultado esperado:**
```
🚀 Servidor de Automação iniciado!
📡 Acesse: http://localhost:5000
🔧 Para parar: Ctrl+C
```

### **2. Abrir Dashboard**
```bash
# Abrir no navegador:
file:///C:/Projetos Git/Automação de sistemas/dashboard.html
```

### **3. Testar Automação Real**

#### **A) Cenário Ideal (Servidor Rodando):**
1. ✅ Clicar "Executar Automação"
2. ✅ Ver "Conectando com servidor..."
3. ✅ Ver "Automação iniciada com sucesso!"
4. ✅ Acompanhar progresso real (0% → 100%)
5. ✅ Ver "Automação concluída com sucesso!"
6. ✅ Dashboard atualiza com dados reais

#### **B) Cenário Fallback (Servidor OFF):**
1. ❌ Clicar "Executar Automação"
2. ⚠️ Ver erro de conexão
3. 🔄 Ver "Usando modo simulação..."
4. ✅ Simulação executa normalmente
5. ⚠️ Dashboard não atualiza (dados não reais)

### **4. Verificar Resultados**

#### **Métricas Atualizadas:**
- **Total Produtos**: 10 (após automação real)
- **Valor Total**: Calculado dos produtos reais
- **Estoque Baixo**: Baseado em dados reais
- **Críticos**: Produtos realmente críticos

#### **Gráficos Atualizados:**
- **Pizza**: Distribuição real por categoria
- **Barras**: Valores reais por categoria

### **5. Logs do Servidor**

**Terminal do Flask mostra:**
```
POST /executar-automacao - 200
GET /status-automacao - 200
GET /status-automacao - 200
...
```

### **6. Solução de Problemas**

#### **Erro: "Falha ao iniciar automação"**
```bash
# Verificar se servidor está rodando:
curl http://localhost:5000/status-automacao
```

#### **Erro: "CORS policy"**
- Flask-CORS já instalado ✅
- Servidor permite requisições do navegador ✅

#### **Erro: "Timeout"**
- Automação demora mais que 5 minutos
- Normal para muitos produtos

### **7. Comandos Úteis**

#### **Verificar Status via API:**
```bash
# No navegador ou Postman:
GET http://localhost:5000/status-automacao
```

#### **Parar Servidor:**
```bash
# No terminal do Flask:
Ctrl + C
```

#### **Reiniciar Tudo:**
```bash
# 1. Parar servidor (Ctrl+C)
# 2. Reiniciar:
python servidor_automacao.py
# 3. Refresh dashboard
```

---

## 🎯 **FLUXO COMPLETO DE TESTE**

### **Teste 1: Dashboard Vazio → Automação → Dashboard Populado**
1. Limpar localStorage (F12 → Console → `localStorage.clear()`)
2. Refresh dashboard (métricas zeradas)
3. Iniciar servidor Flask
4. Executar automação via dashboard
5. Ver dashboard populado com dados reais

### **Teste 2: Múltiplas Execuções**
1. Executar automação primeira vez
2. Tentar executar novamente (deve dar erro "já executando")
3. Aguardar terminar
4. Executar novamente (deve funcionar)

### **Teste 3: Servidor Offline**
1. Parar servidor Flask
2. Tentar executar automação
3. Ver fallback para simulação
4. Verificar que dados não mudam

---

## ✅ **CHECKLIST DE VALIDAÇÃO**

- [ ] Servidor Flask inicia sem erros
- [ ] Dashboard carrega corretamente
- [ ] Botão "Executar Automação" funciona
- [ ] Progresso é mostrado em tempo real
- [ ] Automação real é executada (Edge abre)
- [ ] Dashboard atualiza após automação
- [ ] Gráficos mostram dados reais
- [ ] Fallback funciona se servidor offline
- [ ] Exportar relatório funciona
- [ ] Múltiplas execuções funcionam

**Agora o dashboard atualiza com dados REAIS após a automação!** 🎉