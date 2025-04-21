#!/usr/bin/env python
"""
Script para ejecutar la aplicación Chat GPT Local.
Añade el directorio src al PYTHONPATH para que el módulo sea encontrado.
"""

import os
import sys

# Añadir el directorio src al PYTHONPATH
src_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "src")
sys.path.insert(0, src_path)

# Importar el módulo principal y ejecutar la aplicación
from chat_gpt_local.main import main

if __name__ == "__main__":
    sys.exit(main())