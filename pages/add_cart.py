import time

from selenium.webdriver.common.by import By
from utils.locator_utils import LocatorUtilities
from conftest import save_step_screenshot


from selenium.webdriver.common.action_chains import ActionChains



class ADDCARD:
    def __init__(self, driver, request,product_name):
        self.product_name=product_name
        self.driver = driver
        self.request = request
        self.add_button_click = (By.XPATH, "//span[text()='Add to Cart']")
        self.add_cart_after_message_appear = (By.XPATH, "//div[contains(@class,'mdc-snackbar__label')]")
        self.cart_click_icon = (By.XPATH, "(//button[contains(@class,'is-pulled-right')])[1]")
        self.display_locator = (
            By.XPATH,
            f"//div[contains(@class,'ng-star-inserted')]/descendant::div[@class='card']//p[contains(text(),'{self.product_name}')]"
        )
        self.display_locator111 = (
            By.XPATH,
            f"//div[contains(@class,'ng-star-inserted')]/descendant::div[@class='card']//p[contains(text(),'{self.product_name}')]"
        )
        self.btn=(By.XPATH,"//p[contains(@class,'card-header-title') and contains(text(),'Fjallraven - Foldsack No. 1 Ba...')]/ancestor::div[contains(@class,'card')]//button[contains(@class,'button') and contains(@class,'is-link') and contains(@class,'is-fullwidth')]")
        self.btn_locator = (
            By.XPATH,
            f"//p[contains(@class,'card-header-title') and contains(text(),'{self.product_name}')]/ancestor::div[contains(@class,'card')]//button[contains(@class,'button') and contains(@class,'is-link') and contains(@class,'is-fullwidth')]"
        )


    def product_select(self, product_name=None):
        #display_locator = self.get_display_product_cart(product_name)
       # print("display locator of product",self.display_locator)

        status, ele = LocatorUtilities.is_element_displayed(self.driver, self.display_locator)
        print("click is done", status)
        time.sleep(10)
        if status:
            # ele.click()
            # print("click is done display_locator",status)
            status, btn_locator_ele = LocatorUtilities.is_element_clickable(self.driver, self.btn_locator)
            if status:
              print("clickable is  btn_locator", btn_locator_ele)
              #btn_locator_ele.click()
              print("clickable is  before btn_locator", btn_locator_ele)
              self.driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", btn_locator_ele)
              self.driver.execute_script("arguments[0].style.border='3px solid red'", btn_locator_ele)

              # actions = ActionChains(self.driver)
              # actions.double_click(btn_locator_ele).perform()
              try:
                  btn_locator_ele.click()  # or use JS if needed
                  print("Button clicked successfully")
                  time.sleep(1)
                  save_step_screenshot(self.driver, self.request.node.name, "click on product button", self.request.node)
                  print("after is done btn_locator", self.btn_locator)

              except Exception as e:
                  print("Standard click failed, trying JS click:", e)
                  self.driver.execute_script("arguments[0].click();", btn_locator_ele)
              time.sleep(20)
        else:
            print("Failed to locate product name:", product_name)

        status, ele = LocatorUtilities.is_element_clickable(self.driver, self.add_button_click)
        if status:
            ele.click()
            save_step_screenshot(self.driver, self.request.node.name, "add button click", self.request.node)
            status, ele = LocatorUtilities.is_check_locator_present(self.driver, self.add_cart_after_message_appear)
            if status:
                after_select_message = ele.text
                print("Message after item selection:", after_select_message)

        status, ele = LocatorUtilities.is_element_clickable(self.driver, self.cart_click_icon)
        if status:
            ele.click()
            save_step_screenshot(self.driver, self.request.node.name, "click on cart button", self.request.node)
            time.sleep(10)
        else:
            print("profile button is not click")