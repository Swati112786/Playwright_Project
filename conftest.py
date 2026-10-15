import pytest
from pages.login_page import LoginPage

@pytest.fixture
def login_page(page):
    login_page = LoginPage(page)
    login_page.open()
    return login_page


# @pytest.fixture tells Pytest that this function provides reusable setup.
# page is the browser-page fixture provided by pytest-playwright.
# LoginPage(page) creates the Page Object.
# login_page.open() navigates to SauceDemo.
# return login_page gives the prepared object to the test.