from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Checkout:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 15)

        self.continue_button = (By.CSS_SELECTOR, "#billing-buttons-container input")
        self.shipping_method = (By.CSS_SELECTOR, "#shipping-buttons-container input")
        self.third_continue_button = (By.CSS_SELECTOR, "#shipping-method-buttons-container input")
        self.payment_method = (By.CSS_SELECTOR, "#payment-method-buttons-container input")
        self.payment_information = (By.CSS_SELECTOR, "#payment-info-buttons-container input")
        self.confirm_order = (By.CSS_SELECTOR, "#confirm-order-buttons-container input")
        self.final_continue_button = (By.CSS_SELECTOR, ".order-completed-continue-button")

    def first_continue(self):
        self.wait.until(
            EC.element_to_be_clickable(self.continue_button)
        ).click()

    def shipping(self):
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable(self.shipping_method)
        ).click()

    def continue_three(self):
        self.wait.until(
            EC.element_to_be_clickable(self.third_continue_button)
        ).click()

    def payment(self):
        self.wait.until(
            EC.element_to_be_clickable(self.payment_method)
        ).click()

    def payment_info(self):
        self.wait.until(
            EC.element_to_be_clickable(self.payment_information)
        ).click()

    def order_confirmation(self):
        self.wait.until(
            EC.element_to_be_clickable(self.confirm_order)
        ).click()

    def final_continue(self):
        self.wait.until(
            EC.element_to_be_clickable(self.final_continue_button)
        ).click()