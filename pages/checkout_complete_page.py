from selenium.webdriver.common.by import By

class CheckoutCompletePage:
    def __init__(self, driver):
        self.driver = driver

        self.title = (By.CLASS_NAME, "title")
        self.complete_message = (By.CLASS_NAME, "complete-header")

    # Validar título de la página
    def get_page_title(self):
        return self.driver.find_element(*self.title).text

    # Obtener mensaje de confirmación
    def get_complete_message(self):
        return self.driver.find_element(*self.complete_message).text
