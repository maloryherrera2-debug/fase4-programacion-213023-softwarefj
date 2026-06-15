"""
Archivo: pruebas_cliente.py
Descripción: Pruebas iniciales para validar el funcionamiento de la clase Cliente.
Estas pruebas demuestran el manejo de datos válidos e inválidos.
"""

from models.cliente import Cliente
from exceptions.excepciones import ClienteInvalidoError


def probar_cliente_valido():
    """
    Prueba la creación de un cliente con datos correctos.
    """
    try:
        cliente = Cliente(
            documento="123456789",
            nombre="Malory Herrera",
            correo="malory@example.com",
            telefono="3101234567"
        )

    except ClienteInvalidoError as error:
        print(f"Error al crear cliente válido: {error}")

    else:
        print("Cliente válido creado correctamente.")
        print(cliente.mostrar_informacion())

    finally:
        print("Finalizó la prueba de cliente válido.\n")


def probar_cliente_sin_nombre():
    """
    Prueba la creación de un cliente con nombre vacío.
    """
    try:
        cliente = Cliente(
            documento="123456789",
            nombre="",
            correo="malory@example.com",
            telefono="3101234567"
        )

    except ClienteInvalidoError as error:
        print(f"Error controlado: {error}")

    else:
        print("Cliente creado:", cliente.mostrar_informacion())

    finally:
        print("Finalizó la prueba de cliente sin nombre.\n")


def probar_cliente_correo_invalido():
    """
    Prueba la creación de un cliente con correo inválido.
    """
    try:
        cliente = Cliente(
            documento="123456789",
            nombre="Malory Herrera",
            correo="correo_invalido",
            telefono="3101234567"
        )

    except ClienteInvalidoError as error:
        print(f"Error controlado: {error}")

    else:
        print("Cliente creado:", cliente.mostrar_informacion())

    finally:
        print("Finalizó la prueba de cliente con correo inválido.\n")


def probar_cliente_documento_invalido():
    """
    Prueba la creación de un cliente con documento inválido.
    """
    try:
        cliente = Cliente(
            documento="ABC123",
            nombre="Malory Herrera",
            correo="malory@example.com",
            telefono="3101234567"
        )

    except ClienteInvalidoError as error:
        print(f"Error controlado: {error}")

    else:
        print("Cliente creado:", cliente.mostrar_informacion())

    finally:
        print("Finalizó la prueba de cliente con documento inválido.\n")


if __name__ == "__main__":
    probar_cliente_valido()
    probar_cliente_sin_nombre()
    probar_cliente_correo_invalido()
    probar_cliente_documento_invalido()
