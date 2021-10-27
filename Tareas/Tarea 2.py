print("\033[92mHello World\033[0m") # Empleamos el codigo de color ANSI de Python para cambiar el color del Texto al ser printeado en la consola.

# Usamos colorama para realizar el mismo ejercicio pero empleando un módula para el cambio de colores
import colorama
from colorama import Fore as color
colorama.init(autoreset=True)

print(color.GREEN+"Hello world")
# Output: Hello world (Color verde)
#         Hello world (Color verde)