"""
Estilos para la ventana principal de la aplicación.
"""

from .base import BORDER_RADIUS, COLORS, FONTS, GRADIENTS, SPACING


def get_main_window_style():
    """Retorna el estilo para la ventana principal."""
    return f"""
        QMainWindow {{
            background-color: {COLORS["background"]};
            /* Eliminando la imagen SVG de fondo que causa problemas */
        }}
        QScrollArea {{
            border: none;
            background-color: transparent;
        }}
        QScrollBar:vertical {{
            background-color: {COLORS["scrollbar_background"]};
            width: 10px;
            margin: 0px;
            border-radius: 5px;
        }}
        QScrollBar::handle:vertical {{
            background: {GRADIENTS["scrollbar_handle"]};
            min-height: 30px;
            border-radius: 5px;
        }}
        QScrollBar::handle:vertical:hover {{
            background: {GRADIENTS["scrollbar_handle_hover"]};
        }}
        QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {{
            border: none;
            background: none;
            height: 0px;
        }}
        QScrollBar::add-page:vertical, QScrollBar::sub-page:vertical {{
            background: rgba(0, 255, 255, 0.05);
            border-radius: 5px;
        }}
        QScrollBar:horizontal {{
            background-color: {COLORS["scrollbar_background"]};
            height: 10px;
            margin: 0px;
            border-radius: 5px;
        }}
        QScrollBar::handle:horizontal {{
            background: {GRADIENTS["scrollbar_handle"]};
            min-width: 30px;
            border-radius: 5px;
        }}
        QScrollBar::handle:horizontal:hover {{
            background: {GRADIENTS["scrollbar_handle_hover"]};
        }}
        QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {{
            border: none;
            background: none;
            width: 0px;
        }}
        QScrollBar::add-page:horizontal, QScrollBar::sub-page:horizontal {{
            background: rgba(0, 255, 255, 0.05);
            border-radius: 5px;
        }}
        QWidget {{
            background-color: transparent;
            color: {COLORS["text_secondary"]};
            font-family: {FONTS["main"]};
        }}
        QTextEdit {{
            border: 1px solid {COLORS["accent_cyan"]};
            border-radius: {BORDER_RADIUS["medium"]};
            background-color: {COLORS["input_background"]};
            color: {COLORS["text_primary"]};
            padding: {SPACING["md"]};
            font-size: 14px;
            font-family: {FONTS["main"]};
        }}
        QTextEdit:focus {{
            border: 2px solid {COLORS["accent_cyan"]};
            background-color: rgba(22, 38, 54, 0.9);
            /* Eliminada propiedad box-shadow no soportada por Qt */
        }}
        QPushButton {{
            background: {GRADIENTS["button_background"]};
            color: white;
            border-radius: {BORDER_RADIUS["medium"]};
            padding: 10px 20px;
            font-weight: bold;
            font-size: 14px;
            border: none;
            font-family: {FONTS["headers"]};
        }}
        QPushButton:hover {{
            background: {GRADIENTS["button_background_hover"]};
        }}
        QPushButton:pressed {{
            background: {GRADIENTS["button_background_pressed"]};
        }}
        QPushButton:disabled {{
            background-color: {COLORS["text_disabled"]};
            color: {COLORS["text_disabled"]};
        }}
        QMessageBox {{
            background-color: #0F1A26;
            color: {COLORS["text_primary"]};
            border: 1px solid {COLORS["accent_cyan"]};
            border-radius: 10px;
        }}
        QMessageBox QPushButton {{
            background: {GRADIENTS["button_background"]};
            color: white;
            border-radius: 6px;
            padding: 8px 16px;
            font-weight: bold;
        }}
        QLabel {{
            color: {COLORS["text_primary"]};
            font-family: {FONTS["main"]};
        }}
    """

def get_header_styles():
    """Retorna los estilos para los componentes del encabezado."""
    styles = {
        "title": f"""
            color: {COLORS["accent_cyan"]}; 
            font-size: 28px; 
            font-weight: bold;
            letter-spacing: 3px;
            font-family: {FONTS["headers"]};
            background-color: transparent;
            padding: 5px 15px;
            border-bottom: 2px solid {COLORS["accent_cyan"]};
        """,
        "status": f"""
            color: {COLORS["accent_green"]};
            background-color: rgba(57, 255, 20, 0.1);
            border: 1px solid {COLORS["accent_green"]};
            border-radius: 4px;
            padding: 5px 10px;
            font-size: 12px;
            font-weight: bold;
            font-family: {FONTS["monospace"]};
        """,
        "mode": f"""
            color: {COLORS["accent_magenta"]};
            background-color: rgba(255, 0, 255, 0.1);
            border: 1px solid {COLORS["accent_magenta"]};
            border-radius: 4px;
            padding: 5px 10px;
            margin-left: 10px;
            font-size: 12px;
            font-weight: bold;
            font-family: {FONTS["monospace"]};
        """
    }
    return styles

def get_input_area_styles():
    """Retorna los estilos para el área de entrada de mensajes."""
    styles = {
        "container": f"""
            QFrame {{
                background-color: {COLORS["background_secondary"]};
                border: 1px solid {COLORS["accent_cyan"]};
                border-radius: {BORDER_RADIUS["extra_large"]};
                padding: 2px;
            }}
        """,
        "frame": """
            QFrame {
                background-color: rgba(18, 26, 34, 0.9);
                border-radius: 14px;
                padding: 5px;
            }
        """,
        "prefix": f"""
            color: {COLORS["accent_cyan"]};
            font-size: 12px;
            font-family: {FONTS["monospace"]};
            background-color: rgba(0, 255, 255, 0.1);
            padding: 8px;
            border-radius: 4px;
        """,
        "input": f"""
            border: none;
            background-color: {COLORS["widget_background"]};
            color: {COLORS["text_primary"]};
            font-size: 14px;
            font-family: {FONTS["main"]};
            padding: 8px;
            border-radius: {BORDER_RADIUS["medium"]};
        """,
        "send_button": f"""
            QPushButton {{
                background: {GRADIENTS["button_background"]};
                color: white;
                border-radius: {BORDER_RADIUS["medium"]};
                padding: 12px 25px;
                font-weight: bold;
                font-size: 14px;
                font-family: {FONTS["headers"]};
                letter-spacing: 1px;
                border: none;
            }}
            QPushButton:hover {{
                background: {GRADIENTS["button_background_hover"]};
            }}
            QPushButton:disabled {{
                background: {GRADIENTS["button_background_disabled"]};
                color: {COLORS["text_disabled"]};
            }}
        """
    }
    return styles

def get_scroll_area_styles():
    """Retorna los estilos para el área de desplazamiento de mensajes."""
    styles = {
        "container": f"""
            QFrame {{
                background-color: {COLORS["background_secondary"]};
                border: 1px solid {COLORS["accent_cyan"]};
                border-radius: {BORDER_RADIUS["extra_large"]};
                padding: 2px;
            }}
        """,
        "scrollarea": """
            QScrollArea {
                background-color: transparent;
                border: none;
                border-radius: 14px;
            }
        """
    }
    return styles