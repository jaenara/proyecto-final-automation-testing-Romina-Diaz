from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        # Constructor: recibe el driver y lo guarda para usarlo en todos los métodos
        self.driver = driver

        # Locators (elementos de la página)
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.CSS_SELECTOR, "[data-test='error']")

    # Método para ingresar el usuario
    def enter_username(self, username):
        self.driver.find_element(*self.username_input).clear()
        self.driver.find_element(*self.username_input).send_keys(username)

    # Método para ingresar la contraseña
    def enter_password(self, password):
        self.driver.find_element(*self.password_input).clear()
        self.driver.find_element(*self.password_input).send_keys(password)

    # Método para hacer click en el botón de login
    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    # Método de acción completa: login
    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()

    # Método para obtener el mensaje de error
    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text
