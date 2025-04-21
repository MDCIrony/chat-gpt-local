"""
Módulo para la integración con la API de OpenAI.
"""


import openai
from openai.types.chat import ChatCompletion

from chat_gpt_local.config.settings import settings


class OpenAIClient:
    """Cliente para la API de OpenAI."""

    def __init__(self) -> None:
        """Inicializa el cliente con la clave API de la configuración."""
        self.client = openai.OpenAI(api_key=settings.openai_api_key)
        self.model = settings.model
        self.temperature = settings.temperature
        self.max_tokens = settings.max_tokens

    def send_message(self, message: str) -> str:
        """
        Envía un mensaje a la API de OpenAI y devuelve la respuesta.
        
        Args:
            message: El mensaje del usuario
            
        Returns:
            La respuesta del modelo de OpenAI
            
        Raises:
            Exception: Si hay un error en la comunicación con la API
        """
        try:
            response: ChatCompletion = self.client.chat.completions.create(
                model=self.model,
                messages=[
                    {"role": "user", "content": message}
                ],
                temperature=self.temperature,
                max_tokens=self.max_tokens,
            )
            return response.choices[0].message.content or ""
        except Exception as e:
            raise Exception(f"Error al comunicarse con OpenAI: {str(e)}") from e