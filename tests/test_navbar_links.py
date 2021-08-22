from page_objects.homepage import Homepage
from page_objects.main_category import MainCategory


def test_navbar_links(driver):
    """
    Verifies that the links in the navigation bar go to the correct category pages.
    """
    homepage = Homepage(driver)
    main_category = MainCategory(driver)

    category_names = ['WOMEN', 'DRESSES', 'T-SHIRTS']
    for category_name in category_names:
        homepage.load()
        homepage.select_category(category_name)
        category_title = driver.find_element(*main_category.CATEGORY_TITLE)
        assert category_title.text.upper() == category_name
