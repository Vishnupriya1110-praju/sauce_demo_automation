from pages.products_page import ProductsPage
from pages.login_page import LoginPage
from utils.logger import get_logger

def test_dropdown(driver):
    logger = get_logger()
    logger.info("Test started")
    
    login = LoginPage(driver)
    login.login("standard_user", "secret_sauce")
    products = ProductsPage(driver)
    assert products.is_products_page_displayed()
    login.take_screenshot("Products_page")
    
    products.dropdown("Name (Z to A)")
    login.take_screenshot("Products sorted in Descending order")
    
    actual_product_names = products.get_all_products_names()
    expected_product_names = sorted(actual_product_names, reverse=True)
    logger.info(f"Actual Product Names: {actual_product_names}")
    logger.info(f"Expected Product Names: {expected_product_names}")
    assert actual_product_names == expected_product_names

    products.dropdown("Name (A to Z)")
    login.take_screenshot("Products sorted in Ascending order")

    actual_product_names = products.get_all_products_names()
    expected_product_names = sorted(actual_product_names, reverse=False)
    logger.info(f"Actual Product Names: {actual_product_names}")
    logger.info(f"Expected Product Names: {expected_product_names}")
    assert actual_product_names == expected_product_names

    products.dropdown("Price (high to low)")
    login.take_screenshot("Products sorted in Price High to Low")

    actual_prices = products.get_all_products_prices()
    expected_prices = sorted(actual_prices, reverse=True)
    logger.info(f"Actual Prices: {actual_prices}")
    logger.info(f"Expected Prices: {expected_prices}")
    assert actual_prices == expected_prices

    products.dropdown("Price (low to high)")
    login.take_screenshot("Products sorted in Price Low to High")

    actual_prices = products.get_all_products_prices()
    expected_prices = sorted(actual_prices, reverse=False)
    logger.info(f"Actual Prices: {actual_prices}")
    logger.info(f"Expected Prices: {expected_prices}")
    assert actual_prices == expected_prices

    logger.info("Test completed")