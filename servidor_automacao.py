from flask import Flask, jsonify, request
from flask_cors import CORS
import subprocess
import threading
import time
import os

app = Flask(__name__)
CORS(app)  # Permitir requisições do navegador

# Status global da automação
status_automacao = {
    'executando': False,
    'progresso': 0,
    'mensagem': '',
    'concluida': False
}

@app.route('/executar-automacao', methods=['POST'])
def executar_automacao():
    """
    Endpoint para executar a automação
    """
    global status_automacao
    
    if status_automacao['executando']:
        return jsonify({'erro': 'Automação já está executando'}), 400
    
    # Resetar status
    status_automacao = {
        'executando': True,
        'progresso': 0,
        'mensagem': 'Iniciando automação...',
        'concluida': False
    }
    
    # Executar automação em thread separada
    thread = threading.Thread(target=executar_automacao_background)
    thread.start()
    
    return jsonify({'sucesso': True, 'mensagem': 'Automação iniciada'})

@app.route('/status-automacao', methods=['GET'])
def obter_status():
    """
    Endpoint para obter status da automação
    """
    return jsonify(status_automacao)

def executar_automacao_background():
    """
    Executa a automação em background
    """
    global status_automacao
    
    try:
        # Atualizar status
        status_automacao['mensagem'] = 'Executando automacao_estoque.py...'
        status_automacao['progresso'] = 20
        
        # Executar script Python
        resultado = subprocess.run(
            ['python', 'automacao_estoque.py'],
            cwd=os.getcwd(),
            capture_output=True,
            text=True,
            timeout=300  # 5 minutos timeout
        )
        
        status_automacao['progresso'] = 80
        
        if resultado.returncode == 0:
            status_automacao['mensagem'] = 'Automação concluída com sucesso!'
            status_automacao['progresso'] = 100
            status_automacao['concluida'] = True
        else:
            status_automacao['mensagem'] = f'Erro na automação: {resultado.stderr}'
            status_automacao['progresso'] = 100
            
    except subprocess.TimeoutExpired:
        status_automacao['mensagem'] = 'Timeout: Automação demorou muito para executar'
        status_automacao['progresso'] = 100
    except Exception as e:
        status_automacao['mensagem'] = f'Erro inesperado: {str(e)}'
        status_automacao['progresso'] = 100
    
    finally:
        status_automacao['executando'] = False

@app.route('/limpar-dados', methods=['POST'])
def limpar_dados():
    """
    Endpoint para limpar dados do localStorage (simulação)
    """
    return jsonify({'sucesso': True, 'mensagem': 'Dados limpos'})

if __name__ == '__main__':
    print("🚀 Servidor de Automação iniciado!")
    print("📡 Acesse: http://localhost:5000")
    print("🔧 Para parar: Ctrl+C")
    app.run(debug=True, port=5000)