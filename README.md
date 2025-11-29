# Proyecto Final de Automatización - Testing UI + API #

# Descripción General
Este proyecto corresponde a la entrega final del curso de Automatización de Testing.
Incluye:
-Pruebas automáticas de UI utilizando Selenium WebDriver
-Pruebas automáticas de API utilizando requests
-Implementación del patrón Page Object Model (POM)
-Reportes HTML generados mediante pytest-html
-Sistema de capturas automáticas cuando un test falla
-Suite completa integrable, reproducible y documentada
-La aplicación utilizada para las pruebas UI es SauceDemo.
-Para API se utiliza la API pública JSONPlaceholder.

# Tecnologías Utilizadas
-Python 3
-Pytest
-Selenium WebDriver
-Requests
-Pytest-html
-Patrones POM
-ChromeDriver
-JSONPlaceholder (API pública)

# Estructura del Proyecto
 El proyecto sigue una estructura basada en buenas prácticas para automatización con Selenium + Pytest, utilizando el patrón Page Object Model (POM).

proyecto-final-automation-testing-Romina-Diaz/
│
├── pages/                      # Clases POM: una por cada página de SauceDemo
│   ├── login_page.py
│   ├── inventory_page.py
│   ├── cart_page.py
│   ├── checkout_page.py
│   ├── checkout_overview_page.py
│   └── checkout_complete_page.py
│
├── tests/                      # Pruebas UI y API
│   ├── test_login_correcto.py
│   ├── test_login_incorrecto.py
│   ├── test_login_bloqueado.py
│   ├── test_agregar_producto.py
│   ├── test_checkout_completo.py
│   ├── test_api_get_posts.py
│   ├── test_api_create_post.py
│   ├── test_api_delete_post.py
│   ├── test_api_encadenado.py   # Post + Get encadenado
│
├── utils/
│   └── driver_factory.py        # Inicialización del WebDriver
│
├── reports/
│   ├── reporte_test.html        # Generado automáticamente con pytest-html
│   └── screenshots/             # Capturas automáticas de fallos
│
├── conftest.py                  # Fixture del driver + hook de capturas
├── requirements.txt             # Dependencias del proyecto
├── pytest.ini                   # Configuración para Pytest
└── README.md                    # Documentación del proyecto

# Instalación del Entorno #

# Clonar el repositorio:

git clone https://github.com/jaenara/proyecto-final-automation-testing-Romina-Diaz.git


# Instalar dependencias:

pip install -r requirements.txt


Verificar que ChromeDriver está disponible
(Se encuentra configurado automáticamente mediante driver_factory.py).

El entorno quedará listo para ejecutar la suite completa.

# Cómo ejecutar los tests
-Para ejecutar la suite completa (UI + API):
pytest -v

Esto ejecuta:
→Pruebas de UI con Selenium
→Pruebas de API con Requests
→La estructura POM
→Los fixtures configurados
→Todo el flujo de checkout

# Ejecutar un archivo específico
pytest tests/test_login_correcto.py -v

Generación de Reporte HTML

El proyecto incluye reportes generados con pytest-html.

# Para generar un reporte manual:
pytest --html=reports/reporte_test.html --self-contained-html -v

El archivo se genera en:
reports/reporte_test.html

Contiene:
→Listado de tests
→Estado (passed / failed)
→Tiempos
→Metadata
→Capturas automáticas si hubo fallos

# Capturas Automáticas de Fallos
Cuando un test falla, el hook implementado en conftest.py:
→Detecta el fallo
→Toma una captura del navegador
→Guarda la imagen en:
reports/screenshots/

Esta funcionalidad permite analizar visualmente qué ocurrió en el momento del error, mejorando el proceso de debugging.

# Pruebas de UI Implementadas
El proyecto automatiza las siguientes funciones reales de SauceDemo:
-Login correcto
-Login incorrecto
-Login bloqueado
-Agregar producto al carrito
-Flujo completo de compra:
Login → Inventario → Carrito → Checkout Step One → Overview → Confirmación

Todas las páginas están implementadas utilizando el patrón Page Object Model, con:
-Métodos específicos por página
-Selectores organizados
-Esperas explícitas (WebDriverWait)
-Validaciones claras

# Pruebas de API Implementadas
Usando la API pública JSONPlaceholder se implementaron:
-GET /posts
-POST /posts (creación de recurso)
-DELETE /posts/id
-Prueba encadenada POST → GET
(Crear un recurso y luego obtenerlo usando el ID devuelto)

Cada prueba valida:
→Código de estado
→Estructura y contenido
→Flujo de petición y respuesta

# Inestabilidad de SauceDemo
El test test_checkout_completo.py puede fallar de manera ocasional debido a la inestabilidad del sitio real de práctica SauceDemo, especialmente en el paso de confirmación del checkout.

Este comportamiento es externo al proyecto y no depende del código.
Cuando el sitio no responde correctamente:
→El test falla
→Se toma una captura automática
→El reporte HTML lo documenta
→Este caso sirve como ejemplo real de cómo manejar errores intermitentes en entornos externos.

# Autora
Romina Elizabeth Díaz
Proyecto Final – Automatización de Testing
Año 2025