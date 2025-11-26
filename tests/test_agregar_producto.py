from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage

def test_agregar_producto_al_carrito(driver):
    # 1. Abrir la página principal
    driver.get("https://www.saucedemo.com/")

    # 2. Login correcto
    login_page = LoginPage(driver)
    login_page.login("standard_user", "secret_sauce")

    # 3. Ir al inventario
    inventory_page = InventoryPage(driver)

    # 4. Validar que estamos en la página de inventario
    assert inventory_page.get_page_title() == "Products"

    # 5. Agregar el primer producto
    inventory_page.add_first_product_to_cart()

    # 6. Ir al carrito
    inventory_page.go_to_cart()

    # 7. Validar que la URL corresponde al carrito
    assert driver.current_url.endswith("/cart.html")
