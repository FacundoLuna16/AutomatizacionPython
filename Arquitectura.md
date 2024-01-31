# Documentación de la Arquitectura de Testing en Python

## Estructura del Proyecto

El proyecto está organizado en varias carpetas, cada una con un propósito específico:

- **.pytest_cache:** Esta carpeta almacena archivos de caché generados por pytest.

- **autoTest:** Carpeta creada al configurar el entorno virtual con venv.

- **config:** Contiene archivos de configuración para la automatización de pruebas.

- **img:** Almacena imágenes relacionadas con el proyecto o a la documentacion.

- **pages:** Contiene archivos que representan las páginas o componentes a probar.

- **reports:** Aquí se generarán los informes de las pruebas realizadas.

- **test:** Contiene los casos de prueba.

- **utils:** Carpeta para utilidades y funciones auxiliares.

## Archivos Importantes

- **.gitignore:** Especifica los archivos y carpetas que deben ser ignorados por el sistema de control de versiones Git.

- **pytest.ini:** Archivo de configuración para pytest.

- **README.md:** Documentación principal del proyecto.

- **requirements.txt:** Lista de dependencias del proyecto.

## Instrucciones para Configuración

1. Crear un entorno virtual con venv:

   ```bash
   python -m venv venv




- > Documentacion sobre Pytest-Html [Aqui](https://pytest-html.readthedocs.io/en/latest/user_guide.html#ansi-codes)

- > Documentacion sobre Hook en Pytest [Aqui](https://pytest.org/en/7.4.x/how-to/writing_plugins.html#pytest-hook-reference) !IMPORTANTE! para entender conftest.py