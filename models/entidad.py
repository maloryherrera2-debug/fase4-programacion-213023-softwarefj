"""
Archivo: entidad.py
Descripción: Define la clase abstracta base para las entidades del sistema Software FJ.
"""

from abc import ABC, abstractmethod


class EntidadSistema(ABC):
    """
    Clase abstracta que representa una entidad general del sistema.

    Esta clase sirve como base para otras clases como Cliente, Servicio o Reserva.
    Aplica el principio de abstracción porque define una estructura común,
    pero obliga a las clases hijas a implementar su propia forma de mostrar información.
    """

    def __init__(self, identificador: str, nombre: str):
        """
        Inicializa una entidad del sistema.

        Args:
            identificador (str): Código o documento que identifica la entidad.
            nombre (str): Nombre de la entidad.
        """
        self._identificador = identificador
        self._nombre = nombre

    @property
    def identificador(self):
        """
        Retorna el identificador de la entidad.
        """
        return self._identificador

    @property
    def nombre(self):
        """
        Retorna el nombre de la entidad.
        """
        return self._nombre

    @abstractmethod
    def mostrar_informacion(self):
        """
        Método abstracto que debe ser implementado por las clases hijas.
        """
        pass
