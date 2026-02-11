from pages.products_page import ProductsPage
from pages.login_page import LoginPage
from utils.logger import get_logger

def test_add_to_cart(driver):
    logger = get_logger()
    logger.info("Test started")
    
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    assert "Swag Labs" in driver.title

    products = ProductsPage(driver)
    #searching for product name specified by customer and adding to cart

    products.add_to_cart("Sauce Labs Backpack")
    login.take_screenshot("Product added to cart")
    products.add_to_cart("Sauce Labs Fleece Jacket")
    login.take_screenshot("another product added to cart")
    cart_badge_count = products.get_cart_badge_count()
    logger.info(f"Cart badge count after adding products: {cart_badge_count}")

    logger.info("Test completed")
    