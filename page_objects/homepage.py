from selenium.webdriver.common.by import By


class Homepage:
    CATEGORY = (By.XPATH, "//div[@id='block_top_menu']//a")
    SEARCH_INPUT = (By.ID, "search_query_top")
    SEARCH_BUTTON = (By.XPATH, "//button[contains(@class, 'button-search')]")

    URL = 'http://automationpractice.com/index.php'

    def __init__(self, driver):
        self.driver = driver

    def load(self):
        self.driver.get(self.URL)

    def select_category(self, category_name):
        categories = self.driver.find_elements(*self.CATEGORY)
        for category in categories:
            if category.text == category_name:
                category.click()
                break

    def search(self, keywords):
        search_input = self.driver.find_element(*self.SEARCH_INPUT)
        search_input.send_keys(keywords)
        search_button = self.driver.find_element(*self.SEARCH_BUTTON)
        search_button.click()

