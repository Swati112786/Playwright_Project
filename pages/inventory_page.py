from playwright.sync_api import Page

class InventoryPage:
    def __init__(self, page:Page):
        self.page = page
# Inventory page locator
        self.page_title = page.locator(".title")
        self.product_cards = page.locator(".inventory_item" )
        self.sort_dropdown = page.locator("[data-test='product-sort-container']"  )
        self.cart_icon = page.locator("[data-test='shopping-cart-link']" )
        self.product_name = page.locator(".inventory_item_name")
        self.add_to_cart_button = page.get_by_role("button", name="Add to cart")
        self.remove_button = self.page.get_by_role("button", name="Remove")

    def sort_products(self, option: str):
        self.sort_dropdown.select_option(option)

    def add_first_product_to_cart(self):
        self.add_to_cart_button.first.click()

    def remove_first_product_from_cart(self):
        self.remove_button.first.click()

    def open_cart(self):
        self.cart_icon.click()
        

        