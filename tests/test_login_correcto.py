import time
from pages.login_page import LoginPage

def test_login_correcto(driver):
    # 1. Navegar a la página
    driver.get("https://www.saucedemo.com/")

    # 2. Crear instancia de LoginPage
    login_page = LoginPage(driver)

    # 3. Ejecutar acción de login
    login_page.login("standard_user", "secret_sauce")

    # 4. Validar que la URL cambió al inventario
    assert driver.current_url.endswith("/inventory.html")

time.sleep(1)
