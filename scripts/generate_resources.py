#!/usr/bin/env python
"""
Script alternativo para crear un módulo resources_rc.py básico sin depender
de herramientas externas o PyQt6-tools.
"""

import base64
import sys
from pathlib import Path


def main():
    """
    Genera un archivo resources_rc.py básico que contiene las fuentes codificadas en base64.
    Este enfoque no requiere herramientas externas y funciona en cualquier entorno.
    """
    # Obtener la ruta al directorio de recursos
    resources_dir = Path('src/chat_gpt_local/gui/resources')
    fonts_dir = resources_dir / 'fonts'
    output_file = resources_dir / 'resources_rc.py'
    
    # Verificar que el directorio de fuentes existe
    if not fonts_dir.exists():
        print(f"Error: El directorio de fuentes no existe: {fonts_dir}")
        return 1
    
    # Obtener la lista de archivos de fuentes
    font_files = []
    for ext in ['*.ttf']:
        font_files.extend(list(fonts_dir.glob(ext)))
    
    if not font_files:
        print("Error: No se encontraron archivos de fuentes")
        return 1
    
    # Generar el contenido del archivo resources_rc.py
    py_content = [
        "# -*- coding: utf-8 -*-",
        "",
        "# Archivo generado manualmente - no editar",
        "# Este archivo proporciona las fuentes y otros recursos para la aplicación",
        "",
        "import base64",
        "import tempfile",
        "import os",
        "import atexit",
        "import shutil",
        "",
        "# Directorio temporal para almacenar fuentes extraídas",
        "_temp_dir = tempfile.mkdtemp(prefix='chat_gpt_local_resources_')",
        "",
        "# Limpiar el directorio temporal al salir",
        "@atexit.register",
        "def _cleanup_temp_dir():",
        "    if os.path.exists(_temp_dir):",
        "        shutil.rmtree(_temp_dir)",
        "",
        "# Diccionario de recursos (archivos)",
        "_resources = {}"
    ]
    
    # Procesar cada archivo de fuente
    print(f"Procesando {len(font_files)} archivos de fuentes...")
    for font_file in font_files:
        rel_path = font_file.relative_to(resources_dir.parent.parent)
        qrc_path = f":/fonts/{font_file.name}"
        
        # Leer el contenido del archivo en modo binario
        with open(font_file, 'rb') as f:
            content = f.read()
        
        # Codificar el contenido en base64
        encoded = base64.b64encode(content).decode('utf-8')
        
        # Agregar el recurso al diccionario
        py_content.append(f"""
# Recurso: {rel_path}
_resources["{qrc_path}"] = "{encoded}"
""")
    
    # Agregar funciones para acceder a los recursos
    py_content.extend([
        "",
        "def get_resource_path(resource_name):",
        "    \"\"\"",
        "    Obtiene la ruta a un recurso extraído.",
        "    Si el recurso no existe, lo extrae del código incorporado.",
        "    ",
        "    Args:",
        "        resource_name: La ruta del recurso (por ejemplo, ':/fonts/font.ttf')",
        "    ",
        "    Returns:",
        "        La ruta al archivo temporal que contiene el recurso extraído",
        "    \"\"\"",
        "    if resource_name not in _resources:",
        "        raise KeyError(f\"Recurso no encontrado: {resource_name}\")",
        "    ",
        "    # Crear la ruta de salida",
        "    basename = os.path.basename(resource_name)",
        "    output_path = os.path.join(_temp_dir, basename)",
        "    ",
        "    # Si el archivo ya existe, devolverlo",
        "    if os.path.exists(output_path):",
        "        return output_path",
        "    ",
        "    # Extraer el recurso",
        "    content = base64.b64decode(_resources[resource_name])",
        "    with open(output_path, 'wb') as f:",
        "        f.write(content)",
        "    ",
        "    return output_path",
        "",
        "# Compatibilidad con qrc"
        "def qCleanupResources():",
        "    pass",
        ""
    ])
    
    # Escribir el archivo
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write('\n'.join(py_content))
    
    print(f"Archivo de recursos generado exitosamente: {output_file}")
    print(f"Se han incluido {len(font_files)} archivos de fuentes.")
    return 0

if __name__ == "__main__":
    sys.exit(main())