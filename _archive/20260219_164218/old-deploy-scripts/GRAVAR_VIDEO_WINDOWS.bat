@echo off
echo ========================================
echo    GRAVACAO DE VIDEO - WINDOWS NATIVO
echo ========================================
echo.
echo Este script vai gravar o video usando Xbox Game Bar (Windows 10/11)
echo.
echo INSTRUCOES:
echo 1. Pressione Windows + G para abrir Xbox Game Bar
echo 2. Clique no botao de gravacao (circulo branco)
echo 3. OU pressione Windows + Alt + R para iniciar/parar gravacao
echo.
echo O video sera salvo em: C:\Users\%USERNAME%\Videos\Captures
echo.
echo ========================================
echo Preparando sistema...
echo ========================================
echo.

REM Testar sistema
python teste_pre_gravacao.py

echo.
echo ========================================
echo PRESSIONE ENTER PARA INICIAR SERVIDOR
echo ========================================
pause

echo.
echo Servidor Flask iniciando...
echo.
echo AGORA:
echo 1. Pressione Windows + Alt + R para INICIAR gravacao
echo 2. Abra dashboard.html no navegador
echo 3. Execute a automacao
echo 4. Pressione Windows + Alt + R para PARAR gravacao
echo.
python servidor_automacao.py