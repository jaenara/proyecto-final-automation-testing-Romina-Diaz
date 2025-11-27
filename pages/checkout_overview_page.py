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
        # Espera a que el botón sea clickeable
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(self.finish_button)
        ).click()
