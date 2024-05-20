import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LcWaikiki(unittest.TestCase):
    WEBSITE_URL = "https://www.lcwaikiki.com/tr-TR/TR/"
    HOMEPAGE_CONTAINER = (By.CSS_SELECTOR, ".container-fluid.homepage-container")
    CATEGORY_PAGE = (By.LINK_TEXT, "AYAKKABI")
    SUB_CATEGORY_PAGE = (By.CSS_SELECTOR, ".tree-node__item") #4
    SUB_CATEGORY_SELECTED_CONTROL = (By.CSS_SELECTOR, ".tree-node__text--selected")
    PRODUCT_PAGE = (By.CSS_SELECTOR, ".product-card.product-card--one-of-4")  #1
    SHOW_REVIEWS_BUTTON = (By.CSS_SELECTOR, ".show-reviews-button")
    CHOOSE_SIZE = (By.CSS_SELECTOR, "a[data-tracking-label='BedenSecenekleri']")  #1
    ADD_TO_CART = (By.CSS_SELECTOR, ".add-to-cart.button-link.add-to-cart-button")
    NUMBER_CART_PRODUCTS = (By.CSS_SELECTOR, ".badge-circle")
    CART_PAGE = (By.CSS_SELECTOR, ".cart-dropdown") #2
    CART_TITLE = (By.CSS_SELECTOR, ".col-xs-6")
    MAIN_HEADER_LOGO = (By.CSS_SELECTOR, ".main-header-logo")

    def setUp(self):
        """
        Initial settings are being made
        """
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.driver.get(self.WEBSITE_URL)
        self.wait = WebDriverWait(self.driver, 15)

    def test_navigate(self):
        """
        Initialization processes
        """
        self.assertTrue(self.wait.until(ec.presence_of_element_located(self.HOMEPAGE_CONTAINER)).is_displayed(),
                        "No homepage container")

        self.wait.until(ec.element_to_be_clickable(self.CATEGORY_PAGE)).click()
        self.assertTrue(self.wait.until(ec.element_to_be_clickable(self.SUB_CATEGORY_PAGE)), "Sub categories not clickable")

        self.wait.until(ec.presence_of_all_elements_located(self.SUB_CATEGORY_PAGE))[4].click()
        self.driver.implicitly_wait(10)
        self.assertTrue(self.wait.until(ec.presence_of_element_located(self.SUB_CATEGORY_SELECTED_CONTROL)).is_displayed(), "Banner did not arrive")

        self.wait.until(ec.presence_of_all_elements_located(self.PRODUCT_PAGE))[1].click()
        self.assertTrue(self.wait.until(ec.presence_of_element_located(self.SHOW_REVIEWS_BUTTON)).is_displayed(), "No show reviews button")

        self.wait.until(ec.presence_of_all_elements_located(self.CHOOSE_SIZE))[1].click()
        self.assertTrue(self.wait.until(ec.element_to_be_clickable(self.CHOOSE_SIZE)), "Choose size not clickable")

        self.wait.until(ec.presence_of_element_located(self.ADD_TO_CART)).click()
        self.assertEqual("1", self.wait.until(ec.presence_of_element_located(self.NUMBER_CART_PRODUCTS)).text, "Add to cart failed")

        self.wait.until(ec.presence_of_all_elements_located(self.CART_PAGE))[2].click()
        self.assertEqual("SİPARİŞ ÖZETİ", self.wait.until(ec.presence_of_element_located(self.CART_TITLE)).text, "Cart page could not be opened")

        self.wait.until(ec.presence_of_element_located(self.MAIN_HEADER_LOGO)).click()
        self.assertTrue(self.wait.until(ec.presence_of_element_located(self.HOMEPAGE_CONTAINER)).is_displayed(),
                        "No homepage container")

    def tearDown(self):
        """
        Termination operations
        """
        self.driver.quit()


lcWaikiki = LcWaikiki()
lcWaikiki.setUp()
lcWaikiki.test_navigate()

