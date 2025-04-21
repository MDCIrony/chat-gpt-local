"""
Estilos para los widgets de mensajes y efectos visuales.
"""

from .base import BORDER_RADIUS, COLORS, FONTS, SPACING


def get_message_frame_style(is_user=False):
    """
    Retorna el estilo para el marco del mensaje.
    
    Args:
        is_user: Si el mensaje es del usuario o del asistente
    """
    # Configurar colores según si es usuario o asistente
    if is_user:
        bg_color = "#111927"
        border_color = COLORS["accent_cyan"]
    else:
        bg_color = "#1A0F26"
        border_color = COLORS["accent_magenta"]
    
    return f"""
        QFrame {{
            background-color: {bg_color}; 
            border: 1px solid {border_color};
            border-radius: {BORDER_RADIUS["large"]}; 
            padding: {SPACING["md"]};
        }}
    """

def get_avatar_style(is_user=False):
    """
    Retorna el estilo para el avatar del mensaje.
    
    Args:
        is_user: Si el mensaje es del usuario o del asistente
    """
    avatar_color = COLORS["accent_cyan"] if is_user else COLORS["accent_magenta"]
    
    return f"""
        background-color: {avatar_color};
        border-radius: 15px;
        color: #000000;
        font-weight: bold;
        font-size: 14px;
    """

def get_role_label_style(is_user=False):
    """
    Retorna el estilo para la etiqueta de rol.
    
    Args:
        is_user: Si el mensaje es del usuario o del asistente
    """
    color = COLORS["accent_cyan"] if is_user else COLORS["accent_magenta"]
    
    return f"""
        color: {color}; 
        font-weight: bold; 
        font-size: 12px;
        font-family: {FONTS["headers"]};
    """

def get_time_label_style(is_user=False):
    """
    Retorna el estilo para la etiqueta de tiempo.
    
    Args:
        is_user: Si el mensaje es del usuario o del asistente
    """
    avatar_color = COLORS["accent_cyan"] if is_user else COLORS["accent_magenta"]
    
    return f"""
        color: #A7B6C2; 
        font-size: 10px;
        font-family: {FONTS["monospace"]};
        background-color: rgba(0, 0, 0, 0.3);
        padding: 2px 5px;
        border-radius: 3px;
        border-left: 1px solid {avatar_color};
    """

def get_markdown_css_template():
    """
    Retorna la plantilla CSS para contenido Markdown.
    Incluye un parámetro de formateo 'avatar_color' que debe ser reemplazado
    con el color correspondiente.
    """
    return """
        @font-face {{
            font-family: 'Share Tech Mono';
            src: url('qrc:/fonts/ShareTechMono-Regular.ttf') format('truetype');
            font-weight: normal;
            font-style: normal;
        }}
        @font-face {{
            font-family: 'Rajdhani';
            src: url('qrc:/fonts/Rajdhani-Medium.ttf') format('truetype');
            font-weight: 500;
            font-style: normal;
        }}
        @font-face {{
            font-family: 'Fira Code';
            src: url('qrc:/fonts/FiraCode-Regular.ttf') format('truetype');
            font-weight: normal;
            font-style: normal;
        }}
        @font-face {{
            font-family: 'Orbitron';
            src: url('qrc:/fonts/Orbitron-Regular.ttf') format('truetype');
            font-weight: normal;
            font-style: normal;
        }}
        
        body {{
            font-family: 'Rajdhani', sans-serif;
            color: #FFFFFF;
            background-color: transparent;
            margin: 0;
            padding: 5px 0;
            line-height: 1.5;
        }}
        pre {{
            background-color: rgba(0, 0, 0, 0.5);
            border-left: 3px solid {avatar_color};
            border-top: 1px solid rgba(255, 255, 255, 0.1);
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            border-radius: 4px;
            padding: 12px;
            overflow-x: auto;
            font-family: 'Fira Code', monospace;
            margin: 15px 0;
            /* Eliminada propiedad box-shadow */
        }}
        code {{
            font-family: 'Fira Code', monospace;
            background-color: rgba(0, 0, 0, 0.3);
            border-radius: 3px;
            padding: 2px 4px;
            color: #AEE8FF; /* Azul claro para código */
        }}
        a {{
            color: {avatar_color};
            text-decoration: none;
            border-bottom: 1px dotted {avatar_color};
            padding-bottom: 1px;
        }}
        a:hover {{
            border-bottom: 1px solid {avatar_color};
            /* Eliminada propiedad text-shadow */
        }}
        blockquote {{
            border-left: 3px solid {avatar_color};
            margin-left: 0;
            padding: 10px 20px;
            background-color: rgba(0, 0, 0, 0.2);
            color: #E0E0E0;
            font-style: italic;
            border-radius: 0 5px 5px 0;
        }}
        ul, ol {{
            padding-left: 25px;
        }}
        li {{
            margin-bottom: 5px;
        }}
        li::marker {{
            color: {avatar_color};
        }}
        table {{
            border-collapse: collapse;
            width: 100%;
            margin: 15px 0;
            background-color: rgba(0, 0, 0, 0.2);
            /* Eliminada propiedad box-shadow */
        }}
        th, td {{
            border: 1px solid #333;
            padding: 10px;
            text-align: left;
        }}
        th {{
            background-color: rgba(0, 0, 0, 0.5);
            color: {avatar_color};
            font-family: 'Share Tech Mono', monospace;
            text-transform: uppercase;
            font-weight: normal;
            letter-spacing: 1px;
        }}
        tr:nth-child(even) {{
            background-color: rgba(255, 255, 255, 0.05);
        }}
        h1, h2, h3, h4, h5, h6 {{
            color: {avatar_color};
            font-family: 'Orbitron', sans-serif;
            border-bottom: 1px solid rgba(255, 255, 255, 0.1);
            padding-bottom: 5px;
            margin-top: 25px;
            margin-bottom: 15px;
            font-weight: 500;
            letter-spacing: 1px;
        }}
        h1 {{ font-size: 1.8em; }}
        h2 {{ font-size: 1.5em; }}
        h3 {{ font-size: 1.3em; }}
        h4, h5, h6 {{ font-size: 1.1em; }}
        p {{
            margin: 10px 0;
        }}
        strong {{
            color: #FFFFFF;
            font-weight: 600;
        }}
        em {{
            font-style: italic;
            color: #D0D0D0;
        }}
        img {{
            max-width: 100%;
            border-radius: 5px;
            border: 1px solid {avatar_color};
        }}
        ::-webkit-scrollbar {{
            width: 8px;
            height: 8px;
        }}
        ::-webkit-scrollbar-track {{
            background: rgba(0, 0, 0, 0.2);
            border-radius: 4px;
        }}
        ::-webkit-scrollbar-thumb {{
            background: {avatar_color};
            border-radius: 4px;
        }}
    """

def get_html_template():
    """
    Retorna la plantilla HTML para el contenido de mensajes.
    Incluye tres parámetros de formateo:
    - 'css_styles': Los estilos CSS
    - 'html_content': El contenido HTML generado desde Markdown
    """
    return """
    <html>
    <head>
        <style>
            {css_styles}
        </style>
    </head>
    <body>
        {html_content}
    </body>
    </html>
    """

def get_webview_style():
    """Retorna el estilo para el componente WebView."""
    return """
        background-color: transparent;
    """