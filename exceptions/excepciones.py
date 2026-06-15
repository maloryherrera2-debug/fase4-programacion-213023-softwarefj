"""
Archivo: excepciones.py
Descripción: Define las excepciones personalizadas del sistema Software FJ.
Estas excepciones permiten controlar errores sin detener la aplicación.
"""


class SistemaGestionError(Exception):
    """
    Excepción base para todos los errores personalizados del sistema.
    Sirve como clase general para agrupar los errores propios de la aplicación.
    """

    pass


class CampoObligatorioError(SistemaGestionError):
    """
    Se genera cuando un campo requerido está vacío o no fue proporcionado.
    """

    pass


class ClienteInvalidoError(SistemaGestionError):
    """
    Se genera cuando los datos generales del cliente no cumplen las validaciones.
    """

    pass


class DocumentoInvalidoError(ClienteInvalidoError):
    """
    Se genera cuando el documento del cliente tiene un formato incorrecto.
    """

    pass


class CorreoInvalidoError(ClienteInvalidoError):
    """
    Se genera cuando el correo electrónico del cliente no tiene un formato válido.
    """

    pass


class TelefonoInvalidoError(ClienteInvalidoError):
    """
    Se genera cuando el teléfono del cliente contiene datos inválidos.
    """

    pass


class OperacionNoPermitidaError(SistemaGestionError):
    """
    Se genera cuando el sistema intenta ejecutar una operación no permitida.
    """

    pass
