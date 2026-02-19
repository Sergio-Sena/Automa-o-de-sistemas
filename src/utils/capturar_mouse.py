import pyautogui
import time

print("Capturador de Coordenadas do Mouse")
print("Pressione Ctrl+C para sair")
print("-" * 40)

try:
    while True:
        x, y = pyautogui.position()
        print(f"X: {x:4d} Y: {y:4d}", end='\r')
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nPrograma encerrado.")