from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutOverviewPage:
    def __init__(self, driver):
        self.driver = driver

        self.finish_button = (By.ID, "finish")
        self.title = (By.CLASS_NAME, "title")

    def get_page_title(self):
        return self.driver.find_element(*self.title).text

    def click_finish(self):
        # Esperar a que el botón FINISH esté presente
        WebDriverWait(self.driver, 15).until(
            EC.presence_of_element_located(self.finish_button)
        )

        # Esperar a que sea clickeable
        finish_btn = WebDriverWait(self.driver, 15).until(
            EC.element_to_be_clickable(self.finish_button)
        )
        finish_btn.click()

        # Esperar a que el título de la página final sea visible
        WebDriverWait(self.driver, 15).until(
            EC.text_to_be_present_in_element(
                (By.CLASS_NAME, "title"),
                "Checkout: Complete!"
            )
        )

