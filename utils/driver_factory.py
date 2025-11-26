from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

def get_driver():
    # Configuración de Chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    options.add_argument("--disable-gpu")
    options.add_argument("--disable-notifications")
    options.add_argument("--disable-infobars")
    options.add_argument("--ignore-certificate-errors")
    options.add_argument("--no-sandbox")

    # Crear instancia del driver usando WebDriver Manager
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    return driver
