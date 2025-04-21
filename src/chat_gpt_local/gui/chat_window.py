"""
Módulo para la interfaz gráfica de usuario estilo ChatGPT con tema Cyberpunk.
"""

import random
from datetime import datetime
from typing import Any, Dict, List, Optional

import markdown
from PyQt6.QtCore import QObject, Qt, QTimer, pyqtSignal, pyqtSlot
from PyQt6.QtGui import QBrush, QColor, QFontDatabase, QLinearGradient, QPainter, QPen
from PyQt6.QtWebEngineWidgets import QWebEngineView
from PyQt6.QtWidgets import (
    QApplication,
    QFrame,
    QGraphicsDropShadowEffect,
    QHBoxLayout,
    QLabel,
    QMainWindow,
    QMessageBox,
    QPushButton,
    QScrollArea,
    QSizePolicy,
    QTextEdit,
    QVBoxLayout,
    QWidget,
)

from chat_gpt_local.api.openai_client import OpenAIClient
from chat_gpt_local.gui.styles.base import COLORS, FONT_FILES
from chat_gpt_local.gui.styles.effects import (
    get_glitch_effect_colors,
    get_scan_effect_config,
)
from chat_gpt_local.gui.styles.main_window import (
    get_header_styles,
    get_input_area_styles,
    get_main_window_style,
    get_scroll_area_styles,
)
from chat_gpt_local.gui.styles.message import (
    get_avatar_style,
    get_html_template,
    get_markdown_css_template,
    get_message_frame_style,
    get_role_label_style,
    get_time_label_style,
    get_webview_style,
)
from chat_gpt_local.utils.helpers import run_in_thread


class SignalBus(QObject):
    """Clase para manejar señales entre hilos."""
    response_received = pyqtSignal(str)
    error_occurred = pyqtSignal(str)


class CyberpunkGlitchEffect(QWidget):
    """Clase para crear un efecto de 'glitch' estilo cyberpunk como fondo decorativo."""
    
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.setAttribute(Qt.WidgetAttribute.WA_NoSystemBackground)
        self.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        
        # Configuración de líneas glitch
        self.glitch_lines = []
        self.regen_timer = QTimer(self)
        self.regen_timer.timeout.connect(self.regenerate_glitch)
        self.regen_timer.start(2000)  # Regenerar cada 2 segundos
        self.regenerate_glitch()
    
    def regenerate_glitch(self):
        """Regenera las líneas de 'glitch' para crear animación."""
        self.glitch_lines = []
        glitch_colors = get_glitch_effect_colors()
        
        for _ in range(random.randint(3, 8)):
            pos_y = random.randint(0, self.height())
            length = random.randint(20, 100)
            opacity = random.uniform(0.1, 0.3)
            color_choice = random.choice(glitch_colors)
            self.glitch_lines.append((pos_y, length, opacity, color_choice))
        self.update()
    
    def paintEvent(self, event):
        """Dibuja el efecto de glitch en el widget."""
        painter = QPainter(self)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        for pos_y, length, opacity, color in self.glitch_lines:
            pen = QPen(QColor(color))
            pen.setWidth(1)
            painter.setOpacity(opacity)
            painter.setPen(pen)
            painter.drawLine(0, pos_y, length, pos_y)


