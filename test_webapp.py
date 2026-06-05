from selenium import webdriver
from login import Loginpage
from product import Product
from cart import Cart
from checkout import Checkout
from logout import Logout
import pytest
import time
@pytest.fixture()
def driver():
    driver=webdriver.Chrome()
    yield driver
    driver.quit()

def test_webapp(driver):
    loginpage=Loginpage(driver)
    product=Product(driver)
    cart=Cart(driver)
    checkout=Checkout(driver)
    logout=Logout(driver)
    
    loginpage.open_web("https://demowebshop.tricentis.com/")
    loginpage.click_login_link()
    driver.maximize_window()
    loginpage.enter_email("yusoiwojeje-5130@yopmail.com")
    loginpage.enter_password("abcdef")
    time.sleep(2)
    loginpage.click_login()
    assert "demowebshop" in driver.current_url
    time.sleep(2)

    product.open_books()
    product.dropdown()
    product.open_product_in_new_tab()
    time.sleep(2)
    product.add_to_cart()
    time.sleep(2)
    product.pant()
    product.add_pant()
    time.sleep(5)
    product.cart_menu()
    time.sleep(2)

    cart.update_quantity()
    time.sleep(2)
    cart.remove()
    cart.click_update_cart()
    time.sleep(2)
    cart.terms_and_condition()
    cart.checkout_process()
    time.sleep(3)

    checkout.first_continue()
    checkout.shipping()
    checkout.continue_three()
    checkout.payment()
    checkout.payment_info()
    checkout.order_confirmation()
    time.sleep(2)
    checkout.final_continue()
    time.sleep(3)

    logout.logging_out()
    time.sleep(3)



