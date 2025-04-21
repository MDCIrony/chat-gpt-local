"""
Pruebas básicas para el cliente de OpenAI.
"""

import unittest
from unittest.mock import MagicMock, patch

from chat_gpt_local.api.openai_client import OpenAIClient


class TestOpenAIClient(unittest.TestCase):
    """Pruebas para el cliente OpenAI."""
    
    @patch('openai.OpenAI')
    def test_send_message(self, mock_openai_class):
        """Prueba que el método send_message funciona correctamente."""
        # Configurar el mock
        mock_client = MagicMock()
        mock_openai_class.return_value = mock_client
        
        # Configurar la respuesta simulada
        mock_response = MagicMock()
        mock_response.choices = [MagicMock()]
        mock_response.choices[0].message.content = "Respuesta simulada"
        mock_client.chat.completions.create.return_value = mock_response
        
        # Crear cliente y enviar mensaje
        client = OpenAIClient()
        response = client.send_message("Hola, cómo estás?")
        
        # Verificar que el mensaje se envió correctamente
        mock_client.chat.completions.create.assert_called_once()
        self.assertEqual(response, "Respuesta simulada")
    
    @patch('openai.OpenAI')
    def test_send_message_error(self, mock_openai_class):
        """Prueba que los errores se manejan correctamente."""
        # Configurar el mock para lanzar una excepción
        mock_client = MagicMock()
        mock_openai_class.return_value = mock_client
        mock_client.chat.completions.create.side_effect = Exception("Error de prueba")
        
        # Crear cliente
        client = OpenAIClient()
        
        # Verificar que la excepción se propaga correctamente
        with self.assertRaises(Exception) as context:
            client.send_message("Hola")
        
        self.assertIn("Error al comunicarse con OpenAI", str(context.exception))


if __name__ == '__main__':
    unittest.main()