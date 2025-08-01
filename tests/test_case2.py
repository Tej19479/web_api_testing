from selenium.webdriver.common.by import By

class Test_ejj2:
    def test_demo(self,driver,):
        driver.get("https://admin.faircent.com/admins/withdraw/wallet/maually")
        driver.find_element(By.ID, "edit-all-amount").click()