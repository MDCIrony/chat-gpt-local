"""
Define colores y variables de estilo común para toda la aplicación.
"""

# Colores principales del tema cyberpunk
COLORS = {
    "background": "#0D1117",  # Fondo oscuro principal
    "background_secondary": "rgba(10, 14, 20, 0.7)",  # Fondo secundario con transparencia
    "accent_cyan": "#00FFFF",  # Cian brillante para acentos (usuario)
    "accent_magenta": "#FF00FF",  # Magenta brillante para acentos (asistente)
    "accent_green": "#39FF14",  # Verde neón para indicadores de estado
    "text_primary": "#FFFFFF",  # Texto principal
    "text_secondary": "#E0E0E0",  # Texto secundario
    "text_disabled": "#888888",  # Texto deshabilitado
    "code_text": "#AEE8FF",  # Color para código
    "input_background": "rgba(18, 26, 34, 0.8)",  # Fondo para áreas de entrada
    "scrollbar_background": "#0A0E14",  # Fondo para barras de desplazamiento
    "widget_background": "rgba(18, 26, 34, 0.5)",  # Fondo para widgets
    "border_color": "rgba(255, 255, 255, 0.1)",  # Color para bordes
}

# Gradientes comunes
GRADIENTS = {
    "scrollbar_handle": "qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #FF00FF, stop:1 #00FFFF)",
    "scrollbar_handle_hover": "qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #FF77FF, stop:1 #77FFFF)",
    "button_background": "qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #FF00FF, stop:1 #8A2BE2)",
    "button_background_hover": "qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #FF77FF, stop:1 #9945E8)",
    "button_background_pressed": "qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #CC00CC, stop:1 #6A1CB2)",
    "button_background_disabled": "qlineargradient(x1:0, y1:0, x2:1, y2:0, stop:0 #331933, stop:1 #25152F)",
}

# Fuentes
FONTS = {
    "main": "'Share Tech', sans-serif",
    "monospace": "'Share Tech Mono', monospace",
    "headers": "'Orbitron', sans-serif",
    "code": "'Fira Code', monospace",
    "content": "'Rajdhani', sans-serif",
}

# Rutas a archivos de fuentes
FONT_FILES = {
    "orbitron": ":/fonts/Orbitron-Regular.ttf",
    "share_tech_mono": ":/fonts/ShareTechMono-Regular.ttf",
    "rajdhani": ":/fonts/Rajdhani-Medium.ttf",
    "fira_code": ":/fonts/FiraCode-Regular.ttf",
}

# Radios de borde comunes
BORDER_RADIUS = {
    "small": "4px",
    "medium": "8px",
    "large": "12px",
    "extra_large": "15px",
}

# Espaciados comunes
SPACING = {
    "xs": "5px",
    "sm": "8px",
    "md": "12px",
    "lg": "15px",
    "xl": "20px",
    "xxl": "25px",
}