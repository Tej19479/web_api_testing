from pages.pom_click import POM
from pages.login_page import Login
from utils.assertion import soft_check

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Test_login:
        def test_login_check(self, driver, base_url, request):
            driver.get(base_url)
            pom = POM(driver, request)

            print("request         -----   ", request)

            status = pom.page_click_on_pom()
            print("status of click_on_pom", status)

            if status is True:
                print("title of current page:", driver.title)
                # Soft assertion with screenshot if the title does not match
                soft_check(
                    driver,
                    True,
                    "Title mismatch after clicking POM card",
                    "test_pom_to_click_profile",
                    request.node
                )

            status = pom.click_on_profile_icon()
            print("click_on_profile_page", status)

            if status:
                soft_check(
                    driver,
                    True,
                    "click after profile button",
                    "test_pom_to_click_profile",
                    request.node
                )

            login=Login(driver,request)
            status=login.login_data_centdrails(username='mor_2314',password="83r5^_")
            if status:
                WebDriverWait(driver, 10).until(EC.url_contains("home"))
                print("current url   ",driver.current_url)
                print("current url   ", driver.current_url)
                soft_check(
                    driver,
                    driver.current_url == "https://letcode.in/home",
                    message="test case pass",
                    test_name=request,
                    request_node=request.node
                )
            else:
                soft_check(
                    driver,
                    False,
                    message="Login failed or not navigated to expected page",
                    test_name="test_pom_to_click_profile",
                    request_node=request
                )


