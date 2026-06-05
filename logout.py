from selenium.webdriver.common.by import By
class Logout:
    def __init__(self, driver):
        self.driver=driver
        self.logout_link=(By.XPATH, "/html/body/div[4]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a")

    def logging_out(self):
        self.driver.find_element(*self.logout_link).click()