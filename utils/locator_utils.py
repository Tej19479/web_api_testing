from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import NoSuchElementException,ElementClickInterceptedException, TimeoutException

class LocatorUtilities:
    @staticmethod
    def is_element_displayed(driver, locator, timeout=10):
          print("🔍 Checking visibility of element:", locator)
          try:
           element = WebDriverWait(driver, timeout).until(
            EC.presence_of_element_located(locator)
           )
           is_displayed = element.is_displayed()
           print("✅ Element found. Displayed:", is_displayed)
           return is_displayed,element
          except TimeoutException:
           print("⏰ Timeout: Element not found within", timeout, "seconds.")
           return False
          except NoSuchElementException:
           print("❌ No such element found.")
           return False
          except Exception as e:
           print("❌ Unexpected error:", e)
           return False
    @staticmethod

    def is_element_clickable(driver, locator, timeout=10):
         print("🔍 Checking if element is clickable:", locator)
         try:
          element=WebDriverWait(driver, timeout).until(
           EC.element_to_be_clickable(locator)
          )
          print("✅ Element is clickable.")
          return True,element
         except TimeoutException:
          print("⏰ Element not clickable within timeout.")
          return False
         except Exception as e:
          print("❌ Unexpected error while checking clickable status:", e)
          return False
         
    @staticmethod
    def is_check_locator_present(driver, locator, timeout=10):
        try:
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located(locator)
            )
            return True, element
        except Exception as e:
            print("❌ Unexpected error while checking locator presence:", e)
            return False, None