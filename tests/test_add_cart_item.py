from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from tests.test_login_functionality_check import Login
from pages.add_cart import ADDCARD

class Test_add_cart:
    def test_add_cart(self, driver, base_app_login_url, request):
        # Step 1: Go to login page
        driver.get(base_app_login_url)

        # Step 2: Login
        login = Login(driver, request)
        status = login.login_data_centdrails(username='mor_2314', password="83r5^_")

        # Step 3: After successful login, wait for redirection
        if status:
            # WebDriverWait(driver, 10).until(EC.url_contains("home"))
            # print("Login successful, proceeding with cart process")

            # Step 4: Initialize cart object
            add_cart = ADDCARD(driver, request,"Fjallraven - Foldsack No. 1 Ba...")

            # Step 5: Select product by name (dynamic handling)
            add_cart.product_select()

            print("Cart process completed")
        else:
            print("Login failed, skipping cart process")
