# Chat GPT Local

Aplicación de escritorio con interfaz estilo ChatGPT integrada con la API de OpenAI. Presenta un diseño moderno con temática Cyberpunk.

## Características

- Interfaz de usuario moderna inspirada en ChatGPT con estilo Cyberpunk
- Integración con la API de OpenAI
- Soporte para renderizado de Markdown en las respuestas
- Efectos visuales de alta calidad (glitch, escaneo, etc.)
- Diseñado con prácticas modernas de Python 3.12

## Requisitos del Sistema

### Dependencias de Python
- Python 3.12 o superior

### Dependencias del Sistema
- **Qt 6**: La aplicación utiliza PyQt6, que requiere las bibliotecas Qt 6 instaladas en el sistema.

#### En Ubuntu/Debian:
```bash
sudo apt-get update
sudo apt-get install qt6-base-dev libqt6webenginewidgets6 libqt6webenginecore6 qt6-qpa-plugins
```

#### En Fedora:
```bash
sudo dnf install qt6-qtbase-devel qt6-qtwebengine-devel
```

#### En Arch Linux:
```bash
sudo pacman -S qt6-base qt6-webengine
```

#### En macOS (usando Homebrew):
```bash
brew install qt@6
```

## Instalación

1. Clona este repositorio:
```bash
git clone https://github.com/tuusuario/chat-gpt-local.git
cd chat-gpt-local
```

2. Asegúrate de tener Python 3.12 o superior instalado:
```bash
python --version
```

3. Instala el proyecto con sus dependencias:
```bash
pip install -e .
```

## Configuración

1. Crea un archivo `.env` en el directorio raíz del proyecto con el siguiente contenido:
```
OPENAI_API_KEY=tu_clave_api_aqui
OPENAI_MODEL=gpt-3.5-turbo  # Opcional, valor predeterminado: gpt-3.5-turbo
OPENAI_TEMPERATURE=0.7      # Opcional, valor predeterminado: 0.7
OPENAI_MAX_TOKENS=0         # Opcional, 0 significa sin límite
```

2. Obtén tu clave API de OpenAI en: [https://platform.openai.com/api-keys](https://platform.openai.com/api-keys)

## Uso

Hay dos formas de ejecutar la aplicación:

### Usando el comando instalado
Una vez instalado con pip, puedes ejecutar:
```bash
chat-gpt-local
```

### Usando el script run_app.py
Alternativamente, puedes ejecutar:
```bash
python run_app.py
```

## Desarrollo

### Preparación del Entorno de Desarrollo

1. Instala las dependencias de desarrollo:
```bash
pip install -e ".[dev]"
```

2. Compila los recursos Qt (necesario si modificas archivos en `src/chat_gpt_local/gui/resources/`):
```bash
python scripts/compile_resources.py
```

### Estructura del Proyecto

```
chat-gpt-local/
├── scripts/                # Scripts de utilidad
│   ├── compile_resources.py # Compila recursos Qt
│   └── generate_resources.py # Genera archivos de recursos
├── src/
│   └── chat_gpt_local/     # Código fuente principal
│       ├── api/            # Integración con API de OpenAI
│       ├── config/         # Configuración de la aplicación
│       ├── gui/            # Interfaz gráfica
│       │   ├── resources/  # Recursos (fuentes, imágenes)
│       │   └── styles/     # Estilos CSS para la interfaz
│       └── utils/          # Utilidades y helpers
├── tests/                  # Pruebas unitarias
└── pyproject.toml          # Configuración del proyecto
```

### Flujo de Desarrollo

1. **Modificar la interfaz**: Edita los archivos en `src/chat_gpt_local/gui/`
2. **Cambiar estilos**: Modifica los archivos en `src/chat_gpt_local/gui/styles/`
3. **Añadir recursos**: Coloca nuevos recursos en `src/chat_gpt_local/gui/resources/` y actualiza `resources.qrc`
4. **Compilar recursos**: Ejecuta `python scripts/compile_resources.py` después de modificar los recursos
5. **Pruebas**: Ejecuta `pytest` para ejecutar las pruebas

## Solución de Problemas

### Error: "No se han compilado los recursos"
Si ves el mensaje "No se encontraron recursos compilados", ejecuta:
```bash
python scripts/compile_resources.py
```

### Error: "No se pudo compilar los recursos"
Asegúrate de tener las herramientas de desarrollo de Qt 6 instaladas:
- Verifica que `pyrcc6`, `pyqt6-rcc` o `rcc` estén disponibles en tu sistema
- Instala las dependencias del sistema mencionadas en la sección "Requisitos del Sistema"

### Error: "No se ha configurado la clave API de OpenAI"
Verifica que:
- Has creado el archivo `.env` en el directorio raíz
- Has incluido la línea `OPENAI_API_KEY=tu_clave_api_aqui` con una clave API válida
- La clave API no está caducada o limitada

## Licencia

MIT