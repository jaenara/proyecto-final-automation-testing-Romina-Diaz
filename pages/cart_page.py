from selenium.webdriver.common.by import By

class CartPage:
    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.page_title = (By.CLASS_NAME, "title")
        self.checkout_button = (By.ID, "checkout")

    # Validar que estamos en la página del carrito
    def get_page_title(self):
        return self.driver.find_element(*self.page_title).text

    # Hacer click en el botón de Checkout
    def click_checkout(self):
        self.driver.find_element(*self.checkout_button).click()
