from selenium.webdriver.common.by import By
from utils.locator_utils import  LocatorUtilities
from conftest import save_step_screenshot
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Login:
    def __init__(self,driver,request):
        self.request=request
        self.driver = driver
        self.username=(By.XPATH,"(//input[contains(@class,'input ng-untouched')])[1]")
        self.password=(By.XPATH,"(//input[contains(@class,'input ng-untouched')])[2]")
        self.click_login_button=(By.XPATH,"//button[text()='Login']")

    def login_data_centdrails(self,username=None,password=None):
        status,element= LocatorUtilities.is_check_locator_present(self.driver,self.username)
        if status is True:
            element.clear()
            element.send_keys(username)
            save_step_screenshot(self.driver, self.request.node.name, "click_user_name", self.request.node)
        status,element=LocatorUtilities.is_check_locator_present(self.driver,self.password)
        if status:
            element.clear()
            element.send_keys(password)
        status, element = LocatorUtilities.is_element_clickable(self.driver, self.click_login_button)
        save_step_screenshot(self.driver, self.request.node.name, "before clicking login buttom", self.request.node)
        if status:
            element.click()
            save_step_screenshot(self.driver, self.request.node.name, "after clicking login buttom", self.request.node)
            return True
        return False