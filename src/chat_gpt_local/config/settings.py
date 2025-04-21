"""
Módulo de configuración para gestionar las variables de entorno y configuración de la aplicación.
"""

import os
from pathlib import Path
from typing import Optional

import pydantic
from dotenv import load_dotenv


class Settings(pydantic.BaseModel):
    """Configuración de la aplicación."""
    
    openai_api_key: str
    model: str = "gpt-3.5-turbo"
    temperature: float = 0.7
    max_tokens: Optional[int] = None
    
    @classmethod
    def from_env(cls) -> "Settings":
        """Carga la configuración desde las variables de entorno."""
        # Intenta cargar desde .env si existe
        env_file = Path(".env")
        if env_file.exists():
            load_dotenv(env_file)
        
        return cls(
            openai_api_key=os.environ.get("OPENAI_API_KEY", ""),
            model=os.environ.get("OPENAI_MODEL", "gpt-3.5-turbo"),
            temperature=float(os.environ.get("OPENAI_TEMPERATURE", "0.7")),
            max_tokens=int(os.environ.get("OPENAI_MAX_TOKENS", "0")) or None,
        )

# Instancia global de la configuración
settings = Settings.from_env()