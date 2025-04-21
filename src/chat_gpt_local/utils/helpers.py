"""
Módulo de utilidades para funciones compartidas.
"""

import functools
import threading
import traceback
from typing import Any, Callable, TypeVar

T = TypeVar('T')


def run_in_thread(func: Callable[..., T]) -> Callable[..., None]:
    """
    Decorador para ejecutar una función en un hilo separado.
    
    Args:
        func: La función a ejecutar en un hilo
        
    Returns:
        La función decorada que ejecutará el código en un hilo
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> None:
        thread = threading.Thread(target=func, args=args, kwargs=kwargs)
        thread.daemon = True
        thread.start()
    
    return wrapper


def handle_errors(func: Callable[..., T]) -> Callable[..., T]:
    """
    Decorador para manejar errores de forma genérica.
    
    Args:
        func: La función que se quiere proteger
        
    Returns:
        La función decorada que captura las excepciones
    """
    @functools.wraps(func)
    def wrapper(*args: Any, **kwargs: Any) -> T:
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Error inesperado: {str(e)}")
            traceback.print_exc()
            raise
    
    return wrapper