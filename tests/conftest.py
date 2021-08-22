import pytest
import selenium.webdriver


@pytest.fixture()
def driver():

    browser = selenium.webdriver.Chrome()

    # Will wait up to 10 seconds for elements to appear
    browser.implicitly_wait(10)

    # Return the WebDriver instance for the setup
    yield browser

    # After the test runs, quit the WebDriver instance
    browser.quit()
