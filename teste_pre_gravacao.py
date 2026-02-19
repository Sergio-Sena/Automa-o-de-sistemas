#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Teste pré-gravação - Verificar se tudo está funcionando
"""

import os
import subprocess
import time
import sys

def verificar_arquivos():
    """Verificar se todos os arquivos necessários existem"""
    print("=== VERIFICANDO ARQUIVOS ===")
    
    arquivos_necessarios = [
        'dashboard.html',
        'servidor_automacao.py',
        'automacao_estoque.py',
        'estoque_produtos.csv',
        'login.html',
        'estoque.html'
    ]
    
    todos_ok = True
    for arquivo in arquivos_necessarios:
        if os.path.exists(arquivo):
            print(f"OK {arquivo}")
        else:
            print(f"ERRO {arquivo} - FALTANDO!")
            todos_ok = False
    
    return todos_ok

def verificar_dependencias():
    """Verificar dependências Python"""
    print("\n=== VERIFICANDO DEPENDENCIAS ===")
    
    try:
        import flask
        print("OK Flask")
    except ImportError:
        print("ERRO Flask - INSTALAR: pip install flask")
        return False
    
    try:
        import flask_cors
        print("OK Flask-CORS")
    except ImportError:
        print("ERRO Flask-CORS - INSTALAR: pip install flask-cors")
        return False
    
    try:
        import selenium
        print("OK Selenium")
    except ImportError:
        print("ERRO Selenium - INSTALAR: pip install selenium")
        return False
    
    return True

def verificar_csv():
    """Verificar se CSV tem dados"""
    print("\n=== VERIFICANDO CSV ===")
    
    try:
        with open('estoque_produtos.csv', 'r', encoding='utf-8') as f:
            linhas = f.readlines()
            print(f"OK CSV com {len(linhas)-1} produtos")
            return len(linhas) > 1
    except Exception as e:
        print(f"ERRO no CSV: {e}")
        return False

def teste_servidor_rapido():
    """Teste rápido do servidor Flask"""
    print("\n=== TESTE SERVIDOR FLASK ===")
    
    try:
        # Importar sem executar
        import servidor_automacao
        print("OK Servidor Flask importado com sucesso")
        return True
    except Exception as e:
        print(f"ERRO no servidor: {e}")
        return False

def main():
    """Função principal"""
    print("TESTE PRE-GRAVACAO - SISTEMA DE AUTOMACAO")
    print("=" * 50)
    
    # Verificações
    arquivos_ok = verificar_arquivos()
    deps_ok = verificar_dependencias()
    csv_ok = verificar_csv()
    servidor_ok = teste_servidor_rapido()
    
    # Resultado final
    print("\n" + "=" * 50)
    print("RESULTADO FINAL:")
    
    if arquivos_ok and deps_ok and csv_ok and servidor_ok:
        print("TUDO OK! PRONTO PARA GRAVAR!")
        print("\nPROXIMOS PASSOS:")
        print("1. Abrir OBS Studio")
        print("2. Configurar captura de tela")
        print("3. Testar microfone")
        print("4. Executar: python servidor_automacao.py")
        print("5. Abrir dashboard.html")
        print("6. GRAVAR!")
        return True
    else:
        print("PROBLEMAS ENCONTRADOS - CORRIGIR ANTES DE GRAVAR")
        return False

if __name__ == "__main__":
    main()