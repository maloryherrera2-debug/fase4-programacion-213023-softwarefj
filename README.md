# fase4-programacion-213023-softwarefj
Sistema Integral de Gestión de Clientes, Servicios y Reservas - Fase 4 Programación 213023

# Sistema Integral de Gestión de Clientes, Servicios y Reservas - Software FJ

## Curso

Programación - Código 213023
Fase 4 - Componente práctico - Prácticas simuladas

## Descripción general

Este proyecto corresponde al desarrollo de un sistema integral orientado a objetos para la empresa Software FJ, enfocado en la gestión de clientes, servicios y reservas. El sistema se construye en Python, sin uso de bases de datos, utilizando clases, objetos, listas internas y archivos de registro para eventos y errores.

El objetivo principal es implementar una aplicación estable, modular y extensible, aplicando principios de programación orientada a objetos como abstracción, herencia, polimorfismo, encapsulamiento y manejo avanzado de excepciones.

## Avance del Integrante 1 (Malory Herrera)

El avance desarrollado en esta rama corresponde a la estructura inicial del sistema y a la gestión de clientes.

### Archivos implementados

* `exceptions/excepciones.py`: contiene las excepciones personalizadas del sistema.
* `models/entidad.py`: contiene la clase abstracta `EntidadSistema`.
* `models/cliente.py`: contiene la clase `Cliente`, con validaciones robustas y encapsulamiento.
* `tests/pruebas_cliente.py`: contiene pruebas iniciales para validar clientes correctos e incorrectos.

## Funcionalidades implementadas

* Creación de una clase abstracta general.
* Implementación de la clase `Cliente`.
* Validación de campos obligatorios.
* Validación de documento, nombre, correo y teléfono.
* Encapsulamiento de datos personales.
* Uso de propiedades `@property` y setters.
* Implementación de excepciones personalizadas.
* Uso de bloques `try/except`, `try/except/else` y `try/finally`.
* Encadenamiento de excepciones mediante `raise ... from error`.
* Pruebas con datos válidos e inválidos.

## Pruebas incluidas

El archivo `tests/pruebas_cliente.py` permite probar los siguientes casos:

1. Creación de cliente válido.
2. Creación de cliente con nombre vacío.
3. Creación de cliente con correo inválido.
4. Creación de cliente con documento inválido.

## Organización del trabajo colaborativo sugerida

* Integrante 1: clase abstracta general, clase Cliente, validaciones, encapsulamiento y excepciones asociadas al cliente.
* Integrante 2: clase abstracta Servicio y estructura general de servicios.
* Integrante 3: servicios especializados: reserva de salas, alquiler de equipos y asesoría especializada.
* Integrante 4: clase Reserva, estados, confirmación, cancelación y procesamiento.
* Integrante 5: interfaz en Tkinter, simulaciones, logs y documentación final.

## Ejecución de pruebas

Para ejecutar las pruebas iniciales desde la raíz del proyecto:

```bash
python tests/pruebas_cliente.py
```

## Estado del proyecto

En desarrollo.
