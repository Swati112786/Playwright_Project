from playwright.sync_api import Page


class CartPage:
    def __init__(self, page: Page):
        self.page = page
        self.cart_item = page.locator(".cart_item")
        self.remove_button = page.get_by_role("button", name="Remove")

    def remove_first_item(self):
        self.remove_button.first.click()