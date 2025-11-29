from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.title = (By.CLASS_NAME, "title")

    def get_page_title(self):
        return self.driver.find_element(*self.title).text

    def fill_checkout_form(self, first_name, last_name, postal_code):
        wait = WebDriverWait(self.driver, 10)

        # Esperamos que aparezca el campo de nombre
        wait.until(EC.visibility_of_element_located(self.first_name_input)).send_keys(first_name)

        # Esperamos que aparezca el campo de apellido
        wait.until(EC.visibility_of_element_located(self.last_name_input)).send_keys(last_name)

        # Esperamos el campo de código postal
        wait.until(EC.visibility_of_element_located(self.postal_code_input)).send_keys(postal_code)

    def click_continue(self):
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.continue_button)
        ).click()
