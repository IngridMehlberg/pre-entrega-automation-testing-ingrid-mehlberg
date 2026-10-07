# Proyecto de Automatización de Pruebas - Pre-Entrega (SauceDemo)

## Propósito del Proyecto

Automatizar los flujos principales de navegación y validación en la plataforma de comercio electrónico [SauceDemo](https://www.saucedemo.com/).

Los casos de prueba automatizados cubren:

1. **Inicio de sesión (Login):** Autenticación con credenciales válidas (`standard_user` / `secret_sauce`), sincronización mediante esperas explícitas y validación de redirección a la página de inventario.

2. **Navegación y Catálogo:** Validación del título de la sección de productos, verificación de elementos del inventario, extracción del nombre y precio del primer producto, y comprobación de la presencia de controles de interfaz (menú y selector de filtros).

3. **Carrito de Compras:** Adición del primer producto al carrito, validación del incremento del contador (`badge`) a 1, navegación al carrito y verificación de la presencia del producto agregado.

---

## Tecnologías Utilizadas

- **Lenguaje de Programación:** Python 3
- **Framework de Pruebas:** Pytest
- **Herramienta de Automatización Web:** Selenium WebDriver
- **Generación de Reportes:** pytest-html
- **Control de Versiones:** Git y GitHub

---

## Estructura del Proyecto

```text
pre-entrega-automation-testing-ingrid-mehlberg/
│
├── tests/
│   ├── __init__.py
│   └── test_saucedemo.py       # Casos de prueba automatizados con Pytest
│
├── utils/
│   ├── __init__.py
│   └── driver_setup.py         # Configuración e inicialización del WebDriver
│
├── reports/
│   └── reporte.html            # Reporte visual generado por pytest-html
│
├── datos/                      # Carpeta para archivos de datos de prueba
│
├── .gitignore                  # Exclusiones de Git (entorno virtual, cachés)
├── requirements.txt            # Lista de dependencias del proyecto
└── README.md                   # Documentación del proyecto
```

---

## Instalación y Configuración

### 1. Clonar el repositorio

```bash
git clone <URL_DE_TU_REPOSITORIO_GITHUB>
cd pre-entrega-automation-testing-ingrid-mehlberg
```

### 2. Crear el entorno virtual

```bash
python -m venv venv
```

### 3. Activar el entorno virtual

En Windows:

```bash
.\venv\Scripts\activate
```

En Linux / macOS:

```bash
source venv/bin/activate
```

### 4. Instalar las dependencias

```bash
pip install -r requirements.txt
```

---

## Ejecución de las Pruebas

Para ejecutar todos los casos de prueba:

```bash
pytest -v
```

Para ejecutar las pruebas y generar el reporte HTML:

```bash
pytest -v --html=reports/reporte.html --self-contained-html
```

Una vez finalizada la ejecución, el reporte estará disponible en:

```text
reports/reporte.html
```

El archivo puede abrirse desde cualquier navegador web para consultar el resultado de las pruebas.