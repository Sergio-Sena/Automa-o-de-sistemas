@echo off
echo ========================================
echo    SISTEMA DE AUTOMACAO - DEMO VIDEO
echo ========================================
echo.
echo Preparando ambiente para gravacao...
echo.

REM Verificar se tudo está OK
python teste_pre_gravacao.py

echo.
echo ========================================
echo INSTRUCOES PARA GRAVACAO:
echo ========================================
echo.
echo 1. Abrir OBS Studio
echo 2. Configurar captura de tela (1920x1080)
echo 3. Testar microfone
echo 4. Pressionar ENTER para iniciar servidor Flask
echo 5. Abrir dashboard.html no navegador
echo 6. Seguir roteiro em ROTEIRO_VIDEO_DEMO.md
echo.
pause

echo.
echo Iniciando servidor Flask...
echo Acesse: http://localhost:5000
echo Para parar: Ctrl+C
echo.
python servidor_automacao.py