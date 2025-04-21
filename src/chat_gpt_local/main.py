"""
Punto de entrada principal para la aplicación Chat GPT Local.
"""

import sys

from PyQt6.QtWidgets import QApplication

from chat_gpt_local.config.settings import settings
from chat_gpt_local.gui.chat_window import ChatWindow
from chat_gpt_local.utils.helpers import handle_errors


@handle_errors
def main() -> int:
    """
    Función principal que inicia la aplicación.
    
    Returns:
        Código de salida de la aplicación
    """
    # Verificar que la clave API esté configurada
    if not settings.openai_api_key:
        print("Error: No se ha configurado la clave API de OpenAI.")
        print("Configura la variable de entorno OPENAI_API_KEY o crea un archivo .env")
        return 1
    
    # Crear la aplicación Qt
    app = QApplication(sys.argv)
    app.setApplicationName("Chat GPT Local")
    app.setStyle("Fusion")  # Usar estilo Fusion para una apariencia moderna
    
    # Crear y mostrar la ventana principal
    window = ChatWindow()
    window.show()
    
    # Ejecutar el bucle principal de la aplicación
    return app.exec()


if __name__ == "__main__":
    sys.exit(main())