#!/usr/bin/env python
"""
Script para compilar los recursos Qt (.qrc) a módulos Python.
"""

import os
import shutil
import subprocess
import sys


def main():
    """Compila los recursos Qt."""
    # Ruta al archivo .qrc
    resources_dir = os.path.join('src', 'chat_gpt_local', 'gui', 'resources')
    qrc_file = os.path.join(resources_dir, 'resources.qrc')
    
    # Ruta para el archivo Python compilado
    py_file = os.path.join(resources_dir, 'resources_rc.py')
    
    # Métodos para compilar recursos en orden de preferencia
    compilation_methods = [
        compile_with_pyrcc6,
        compile_with_pyqt_rcc,
        compile_with_system_rcc
    ]
    
    for method in compilation_methods:
        if method(qrc_file, py_file):
            print(f"Recursos compilados exitosamente: {py_file}")
            return 0
    
    print("Error: No se pudo compilar los recursos. Ningún método de compilación disponible.")
    return 1

def compile_with_pyrcc6(qrc_file, py_file):
    """Intenta compilar usando pyrcc6."""
    try:
        command = ['pyrcc6', qrc_file, '-o', py_file]
        subprocess.run(command, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def compile_with_pyqt_rcc(qrc_file, py_file):
    """Intenta compilar usando pyqt6-rcc."""
    try:
        command = ['pyqt6-rcc', qrc_file, '-o', py_file]
        subprocess.run(command, check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

def compile_with_system_rcc(qrc_file, py_file):
    """
    Intenta compilar usando el comando rcc del sistema.
    Este método funciona si Qt está instalado en el sistema.
    """
    try:
        # Primero intentar con rcc-qt6
        for rcc_command in ['rcc-qt6', 'rcc']:
            if shutil.which(rcc_command):
                # Crear archivo XML temporal
                xml_file = f"{qrc_file}.xml"
                command = [rcc_command, '--project', '-o', xml_file, qrc_file]
                subprocess.run(command, check=True)
                
                # Compilar a código Python
                command = [rcc_command, '--generator', 'python', '-o', py_file, xml_file]
                subprocess.run(command, check=True)
                
                # Limpiar archivo temporal
                if os.path.exists(xml_file):
                    os.remove(xml_file)
                
                return True
        return False
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False

if __name__ == "__main__":
    sys.exit(main())
