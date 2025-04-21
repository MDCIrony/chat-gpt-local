"""
Estilos y configuraciones para los efectos visuales de la interfaz.
"""

from .base import COLORS


def hex_to_rgb(hex_color):
    """Convierte un color hexadecimal en una tupla RGB."""
    hex_color = hex_color.lstrip('#')
    if len(hex_color) == 6:
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    elif len(hex_color) == 8:  # Con canal alpha
        return tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4, 6))
    return (0, 0, 0)  # Negro por defecto en caso de error

def get_glitch_effect_colors():
    """Retorna los colores utilizados para el efecto de glitch."""
    return [COLORS["accent_cyan"], COLORS["accent_magenta"], COLORS["accent_green"]]

def get_scan_effect_config():
    """Retorna la configuración para el efecto de escaneo."""
    # Convertir el color de cadena hexadecimal a tupla RGB
    cyan_color = hex_to_rgb(COLORS["accent_cyan"])
    
    return {
        "speed": 2,  # Velocidad de movimiento de la línea de escaneo
        "update_interval": 30,  # Milisegundos entre actualizaciones (30ms)
        "line_color": cyan_color,  # Color de la línea principal como RGB
        "line_opacity": 90,  # Opacidad de la línea principal (0-255)
        "gradient_opacity": 50,  # Opacidad máxima del gradiente (0-255)
    }