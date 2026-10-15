from playwright.sync_api import Page

class CheckoutPage:
    def __init__(self, page:Page):
        self.page = page
        self.checkout_button = page.get_by_role("button", name="Checkout")

        self.first_name_input = page.get_by_placeholder("First Name")
        self.last_name_input = page.get_by_placeholder("Last Name")
        self.postal_code_input = page.get_by_placeholder("Zip/Postal Code")
        self.continue_button = page.get_by_role("button", name="Continue")
        self.summary_items = page.locator(".cart_item")
        self.item_total = page.locator(".summary_subtotal_label")
        self.finish_button = page.get_by_role("button", name="Finish")

    def finish_checkout(self):
        self.finish_button.click()

