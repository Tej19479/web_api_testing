from selenium.webdriver.common.by import By


class CHECKOUT:
    def __init__(self,driver, request):
        self.checkout_button_click=(By.XPATH,"//button[text()='Checkout']")
        self.driver=driver
        self.request=request
        self.plus_button=(By.XPATH,"//button[text()='+']")
        self.minus_button=(By.XPATH,"//button[text()='+']")
        self.deleted_button=(By.XPATH,"//button[contains(@class,'is-danger')]")