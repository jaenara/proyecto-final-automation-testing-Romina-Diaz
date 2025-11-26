from selenium.webdriver.common.by import By

class InventoryPage:
    def __init__(self, driver):
        self.driver = driver

        # Locators
        self.cart_icon = (By.ID, "shopping_cart_container")
        self.first_product_add_button = (By.CSS_SELECTOR, "button.btn_inventory")
        self.inventory_title = (By.CLASS_NAME, "title")

    # Obtener el título de la página (para validar que estamos aquí)
    def get_page_title(self):
        return self.driver.find_element(*self.inventory_title).text

    # Agregar el primer producto de la lista al carrito
    def add_first_product_to_cart(self):
        self.driver.find_element(*self.first_product_add_button).click()

    # Ir al carrito
    def go_to_cart(self):
        self.driver.find_element(*self.cart_icon).click()
