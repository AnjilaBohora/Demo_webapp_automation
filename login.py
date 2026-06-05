from selenium.webdriver.common.by import By
class Loginpage:
    def __init__(self, driver):
        self.driver=driver
        self.login_link=(By.XPATH, "/html/body/div[4]/div[1]/div[1]/div[2]/div[1]/ul/li[2]/a")
        self.email_textbox=(By.ID, "Email")
        self.password_textbox=(By.ID, "Password")
        self.login_button=(By.XPATH, "/html/body/div[4]/div[1]/div[4]/div[2]/div/div[2]/div[1]/div[2]/div[2]/form/div[5]/input")

    def open_web(self,url):
        self.driver.get(url)

    def click_login_link(self):
        self.driver.find_element(*self.login_link).click()

    def enter_email(self, email):
        self.driver.find_element(*self.email_textbox).send_keys(email)

    def enter_password(self, password):
        self.driver.find_element(*self.password_textbox).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()