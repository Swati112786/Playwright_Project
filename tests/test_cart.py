from playwright.sync_api import expect, Page
from config.settings import BASE_URL
from pages.inventory_page import InventoryPage
from test_data.login_data import VALID_LOGIN
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


# test case 1 - to click on add to cart
def test_clicking_cart_icon_opens_cart_page(login_page, page:Page):
     # Log in
    login_page.login(
        VALID_LOGIN["username"],
        VALID_LOGIN["password"]
    )

    # Initialize Inventory Page Object
    inventory_page = InventoryPage(page)

    inventory_page.open_cart()
    # Verify navigation to the cart page
    expect(page).to_have_url(f"{BASE_URL}/cart.html")
    # Verify the cart page heading
    expect(page.get_by_text("Your Cart", exact=True)).to_be_visible()
    


    #  test case 2
def test_cart_displays_added_product(login_page, page: Page):
    # Log in
    login_page.login(
        VALID_LOGIN["username"],
        VALID_LOGIN["password"]
    )

    # Add the first product
    inventory_page = InventoryPage(page)
    inventory_page.add_first_product_to_cart()

    inventory_page.open_cart()
    page.wait_for_timeout(3000)
    expect(page.get_by_text("Sauce Labs Backpack", exact=True)).to_be_visible()


    # test case 3

def test_cart_displays_correct_quantity_and_price(login_page, page: Page):
    # Log in
    login_page.login(
        VALID_LOGIN["username"],
        VALID_LOGIN["password"]
    )

    # Add the first product to the cart
    inventory_page = InventoryPage(page)
    inventory_page.add_first_product_to_cart()

    # Open the cart
    inventory_page.open_cart()

    # Verify quantity is 1
    expect(page.locator(".cart_quantity")).to_have_text("1")

    # Verify the product price
    expect(page.locator(".inventory_item_price")).to_have_text("$29.99")



# test case 5
def test_remove_product_from_cart_page(login_page, page: Page):
    # Log in
    login_page.login(
        VALID_LOGIN["username"],
        VALID_LOGIN["password"]
    )

    # Add a product
    inventory_page = InventoryPage(page)
    inventory_page.add_first_product_to_cart()

    # Open the cart
    inventory_page.open_cart()

    # Initialize Cart Page Object
    cart_page = CartPage(page)

    # Verify one product is in the cart
    expect(cart_page.cart_item).to_have_count(1)

    # Remove the product
    cart_page.remove_first_item()

    # Verify the cart is empty
    expect(cart_page.cart_item).to_have_count(0)



# test case 6 - test checkout page

def test_checkout_with_valid_details(login_page, page:Page):
    login_page.login(VALID_LOGIN["username"], VALID_LOGIN["password"])
    inventory_page = InventoryPage(page)
    inventory_page.add_first_product_to_cart()
    inventory_page.open_cart()

    checkout_page = CheckoutPage(page)
    checkout_page.checkout_button.click()
    checkout_page.first_name_input.fill("Swati")
    checkout_page.last_name_input.fill("Pandey")
    checkout_page.postal_code_input.fill("201301")
    checkout_page.continue_button.click()

    expect(page).to_have_url(BASE_URL + "/checkout-step-two.html")
    expect(page.get_by_text("Checkout: Overview", exact=True)).to_be_visible()
    page.wait_for_timeout(3000)
    
# test case 7
def test_checkout_order_summary(login_page, page:Page):
    login_page.login(VALID_LOGIN["username"], VALID_LOGIN["password"])
    inventory_page = InventoryPage(page)
    inventory_page.add_first_product_to_cart()
    inventory_page.open_cart()

    checkout_page = CheckoutPage(page)
    checkout_page.checkout_button.click()
    checkout_page.first_name_input.fill("Swati")
    checkout_page.last_name_input.fill("Pandey")
    checkout_page.postal_code_input.fill("201301")
    checkout_page.continue_button.click() 
    expect(checkout_page.summary_items).to_have_count(1)
    expect(checkout_page.item_total).to_have_text("Item total: $29.99")
    expect(checkout_page.finish_button).to_be_visible()


    # test case 8


def test_complete_checkout_successfully(login_page, page: Page):
    # Log in
    login_page.login(
        VALID_LOGIN["username"],
        VALID_LOGIN["password"]
    )

    # Add a product to the cart
    inventory_page = InventoryPage(page)
    inventory_page.add_first_product_to_cart()

    # Open cart and start checkout
    inventory_page.open_cart()
    checkout_page = CheckoutPage(page)
    checkout_page.checkout_button.click()

    # Enter checkout details
    checkout_page.first_name_input.fill("Swati")
    checkout_page.last_name_input.fill("Pandey")
    checkout_page.postal_code_input.fill("201301")
    checkout_page.continue_button.click()

    # Finish checkout
    checkout_page.finish_checkout()

    # Verify successful order completion
    expect(page).to_have_url(BASE_URL +  "/checkout-complete.html")
    expect(page.get_by_text("Thank you for your order!", exact=True)).to_be_visible()
