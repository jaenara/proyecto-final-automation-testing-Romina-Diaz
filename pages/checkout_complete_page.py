from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CheckoutCompletePage:
    TITLE = (By.CLASS_NAME, "title")

    def __init__(self, driver):
        self.driver = driver

    def get_page_title(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(self.TITLE)
        )
        return self.driver.find_element(*self.TITLE).text
