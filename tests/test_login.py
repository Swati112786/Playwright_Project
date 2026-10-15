from playwright.sync_api import expect, Page
from config.settings import BASE_URL
from test_data.login_data import VALID_LOGIN, INVALID_LOGIN
from pages.login_page import LoginPage


# Test 1: Valid login
def test_user_can_login_with_valid_credentials(login_page, page: Page):

# Login using test data
    login_page.login(VALID_LOGIN["username"], VALID_LOGIN["password"])
    
 # Verify successful login
    expect(page).to_have_url(f"{BASE_URL}/inventory.html")
    
 # Verify the product listing page
    expect(page.get_by_text("Products", exact=True)).to_be_visible()
  
    page.wait_for_timeout(3000)


   # Test 1: Invalid login
def test_user_can_login_with_invalid_credentials(login_page, page: Page):

# Login using test data
    login_page.login(INVALID_LOGIN["username"], INVALID_LOGIN["password"])

 # Verify failure login
    expect(page).to_have_url(BASE_URL + "/")

 # Verify the product listing page
    expect(page.get_by_text("Epic sadface: Username and password do not match any user in this service", exact= True)).to_be_visible()
   
    page.wait_for_timeout(10000)