class MessageWidget(QFrame):
    """Widget para mostrar un mensaje en el chat con soporte para Markdown."""
    
    def __init__(
        self, 
        content: str, 
        is_user: bool = False, 
        parent: Optional[QWidget] = None
    ) -> None:
        """
        Inicializa el widget de mensaje.
        
        Args:
            content: El contenido del mensaje
            is_user: Si el mensaje es del usuario o del asistente
            parent: Widget padre
        """
        super().__init__(parent)
        self.setFrameShape(QFrame.Shape.StyledPanel)
        self.setLineWidth(1)
        
        # Aplicar estilo según si es usuario o asistente
        self.setStyleSheet(get_message_frame_style(is_user))
        
        # Efecto de sombra para un aspecto más cyberpunk
        glow_color = COLORS["accent_cyan"] if is_user else COLORS["accent_magenta"]
        glow = QGraphicsDropShadowEffect(self)
        glow.setColor(QColor(glow_color))
        glow.setOffset(0, 0)
        glow.setBlurRadius(15)
        self.setGraphicsEffect(glow)
        
        layout = QVBoxLayout(self)
        layout.setSpacing(8)
        
        # Cabecera con avatar y rol
        header_layout = QHBoxLayout()
        
        # Determinar texto para avatar y rol
        role_text = "Usuario" if is_user else "Asistente"
        
        # Avatar (círculo con iniciales)
        avatar_widget = QWidget()
        avatar_widget.setFixedSize(30, 30)
        avatar_widget.setStyleSheet(get_avatar_style(is_user))
        
        # Efecto de sombra para el avatar
        avatar_glow = QGraphicsDropShadowEffect(avatar_widget)
        avatar_glow.setColor(QColor(glow_color))
        avatar_glow.setOffset(0, 0)
        avatar_glow.setBlurRadius(10)
        avatar_widget.setGraphicsEffect(avatar_glow)
        
        avatar_layout = QHBoxLayout(avatar_widget)
        avatar_layout.setContentsMargins(0, 0, 0, 0)
        avatar_label = QLabel(role_text[0].upper())
        avatar_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        avatar_layout.addWidget(avatar_label)
        header_layout.addWidget(avatar_widget)
        
        # Etiqueta con el rol
        role_label = QLabel(role_text.upper())
        role_label.setStyleSheet(get_role_label_style(is_user))
        header_layout.addWidget(role_label)
        header_layout.addStretch()
        
        # Información de la hora con estilo cyberpunk
        time_label = QLabel(datetime.now().strftime("%H:%M"))
        time_label.setStyleSheet(get_time_label_style(is_user))
        header_layout.addWidget(time_label)
        
        layout.addLayout(header_layout)
        
        # Contenido del mensaje con soporte para Markdown
        # Convertir Markdown a HTML
        html_content = markdown.markdown(content, extensions=['fenced_code', 'tables', 'nl2br'])
        
        # Obtener la plantilla CSS y formatearla con el color correspondiente
        avatar_color = COLORS["accent_cyan"] if is_user else COLORS["accent_magenta"]
        css_styles = get_markdown_css_template().format(avatar_color=avatar_color)
        
        # Aplicar la plantilla HTML completa
        styled_html = get_html_template().format(
            css_styles=css_styles,
            html_content=html_content
        )
        
        # Usar QWebEngineView para renderizar HTML
        web_view = QWebEngineView()
        web_view.setHtml(styled_html)
        web_view.setMinimumHeight(100)
        web_view.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        web_view.setStyleSheet(get_webview_style())
        
        layout.addWidget(web_view)
        
        # Agregar efecto de glitch en el fondo (sutil, solo decorativo)
        if not is_user:  # Solo para mensajes del asistente
            glitch_effect = CyberpunkGlitchEffect(self)
            glitch_effect.setGeometry(self.rect())
            glitch_effect.lower()  # Enviar al fondo


