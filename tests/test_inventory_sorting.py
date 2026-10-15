from playwright.sync_api import expect, Page
from test_data.login_data import VALID_LOGIN
from pages.inventory_page import InventoryPage


def test_products_sorted_by_price_low_to_high(login_page, page:Page):
    login_page.login(VALID_LOGIN["username"], VALID_LOGIN["password"])


# test case low to high
    # create inventory page object
    inventory_page = InventoryPage(page)
    # call sorting method
    inventory_page.sort_products("lohi")

    prices = page.locator(".inventory_item_price").all_text_contents()
    numeric_prices = []

    for price in prices:
        numeric_prices.append(float(price.replace("$", "")))
       
    assert numeric_prices == sorted(numeric_prices)




# test case high to low

def test_products_sorted_by_price_high_to_low(login_page, page: Page):
    # Log in
    login_page.login( VALID_LOGIN["username"],VALID_LOGIN["password"])

    # Initialize Inventory Page Object
    inventory_page = InventoryPage(page)

    # Sort products by price: high to low
    inventory_page.sort_products("hilo")

    # Get all product prices displayed on the page
    prices = page.locator(".inventory_item_price").all_text_contents()

    # Convert price strings to numbers
    numeric_prices = []

    for price in prices:
        numeric_prices.append(float(price.replace("$", "")))

    # Verify prices are in descending order
    assert numeric_prices == sorted(numeric_prices, reverse=True)




# test case 3 count no. of products

def test_all_six_product_cards_are_displayed(login_page, page: Page):
    # Log in
    login_page.login(VALID_LOGIN["username"], VALID_LOGIN["password"])

    # Locate all product cards
    product_cards = page.locator(".inventory_item")

    # Verify exactly six products are displayed
    expect(product_cards).to_have_count(6)

