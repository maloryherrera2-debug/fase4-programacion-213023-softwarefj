"""
Archivo: cliente.py
Descripción: Define la clase Cliente del sistema Software FJ.

Esta clase aplica encapsulamiento, validaciones robustas y manejo de
excepciones personalizadas para controlar errores en los datos del cliente.
"""

import re

from models.entidad import EntidadSistema
from exceptions.excepciones import (
    CampoObligatorioError,
    ClienteInvalidoError,
    CorreoInvalidoError,
    DocumentoInvalidoError,
    TelefonoInvalidoError,
)


class Cliente(EntidadSistema):
    """
    Clase que representa a un cliente del sistema Software FJ.

    Hereda de EntidadSistema y encapsula datos personales como correo,
    teléfono y estado del cliente.
    """

    def __init__(self, documento: str, nombre: str, correo: str, telefono: str):
        """
        Inicializa un cliente validando previamente sus datos.

        Args:
            documento (str): Número de identificación del cliente.
            nombre (str): Nombre completo del cliente.
            correo (str): Correo electrónico del cliente.
            telefono (str): Teléfono de contacto del cliente.

        Raises:
            ClienteInvalidoError: Si alguno de los datos no cumple las validaciones.
        """
        try:
            self._validar_campo_obligatorio(documento, "documento")
            self._validar_campo_obligatorio(nombre, "nombre")
            self._validar_campo_obligatorio(correo, "correo")
            self._validar_campo_obligatorio(telefono, "teléfono")

            self._validar_documento(documento)
            self._validar_nombre(nombre)
            self._validar_correo(correo)
            self._validar_telefono(telefono)

        except Exception as error:
            raise ClienteInvalidoError(
                f"No fue posible crear el cliente. Detalle: {error}"
            ) from error

        else:
            super().__init__(documento.strip(), nombre.strip().title())
            self.__correo = correo.strip().lower()
            self.__telefono = telefono.strip()
            self.__activo = True

    @property
    def correo(self):
        """
        Retorna el correo electrónico del cliente.
        """
        return self.__correo

    @correo.setter
    def correo(self, nuevo_correo: str):
        """
        Actualiza el correo electrónico del cliente, validando su formato.
        """
        try:
            self._validar_campo_obligatorio(nuevo_correo, "correo")
            self._validar_correo(nuevo_correo)

        except Exception as error:
            raise CorreoInvalidoError(
                f"No fue posible actualizar el correo. Detalle: {error}"
            ) from error

        else:
            self.__correo = nuevo_correo.strip().lower()

    @property
    def telefono(self):
        """
        Retorna el teléfono del cliente.
        """
        return self.__telefono

    @telefono.setter
    def telefono(self, nuevo_telefono: str):
        """
        Actualiza el teléfono del cliente, validando su formato.
        """
        try:
            self._validar_campo_obligatorio(nuevo_telefono, "teléfono")
            self._validar_telefono(nuevo_telefono)

        except Exception as error:
            raise TelefonoInvalidoError(
                f"No fue posible actualizar el teléfono. Detalle: {error}"
            ) from error

        else:
            self.__telefono = nuevo_telefono.strip()

    @property
    def activo(self):
        """
        Retorna el estado del cliente.
        """
        return self.__activo

    def activar(self):
        """
        Activa al cliente dentro del sistema.
        """
        self.__activo = True

    def desactivar(self):
        """
        Desactiva al cliente dentro del sistema.
        """
        self.__activo = False

    def actualizar_contacto(self, correo: str = None, telefono: str = None):
        """
        Actualiza los datos de contacto del cliente.

        Este método usa parámetros opcionales para simular una forma de
        sobrecarga en Python, permitiendo actualizar solo el correo,
        solo el teléfono o ambos datos.

        Args:
            correo (str, optional): Nuevo correo electrónico.
            telefono (str, optional): Nuevo teléfono.

        Returns:
            bool: True si la actualización fue exitosa.

        Raises:
            ClienteInvalidoError: Si los datos ingresados son inválidos.
        """
        try:
            if correo is None and telefono is None:
                raise CampoObligatorioError(
                    "Debe ingresar al menos un dato para actualizar."
                )

            if correo is not None:
                self.correo = correo

            if telefono is not None:
                self.telefono = telefono

        except Exception as error:
            raise ClienteInvalidoError(
                f"No fue posible actualizar los datos de contacto. Detalle: {error}"
            ) from error

        else:
            return True

        finally:
            # Bloque finally incluido para garantizar el cierre controlado
            # de la operación, incluso si ocurre un error.
            pass

    def mostrar_informacion(self):
        """
        Retorna la información general del cliente.

        Returns:
            dict: Diccionario con los datos principales del cliente.
        """
        return {
            "documento": self.identificador,
            "nombre": self.nombre,
            "correo": self.__correo,
            "telefono": self.__telefono,
            "activo": self.__activo,
        }

    @staticmethod
    def _validar_campo_obligatorio(valor: str, nombre_campo: str):
        """
        Valida que un campo obligatorio no esté vacío.
        """
        if valor is None or str(valor).strip() == "":
            raise CampoObligatorioError(f"El campo {nombre_campo} es obligatorio.")

    @staticmethod
    def _validar_documento(documento: str):
        """
        Valida que el documento contenga únicamente números y tenga una longitud adecuada.
        """
        documento = documento.strip()

        if not documento.isdigit():
            raise DocumentoInvalidoError("El documento solo debe contener números.")

        if len(documento) < 5 or len(documento) > 15:
            raise DocumentoInvalidoError(
                "El documento debe tener entre 5 y 15 dígitos."
            )

    @staticmethod
    def _validar_nombre(nombre: str):
        """
        Valida que el nombre tenga una longitud mínima y solo contenga letras y espacios.
        """
        nombre = nombre.strip()

        if len(nombre) < 3:
            raise ClienteInvalidoError("El nombre debe tener mínimo 3 caracteres.")

        patron_nombre = r"^[A-Za-zÁÉÍÓÚáéíóúÑñ\s]+$"

        if not re.match(patron_nombre, nombre):
            raise ClienteInvalidoError(
                "El nombre solo debe contener letras y espacios."
            )

    @staticmethod
    def _validar_correo(correo: str):
        """
        Valida el formato básico de un correo electrónico.
        """
        correo = correo.strip().lower()
        patron_correo = r"^[\w\.-]+@[\w\.-]+\.\w{2,}$"

        if not re.match(patron_correo, correo):
            raise CorreoInvalidoError("El correo electrónico no tiene un formato válido.")

    @staticmethod
    def _validar_telefono(telefono: str):
        """
        Valida que el teléfono tenga un formato aceptable.
        """
        telefono = telefono.strip()
        patron_telefono = r"^\+?[0-9\s\-]{7,20}$"

        if not re.match(patron_telefono, telefono):
            raise TelefonoInvalidoError(
                "El teléfono debe contener solo números, espacios, guiones o el signo +."
            )
