from pages.login_page import LoginPage

def test_login_bloqueado(driver):
    # 1. Ir al sitio
    driver.get("https://www.saucedemo.com/")

    # 2. Intentar login con usuario bloqueado
    login = LoginPage(driver)
    login.login("locked_out_user", "secret_sauce")

    # 3. Validar mensaje de error
    error_message = login.get_error_message()
    assert "locked out" in error_message.lower()
