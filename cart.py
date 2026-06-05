from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Cart:
    def __init__ (self, driver):
        self.driver=driver
        self.wait = WebDriverWait(driver, 10)
        self.book_quantity = (By.XPATH, "/html/body/div[4]/div[1]/div[4]/div/div/div[2]/div/form/table/tbody/tr[1]/td[5]/input")
        self.remove_jeans = (By.XPATH, "/html/body/div[4]/div[1]/div[4]/div/div/div[2]/div/form/table/tbody/tr[2]/td[1]/input")
        self.update_cart =(By.NAME, "updatecart")
        self.condition = (By.NAME, "termsofservice")
        self.checkout_button = (By.ID, "checkout")

    def update_quantity(self):
        quantity = self.wait.until(EC.element_to_be_clickable(self.book_quantity))
        ActionChains(self.driver)\
        .double_click(quantity)\
        .perform()

        quantity.clear()
        quantity.send_keys("4")

    def remove(self):
        self.driver.find_element(*self.remove_jeans).click()  

    def click_update_cart(self):
        self.wait.until(EC.element_to_be_clickable(self.update_cart)).click()
        self.driver.execute_script("window.scrollBy(0, 1000);")

    def terms_and_condition(self):
        self.driver.find_element(*self.condition).click()  

    def checkout_process(self):
        self.driver.find_element(*self.checkout_button).click()


