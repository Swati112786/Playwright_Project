from playwright.sync_api import expect, Page
from config.settings import BASE_URL
from test_data.login_data import VALID_LOGIN
from pages.inventory_page import InventoryPage

# test case 1
def test_inventory_page_displays_products(login_page, page:Page):
    login_page.login(VALID_LOGIN["username"], VALID_LOGIN["password"])

    # call inventory page
    inventory_page = InventoryPage(page)

    expect(inventory_page.page_title).to_be_visible()
    expect(inventory_page.product_cards.first).to_be_visible()
    expect(inventory_page.cart_icon).to_be_visible()
    expect(inventory_page.sort_dropdown).to_be_visible()

    for i in range(6):
        expect(inventory_page.product_name.nth(i)).to_be_visible()
        print(inventory_page.product_name.nth(i).all_text_contents())


# test case 2- to add first product to cart
def test_add_first_product_to_cart(login_page, page:Page)       :
    login_page.login(VALID_LOGIN["username"], VALID_LOGIN["password"])
    inventory_page = InventoryPage(page)
    inventory_page.add_first_product_to_cart()
    page.wait_for_timeout(3000)
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")

    # test case 3- to remove first product from cart
def test_remove_product_from_cart(login_page, page:Page):
    login_page.login(VALID_LOGIN["username"], VALID_LOGIN["password"])
    inventory_page = InventoryPage(page)

    inventory_page.add_first_product_to_cart()
    expect(page.locator(".shopping_cart_badge")).to_have_text("1")

    inventory_page.remove_first_product_from_cart()
    expect(page.locator(".shopping_cart_badge")).to_have_count(0)
    page.wait_for_timeout(3000)