class ChatWindow(QMainWindow):
    """Ventana principal de la aplicación de chat con tema Cyberpunk."""
    
    def __init__(self) -> None:
        """Inicializa la ventana principal de la aplicación."""
        super().__init__()
        
        self.setWindowTitle("Cyber-GPT")
        self.setGeometry(100, 100, 900, 700)
        self.setMinimumSize(700, 500)
        
        # Cargar y establecer fuentes personalizadas
        self._load_fonts()
        
        # Configurar estilo cyberpunk centralizado
        self.setStyleSheet(get_main_window_style())
        
        # Inicializar cliente OpenAI
        self.openai_client = OpenAIClient()
        
        # Inicializar bus de señales
        self.signal_bus = SignalBus()
        self.signal_bus.response_received.connect(self._handle_response)
        self.signal_bus.error_occurred.connect(self._handle_error)
        
        # Historial de mensajes
        self.messages: List[Dict[str, Any]] = []
        
        # Construir la interfaz
        self._setup_ui()
        
        # Iniciar efecto de escaneo
        self._setup_scan_effect()
    
    def _load_fonts(self) -> None:
        """Cargar fuentes personalizadas."""
        # Configuración para cargar fuentes (en aplicaciones reales, se cargarían desde archivos)
        # En este ejemplo simulamos que ya están instaladas en el sistema
        # Para una aplicación completa, debería incluir las fuentes como recursos
        for font_path in FONT_FILES.values():
            QFontDatabase.addApplicationFont(font_path)
    
    def _setup_scan_effect(self) -> None:
        """Configura el efecto de escaneo horizontal (línea que sube y baja)."""
        self.scan_effect = QWidget(self)
        self.scan_effect.setGeometry(0, 0, self.width(), self.height())
        self.scan_effect.setAttribute(Qt.WidgetAttribute.WA_TransparentForMouseEvents)
        self.scan_effect.setAttribute(Qt.WidgetAttribute.WA_NoSystemBackground)
        self.scan_effect.setAttribute(Qt.WidgetAttribute.WA_TranslucentBackground)
        self.scan_effect.lower()
        
        # Obtener la configuración del efecto de escaneo
        self.scan_config = get_scan_effect_config()
        
        self.scan_line_pos = 0
        self.scan_direction = 1  # 1 = hacia abajo, -1 = hacia arriba
        
        self.scan_timer = QTimer(self)
        self.scan_timer.timeout.connect(self._update_scan_line)
        self.scan_timer.start(self.scan_config["update_interval"])
        
        self.scan_effect.paintEvent = self._paint_scan_effect
        self.scan_effect.show()
    
    def _update_scan_line(self) -> None:
        """Actualiza la posición de la línea de escaneo."""
        self.scan_line_pos += self.scan_direction * self.scan_config["speed"]
        
        if self.scan_line_pos >= self.height():
            self.scan_line_pos = self.height()
            self.scan_direction = -1
        elif self.scan_line_pos <= 0:
            self.scan_line_pos = 0
            self.scan_direction = 1
            
        self.scan_effect.update()
    
    def _paint_scan_effect(self, event) -> None:
        """Dibuja el efecto de escaneo."""
        painter = QPainter(self.scan_effect)
        painter.setRenderHint(QPainter.RenderHint.Antialiasing)
        
        # Dibujar línea de escaneo horizontal
        gradient = QLinearGradient(0, self.scan_line_pos - 5, self.width(), self.scan_line_pos + 5)
        gradient.setColorAt(0, QColor(self.scan_config["line_color"][0], self.scan_config["line_color"][1], self.scan_config["line_color"][2], 0))
        gradient.setColorAt(0.5, QColor(self.scan_config["line_color"][0], self.scan_config["line_color"][1], self.scan_config["line_color"][2], self.scan_config["gradient_opacity"]))
        gradient.setColorAt(1, QColor(self.scan_config["line_color"][0], self.scan_config["line_color"][1], self.scan_config["line_color"][2], 0))
        
        painter.setBrush(QBrush(gradient))
        painter.setPen(Qt.PenStyle.NoPen)
        painter.drawRect(0, self.scan_line_pos - 5, self.width(), 10)
        
        # Dibujar línea central más brillante
        pen = QPen(QColor(self.scan_config["line_color"][0], self.scan_config["line_color"][1], self.scan_config["line_color"][2], self.scan_config["line_opacity"]))
        pen.setWidth(1)
        painter.setPen(pen)
        painter.drawLine(0, self.scan_line_pos, self.width(), self.scan_line_pos)
    
    def resizeEvent(self, event) -> None:
        """Maneja el evento de redimensionamiento de la ventana."""
        super().resizeEvent(event)
        if hasattr(self, 'scan_effect'):
            self.scan_effect.setGeometry(0, 0, self.width(), self.height())
    
    def _setup_ui(self) -> None:
        """Configurar los elementos de la interfaz de usuario."""
        # Widget principal
        main_widget = QWidget()
        main_layout = QVBoxLayout(main_widget)
        main_layout.setContentsMargins(25, 25, 25, 25)
        main_layout.setSpacing(20)
        
        # Cabecera con título y efecto cyberpunk
        header_widget = QWidget()
        header_widget.setFixedHeight(60)
        header_layout = QHBoxLayout(header_widget)
        header_layout.setContentsMargins(0, 0, 0, 10)
        
        # Obtener estilos de encabezado centralizado
        header_styles = get_header_styles()
        
        # Título con efecto de resplandor
        title_label = QLabel("CYBER-GPT")
        title_label.setStyleSheet(header_styles["title"])
        
        title_glow = QGraphicsDropShadowEffect(title_label)
        title_glow.setColor(QColor(COLORS["accent_cyan"]))
        title_glow.setOffset(0, 0)
        title_glow.setBlurRadius(20)
        title_label.setGraphicsEffect(title_glow)
        
        header_layout.addWidget(title_label)
        header_layout.addStretch()
        
        # Etiqueta decorativa "NEURAL LINK ACTIVE"
        status_label = QLabel("NEURAL LINK ACTIVE")
        status_label.setStyleSheet(header_styles["status"])
        
        status_glow = QGraphicsDropShadowEffect(status_label)
        status_glow.setColor(QColor(COLORS["accent_green"]))
        status_glow.setOffset(0, 0)
        status_glow.setBlurRadius(10)
        status_label.setGraphicsEffect(status_glow)
        
        header_layout.addWidget(status_label)
        
        # Etiqueta tipo "modo cyberpunk"
        mode_label = QLabel("MODO CYBERPUNK")
        mode_label.setStyleSheet(header_styles["mode"])
        
        mode_glow = QGraphicsDropShadowEffect(mode_label)
        mode_glow.setColor(QColor(COLORS["accent_magenta"]))
        mode_glow.setOffset(0, 0)
        mode_glow.setBlurRadius(10)
        mode_label.setGraphicsEffect(mode_glow)
        
        header_layout.addWidget(mode_label)
        
        main_layout.addWidget(header_widget)
        
        # Área de mensajes con fondo estilo cyberpunk
        self.messages_area = QWidget()
        self.messages_layout = QVBoxLayout(self.messages_area)
        self.messages_layout.setAlignment(Qt.AlignmentFlag.AlignTop)
        self.messages_layout.setSpacing(20)
        self.messages_layout.setContentsMargins(5, 5, 5, 5)
        
        # Obtener estilos de área de desplazamiento
        scroll_styles = get_scroll_area_styles()
        
        # Área de desplazamiento con efecto de borde brillante
        scroll_container = QFrame()
        scroll_container.setFrameShape(QFrame.Shape.StyledPanel)
        scroll_container.setStyleSheet(scroll_styles["container"])
        
        scroll_glow = QGraphicsDropShadowEffect(scroll_container)
        scroll_glow.setColor(QColor(COLORS["accent_cyan"]))
        scroll_glow.setOffset(0, 0)
        scroll_glow.setBlurRadius(15)
        scroll_container.setGraphicsEffect(scroll_glow)
        
        scroll_layout = QVBoxLayout(scroll_container)
        scroll_layout.setContentsMargins(1, 1, 1, 1)
        scroll_layout.setSpacing(0)
        
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setWidget(self.messages_area)
        scroll_area.setStyleSheet(scroll_styles["scrollarea"])
        
        # Mejorar adaptabilidad vertical
        scroll_area.setSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        scroll_layout.addWidget(scroll_area)
        
        main_layout.addWidget(scroll_container, 1)
        
        # Obtener estilos del área de entrada
        input_styles = get_input_area_styles()
        
        # Área de entrada con diseño cyberpunk mejorado
        input_container = QFrame()
        input_container.setStyleSheet(input_styles["container"])
        
        input_glow = QGraphicsDropShadowEffect(input_container)
        input_glow.setColor(QColor(COLORS["accent_cyan"]))
        input_glow.setOffset(0, 0)
        input_glow.setBlurRadius(15)
        input_container.setGraphicsEffect(input_glow)
        
        input_container_layout = QVBoxLayout(input_container)
        input_container_layout.setContentsMargins(1, 1, 1, 1)
        input_container_layout.setSpacing(0)
        
        input_frame = QFrame()
        input_frame.setStyleSheet(input_styles["frame"])
        
        input_layout = QHBoxLayout(input_frame)
        input_layout.setContentsMargins(15, 15, 15, 15)
        input_layout.setSpacing(15)
        
        # Etiqueta de entrada al estilo terminal
        input_prefix = QLabel("[ MENSAJE ]")
        input_prefix.setStyleSheet(input_styles["prefix"])
        input_prefix.setFixedWidth(100)
        input_prefix.setAlignment(Qt.AlignmentFlag.AlignCenter)
        input_layout.addWidget(input_prefix)
        
        # Campo de texto mejorado
        self.message_input = QTextEdit()
        self.message_input.setPlaceholderText("Escribe un mensaje...")
        self.message_input.setStyleSheet(input_styles["input"])
        self.message_input.setMinimumHeight(50)
        self.message_input.setMaximumHeight(100)
        self.message_input.textChanged.connect(self._on_input_changed)
        input_layout.addWidget(self.message_input, 1)
        
        # Botón de envío mejorado
        self.send_button = QPushButton("ENVIAR")
        self.send_button.setStyleSheet(input_styles["send_button"])
        
        # Efecto de resplandor para el botón
        send_glow = QGraphicsDropShadowEffect(self.send_button)
        send_glow.setColor(QColor(COLORS["accent_magenta"]))
        send_glow.setOffset(0, 0)
        send_glow.setBlurRadius(15)
        self.send_button.setGraphicsEffect(send_glow)
        
        self.send_button.clicked.connect(self._send_message)
        self.send_button.setDisabled(True)
        self.send_button.setFixedWidth(140)
        input_layout.addWidget(self.send_button)
        
        input_container_layout.addWidget(input_frame)
        main_layout.addWidget(input_container)
        
        # Asignar el widget principal a la ventana
        self.setCentralWidget(main_widget)
        
        # Mensaje de bienvenida con contenido cyberpunk mejorado
        welcome_message = """
# Bienvenido al Sistema Cyber-GPT v2.0

Has establecido conexión con la **interfaz neural** del asistente Cyber-GPT. Este sistema utiliza tecnología de _procesamiento de lenguaje avanzado_ para interactuar con humanos.

**Protocolos de interacción:**
* Comunicación en lenguaje natural con formato Markdown
* Optimización de visualización para código y datos
* Adaptación dinámica de respuestas según contexto

```python
# Sistema inicializado correctamente
def night_city_protocol():
    connect_neural_interface()
    print("Conexión neural establecida. Bienvenido a Night City.")
    return STATUS_ONLINE
```

> Los sistemas están operativos y listos. ¿En qué puedo asistirte hoy?
"""
        self._add_message(welcome_message, is_user=False)
    
    def _on_input_changed(self) -> None:
        """Maneja cambios en el campo de texto."""
        has_text = bool(self.message_input.toPlainText().strip())
        self.send_button.setEnabled(has_text)
    
    def _send_message(self) -> None:
        """Envía el mensaje del usuario al chatbot."""
        message = self.message_input.toPlainText().strip()
        if not message:
            return
        
        # Limpiar el campo de entrada
        self.message_input.clear()
        self.send_button.setDisabled(True)
        
        # Agregar mensaje del usuario a la interfaz
        self._add_message(message, is_user=True)
        
        # Enviar mensaje a OpenAI en un hilo separado
        self._send_to_openai(message)
    
    @run_in_thread
    def _send_to_openai(self, message: str) -> None:
        """
        Envía el mensaje a OpenAI en un hilo separado.
        
        Args:
            message: El mensaje del usuario
        """
        try:
            response = self.openai_client.send_message(message)
            self.signal_bus.response_received.emit(response)
        except Exception as e:
            self.signal_bus.error_occurred.emit(str(e))
    
    @pyqtSlot(str)
    def _handle_response(self, response: str) -> None:
        """
        Maneja la respuesta recibida de OpenAI.
        
        Args:
            response: La respuesta del asistente
        """
        self._add_message(response, is_user=False)
    
    @pyqtSlot(str)
    def _handle_error(self, error_message: str) -> None:
        """
        Maneja errores en la comunicación con OpenAI.
        
        Args:
            error_message: El mensaje de error
        """
        QMessageBox.critical(self, "Error", f"Error: {error_message}")
    
    def _add_message(self, content: str, is_user: bool = False) -> None:
        """
        Añade un mensaje al chat.
        
        Args:
            content: El contenido del mensaje
            is_user: Si el mensaje es del usuario o del asistente
        """
        # Guardar mensaje en el historial
        self.messages.append({
            "role": "user" if is_user else "assistant",
            "content": content,
            "timestamp": datetime.now()
        })
        
        # Crear widget de mensaje
        message_widget = MessageWidget(content, is_user, self)
        self.messages_layout.addWidget(message_widget)
        
        # Desplazarse hacia abajo para mostrar el mensaje más reciente
        QApplication.processEvents()
        scroll_area = self.messages_area.parent()
        if isinstance(scroll_area, QScrollArea):
            scrollbar = scroll_area.verticalScrollBar()
            scrollbar.setValue(scrollbar.maximum())