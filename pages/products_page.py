from selenium.webdriver.common.by import By
from pages.base_page import BasePage
from selenium.webdriver.support.ui import Select

class ProductsPage(BasePage):

    cart_badge = (By.CLASS_NAME, "shopping_cart_badge")
    PAGE_TITLE = (By.CLASS_NAME, "title")

    def get_page_title_text(self):
        return self.wait_for_element_visible(self.PAGE_TITLE).text

    def is_products_page_displayed(self):
        return "Products" in self.get_page_title_text()

    def dropdown(self, drop_text):
        dropdown = self.wait_for_element_visible(
            (By.XPATH, "//select[@class='product_sort_container']")
        )
        select = Select(dropdown)
        select.select_by_visible_text(drop_text)

    def get_all_products_prices(self):
        elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_price")
        prices = []
        for price in elements:
            price_text = float(price.text.replace("$", ""))
            prices.append(price_text)
        return prices

    def get_all_products_names(self):
        elements = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        product_names = []
        for product in elements:
            product_names.append(product.text)
        return product_names

    def add_to_cart(self, product_name):
        add_to_cart_btn = self.wait_for_element_clickable(
            (By.XPATH, f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button")
        )
        add_to_cart_btn.click()
    def get_cart_badge_count(self):
        cart_count = self.wait_for_element_visible(self.cart_badge).text
        return cart_count


