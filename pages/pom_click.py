from selenium.webdriver.common.by import By
from utils.locator_utils import LocatorUtilities
from conftest import save_step_screenshot

from pytest_check import  check
class POM:
    def __init__(self,driver,request):
        self.driver=driver
        self.request = request
        self.click_on_pom=(By.XPATH,"(//a[normalize-space(@class)='card-footer-item'])[1]")
        self.click_on_profile_page=(By.XPATH,"(//button[contains(@class,'button is-pulled-right')])[2]")

    def page_click_on_pom(self):
        result,element =LocatorUtilities.is_element_clickable(self.driver,self.click_on_pom)
        print("ffffffffffffffffffffffffffff",result)
        if result is True:
            element.click()
            save_step_screenshot(self.driver, self.request.node.name, "click_on_pom", self.request.node)
            return True
        return False


    def click_on_profile_icon(self):
        result ,element=LocatorUtilities.is_element_clickable(self.driver,self.click_on_profile_page)
        if result is True:
            element.click()
            save_step_screenshot(self.driver, self.request.node.name, "click_on_pom", self.request.node)
            return True
        return False