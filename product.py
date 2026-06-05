from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Product:
    def __init__(self, driver):
        self.driver=driver
        self.wait = WebDriverWait(driver, 10)

        self.books_menu = (By.XPATH, "/html/body/div[4]/div[1]/div[2]/ul[1]/li[1]/a")
        self.sort_dropdown = (By.ID, "products-orderby")
        self.first_product = (By.XPATH, "(//h2[@class='product-title']/a)[1]")
        self.add_book = (By.ID, "add-to-cart-button-13")
        self.second_product = (By.XPATH, "//*[@id='product-details-form']/div/div[2]/div[2]/div[4]/div/div[1]/a/img")
        self.add_jeans = (By.ID, "add-to-cart-button-36")
        self.open_cart_menu = (By.XPATH, "//*[@id='topcartlink']/a/span[1]")

    def open_books(self):
        self.wait.until(
            EC.element_to_be_clickable(self.books_menu)
        ).click()

    def dropdown(self):
        dropdown = self.wait.until(
            EC.visibility_of_element_located(self.sort_dropdown)
        )

        Select(dropdown).select_by_visible_text("Price: Low to High")

    def open_product_in_new_tab(self):

        product = self.wait.until(
            EC.presence_of_element_located(self.first_product)
        )
        url = product.get_attribute("href")
        self.driver.switch_to.new_window("tab")
        self.driver.get(url)

    def add_to_cart(self):
        self.driver.find_element(*self.add_book).click()
        self.driver.execute_script("window.scrollBy(0, 400);")

    def pant(self):
        self.driver.find_element(*self.second_product).click()
        self.driver.execute_script("window.scrollBy(0, 200);")
    def add_pant(self):
        self.driver.find_element(*self.add_jeans).click()
        self.driver.execute_script("window.scrollBy(0, 0);")

    def cart_menu(self):
        self.wait.until(EC.element_to_be_clickable(self.open_cart_menu)
        ).click()
