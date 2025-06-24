# SWAG_LABS - Automatización de Pruebas con Playwright y Python

[![GitHub Workflow Status](https://img.shields.io/github/actions/workflow/status/tu-usuario/SWAG_LABS/playwright.yml?branch=main&label=CI%20Tests)](https://github.com/raizengod/Playwright-Python_Swag-Labs.git)

## 🚀 Descripción del Proyecto

Este proyecto es una suite de automatización de pruebas para la aplicación web **Swag Labs**, una tienda de comercio electrónico ficticia. Desarrollado como parte de mi portafolio, demuestra mi capacidad para diseñar, implementar y mantener pruebas automatizadas robustas y eficientes utilizando **Playwright** con **Python**. El objetivo principal es asegurar la funcionalidad crítica de la aplicación, desde el inicio de sesión hasta la gestión del carrito de compras y la visualización de productos.

**Repositorio:** [https://github.com/tu-usuario/SWAG_LABS](https://github.com/raizengod/Playwright-Python_Swag-Labs.git)

## 🛠️ Tecnologías Utilizadas

* **Playwright**: Framework de automatización de navegadores para pruebas end-to-end.
* **Python**: Lenguaje de programación utilizado para escribir los scripts de prueba.
* **Pytest**: Framework de pruebas para Python, utilizado para organizar y ejecutar los tests.
* **GitHub Actions**: Para la integración continua (CI) y la ejecución automatizada de pruebas.

## 📂 Estructura del Proyecto

La estructura del proyecto está diseñada para ser modular, escalable y fácil de mantener, siguiendo las mejores prácticas en automatización de pruebas:

```
SWAG_LABS/
├── .github/
│   └── workflows/
│       └── playwright.yml         # Configuración de GitHub Actions para CI
├── mv_Swag_Labs/
├──  swag_labs/                 # Contenedor principal del código fuente
│    ├── pages/                 # Implementación del Page Object Model (POM)
│    │   ├── __init__.py
│    │   ├── base_page.py       # Clase base con funciones globales
│    │   ├── login_page.py      # Ejemplo de Page Object para Login (si existe)
│    │   ├── home_page.py       # Ejemplo de Page Object para Home (si existe)
│    │   └── cart_page.py       # Ejemplo de Page Object para Carrito (si existe)
│    ├── selectores/            # Centralización de selectores de elementos web
│    │   ├── __init__.py
│    │   ├── selectorCarrito.py
│    │   ├── selectorHome.py
│    │   ├── selectorLogin.py
│    │   ├── selectorMenu.py
│    │   └── selectorProducto.py
│    └── test/                  # Archivos de pruebas Pytest
│        ├── evidencia/         # Directorio para capturas de pantalla/videos de evidencia
│        ├── __init__.py
│        ├── conftest.py        # Configuración global de Pytest, fixtures
│        ├── test_carrito.py    # Pruebas relacionadas con el carrito de compras
│        ├── test_home.py       # Pruebas de la página de inicio
│        ├── test_login.py      # Pruebas de la funcionalidad de inicio de sesión
│        ├── test_menu.py       # Pruebas del menú de navegación (si existe)
│        └── test_producto.py   # Pruebas de la visualización y detalles de productos (si existe)
├── .gitignore                     # Archivo para ignorar archivos y directorios en Git
└── requirements.txt               # Dependencias del proyecto
```


### Explicación y Ejemplos de Archivos Clave:

* **`pages/`**: Implementa el patrón Page Object Model (POM). Cada archivo dentro de esta carpeta representa una página o componente principal de la aplicación web. Esto mejora la legibilidad, la reutilización del código y la mantenibilidad al encapsular los elementos de la UI y las interacciones.

    * **`base_page.py`**:
        Esta clase (`Funciones_Globales`) proporciona la funcionalidad base para todas las Page Objects, incluyendo la inicialización del objeto `Page` de Playwright y métodos comunes para interacción y aserciones.

* **`selectores/`**: Contiene archivos Python que centralizan los selectores de los elementos web. Separar los selectores de la lógica de las páginas permite una fácil actualización si la interfaz de usuario cambia, sin afectar directamente la lógica de las pruebas.

    * **`selectorLogin.py`**:
        Define los selectores para los elementos de la página de inicio de sesión.

    * **`selectorCarrito.py`**:
        Define selectores para los elementos relacionados con el carrito de compras.

* **`test/`**: Aquí se encuentran los archivos de prueba que utilizan Pytest. Cada archivo se enfoca en probar una característica específica de la aplicación, como el inicio de sesión, el carrito de compras, etc.

    * **`conftest.py`**:
        Este archivo contiene fixtures de Pytest que son compartidas a través de múltiples pruebas. Aquí se configura el navegador de Playwright para cada prueba y se inicializan las Page Objects o clases de selectores.

    * **`test_login.py`**:
        Un ejemplo de un archivo de prueba para la funcionalidad de inicio de sesión, mostrando casos de éxito y de fallo.

    * **`test_carrito.py`**:
        Un ejemplo de un archivo de prueba para la funcionalidad del carrito de compras.

    * **`test_home.py`**:
        Un ejemplo de un archivo de prueba para la funcionalidad de la página de inicio.

## 🚀 Ejecución de las Pruebas

Para ejecutar las pruebas localmente, sigue los siguientes pasos:

1.  **Clonar el repositorio:**
    ```bash
    git clone https://github.com/raizengod/Playwright-Python_Swag-Labs.git
    cd SWAG_LABS
    ```

2.  **Crear y activar un entorno virtual (recomendado):**
    ```bash
    python -m venv venv
    # En Windows:
    .\venv\Scripts\activate
    # En macOS/Linux:
    source venv/bin/activate
    ```

3.  **Instalar las dependencias:**
    ```bash
    pip install -r requirements.txt
    playwright install  # Instala los navegadores necesarios (Chromium, Firefox, WebKit)
    ```

4.  **Ejecutar todas las pruebas con Pytest:**
    ```bash
    pytest swag_labs/test/test_login.py swag_labs/test/test_home.py swag_labs/test/test_producto.py swag_labs/test/test_carrito.py swag_labs/test/test_menu.py -s -v
    ```

5.  **Ejecutar pruebas específicas (ejemplo):**
    ```bash
    pytest swag_labs/test/test_login.py
    ```

6.  **Ejecutar todas las pruebas con reporte detallado (ejemplo):**
    ```bash
    pytest swag_labs/test/test_login.py swag_labs/test/test_home.py swag_labs/test/test_producto.py swag_labs/test/test_carrito.py swag_labs/test/test_menu.py -s -v --template=html1/index.html --report=reporte_de_ejecución.html
    ```

## 📈 Integración Continua (CI)

El proyecto está configurado con **GitHub Actions** para ejecutar las pruebas automáticamente en cada push a la rama principal y en cada pull request. El archivo de configuración se encuentra en `.github/workflows/playwright.yml`. Esto garantiza que cualquier cambio en el código se valide rápidamente, detectando regresiones de manera temprana.

## ✅ Habilidades Demostradas

A través de este proyecto, demuestro las siguientes habilidades clave en QA Automation:

* **Diseño de Frameworks de Automatización**: Implementación de una estructura de proyecto modular y escalable (POM).
* **Automatización de Pruebas End-to-End**: Creación de escenarios de prueba realistas que cubren flujos de usuario completos.
* **Uso de Playwright**: Experiencia en la interacción con elementos web, manejo de aserciones y configuración de pruebas con Playwright.
* **Programación en Python**: Habilidad para escribir código limpio, legible y eficiente para la automatización.
* **Integración Continua (CI)**: Configuración y mantenimiento de pipelines de CI con GitHub Actions para una ejecución de pruebas automatizada y recurrente.
* **Identificación y Reporte de Bugs**: Capacidad para diseñar pruebas que revelen defectos y, en un entorno de trabajo real, reportarlos adecuadamente.
* **Mantenibilidad de Código**: Organización del código para facilitar futuras actualizaciones y extensiones de las pruebas.

## 🔮 Mejoras Futuras

* Implementar generación de reportes más detallados (Allure Report, etc.).
* Añadir capturas de pantalla automáticas en caso de fallos de prueba.
* Integrar pruebas de accesibilidad y rendimiento básicas.
* Configurar variables de entorno para la URL base y credenciales.
