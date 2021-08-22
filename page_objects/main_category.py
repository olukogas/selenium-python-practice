from selenium.webdriver.common.by import By


class MainCategory:
    CATEGORY_TITLE = (By.XPATH, "//span[contains(@class, 'category-name')]")

    def __init__(self, driver):
        self.driver = driver


