# Gestor de Finanzas

El **Gestor de Finanzas** es una aplicación de escritorio diseñada para ayudar a los usuarios a gestionar sus gastos e ingresos de manera efectiva. Con una interfaz minimalista y fácil de usar, permite a los usuarios agregar, editar y eliminar registros financieros, así como visualizar estadísticas clave.

## Características

- **Agregar Registros**: Permite agregar nuevos registros financieros, especificando la descripción, cantidad, tipo (gastos o ingresos) y la fecha.
- **Editar Registros**: Los usuarios pueden seleccionar y editar los registros existentes.
- **Eliminar Registros**: Los registros pueden ser eliminados individualmente o todos a la vez.
- **Visualización de Registros**: Muestra los registros en una tabla ordenada por fecha.
- **Estadísticas**: Calcula y muestra el total de gastos, ingresos y el balance neto.

## Requisitos

- Python 3.x
- Tkinter (incluido en la mayoría de las instalaciones de Python)
- `tkcalendar` para el widget de selección de fecha

## Instalación

1. Clona este repositorio:
    ```bash
    git clone https://github.com/tu_usuario/gestor-finanzas.git
    cd gestor-finanzas
    ```

2. Instala las dependencias necesarias:
    ```bash
    pip install tkcalendar
    ```

## Uso

1. Ejecuta la aplicación:
    ```bash
    python gestor_finanzas.py
    ```

2. La interfaz principal te permitirá agregar, editar y eliminar registros financieros.

## Archivos

- `gestor_finanzas.py`: Archivo principal que contiene el código de la aplicación.
- `datos.json`: Archivo donde se almacenan los registros financieros.

## Capturas de Pantalla

### Pantalla Principal
![Pantalla Principal](screenshots/pantalla_principal.png)
