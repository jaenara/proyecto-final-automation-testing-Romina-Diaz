from pages.login_page import LoginPage

def test_login_incorrecto(driver):
    # 1. Navegar al sitio
    driver.get("https://www.saucedemo.com/")

    # 2. Instancia de LoginPage
    login_page = LoginPage(driver)

    # 3. Ingresar credenciales inválidas
    login_page.login("usuario_inexistente", "password_incorrecta")

    # 4. Obtener el mensaje de error
    mensaje = login_page.get_error_message()

    # 5. Validar que se muestra el mensaje esperado
    assert "Epic sadface" in mensaje
