from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage
from pages.checkout_complete_page import CheckoutCompletePage

def test_checkout_completo(driver):
    # 1. Ir al sitio
    driver.get("https://www.saucedemo.com/")

    # 2. Login
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")

    # 3. Inventario
    inventory = InventoryPage(driver)
    assert inventory.get_page_title() == "Products"

    # 4. Agregar producto
    inventory.add_first_product_to_cart()

    # 5. Ir al carrito
    inventory.go_to_cart()

    # 6. Carrito
    cart = CartPage(driver)
    assert cart.get_page_title() == "Your Cart"
    cart.click_checkout()

    # 7. Checkout Step One
    checkout = CheckoutPage(driver)
    checkout.fill_checkout_form("Jae", "Tester", "1234")
    checkout.click_continue()

    # 8. Checkout Overview
    overview = CheckoutOverviewPage(driver)
    assert overview.get_page_title() == "Checkout: Overview"
    overview.click_finish()

    # 9. Checkout Complete
    complete = CheckoutCompletePage(driver)
    assert complete.get_page_title() == "Checkout: Complete!"
    assert "Thank you" in complete.get_complete_message()
