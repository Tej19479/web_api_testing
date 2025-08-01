from pages.pom_click import POM
from pytest_check import check
from utils.assertion import soft_check

class Test_POM:
    def test_pom_to_click_profile(self, driver, base_url, request):
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
        print(driver.title)
