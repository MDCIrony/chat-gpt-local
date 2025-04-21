"""
Módulo para manejar los recursos de la aplicación.
"""

from PyQt6.QtCore import QFile, QIODevice
from PyQt6.QtGui import QFontDatabase

def load_resources():
    """
    Carga y registra las fuentes y otros recursos.
    Esta función debe ser llamada al inicio de la aplicación.
    """
    # Registrar fuentes
    font_files = [
        ":/fonts/Orbitron-Regular.ttf",
        ":/fonts/ShareTechMono-Regular.ttf",
        ":/fonts/Rajdhani-Medium.ttf",
        ":/fonts/FiraCode-Regular.ttf",
    ]
    
    for font_path in font_files:
        font_file = QFile(font_path)
        if font_file.open(QIODevice.OpenModeFlag.ReadOnly):
            font_id = QFontDatabase.addApplicationFontFromData(font_file.readAll())
            if font_id == -1:
                print(f"Error: No se pudo cargar la fuente {font_path}")
            font_file.close()
        else:
            print(f"Error: No se pudo abrir el archivo de fuente {font_path}")
