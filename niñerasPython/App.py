# importo la clase NiñerasController desde el módulo donde se aloja
from src.controller.NiñerasController import NiñerasController

# # otra vez importo os para manipular archivos en este caso los csv
# import os

# # módulo útil para realizar operaciones de alto nivel como copiar, mover, eliminar, y manejar archivos y directorios enteros.
# import shutil

# comprueba si el script se está ejecutando directamente (no importado como un módulo en otro script). Si es así, el código dentro de este bloque se ejecutará
if __name__ == "__main__":

# crea una instancia de la clase
    controlador = NiñerasController()

#llama al método de la instancia controlador e inicia su flujo
    controlador.ejecutar()


"""Esta parte final del código (SOLO PARA CUANDOEL PERFÍL NO ESTA CONFIGURADO PARA PYTHON) recorre todos los directorios y subdirectorios comenzando desde el
directorio actual. Busca el subdirectirio __pycache__, lo elimina junto con todo el contenido.
Este script es útil para limpiar los directorios __pycache__ generados por Python cuando no deseas que se almacenen los archivos bytecode compilados.
ROOT: dierctorio actual que se está iterando
DIRS: lista de subdirectorios
FILES: lista de archivos
"""
# # itera cada directorio
# for root, dirs, files in os.walk("."):
#     #  subdirectorios desde el actual
#     for dir in dirs:
#         # busca __pycache__ para eliminarlo
#         if dir == "__pycache__":
#             # lo elimina consu contenido de manera recursiva
#             shutil.rmtree(os.path.join(root, dir))
