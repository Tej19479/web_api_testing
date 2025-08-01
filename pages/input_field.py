from selenium.webdriver.common.by import By
from utils.locator_utils import LocatorUtilities
from selenium.webdriver.common.keys import Keys

class Inputfieldpages:

    
    def __init__(self,driver):
        self.driver=driver
        self.click_to_input_flied= (By.XPATH,"(//a[normalize-space(@class)='card-footer-item'])[2]")
        self.full_name=(By.ID,"fullName")
        self.key_tab=(By.ID,"join")
        self.inside_letter=(By.ID,"getMe")
        self.clear_text=(By.ID,"clearMe")
        self.confrim_edit_button_disabled=(By.ID, "noEdit")
        self.text_field_reable=(By.ID,"dontwrite")

    def click_input_field(self):
        #ele=(By.XPATH,self.click_to_input_flied)
        try:
            print("fffffffffffffffffffffffff",self)
            result=LocatorUtilities.is_element_displayed(self.driver,self.click_to_input_flied)
            if result:
                print("condtion of true case",result)
                status,element=LocatorUtilities.is_element_clickable(self.driver,self.click_to_input_flied)
                print("is element clickable element", status)
                if status is True:
                    element.click()
                    print("is element clickable emelement",result)
                    return True



            else:
               print("faild the select itmes",result)
        except Exception as e:
            print("Raise excetion in input filed clickable",e)
            return  e
    def input_field_data_entered(self, fullname=None, key_value=None):
        print("paramenter field",self , fullname,key_value)
        try:
            # Fill full name if provided
            if fullname is not None:
                status, element = LocatorUtilities.is_element_clickable(self.driver, self.full_name)
                if status:
                    element.clear()
                    element.send_keys(fullname)

            # Fill tab key value if provided
            if key_value is not None:
                status, element = LocatorUtilities.is_element_clickable(self.driver, self.key_tab)
                if status:
                    element.clear()
                    element.send_keys(Keys.TAB)
                    element.send_keys(key_value)

            # Read value of inside_letter
            status, element = LocatorUtilities.is_element_displayed(self.driver, self.inside_letter)
            if status:
                text = element.get_attribute('value')
                print("✅ Value inside 'inside_letter':", text)

            status,element=LocatorUtilities.is_element_clickable(self.driver,self.clear_text)
            if status:
                element.clear()
                print("sucessfull clear the text and clear text",element.get_attribute('value'))
            status,element=LocatorUtilities.is_check_locator_present(self.driver, self.confrim_edit_button_disabled)
            self.driver.execute_script("window.scrollBy(0, 100)")
            print("sttaus-----------------",status)
            if status is False:
                print("button is disbaled ",status)
            else:
                print("button is else case disabaled case",status)
            print("another method two check element is",element.is_enabled())

            status,element=LocatorUtilities.is_check_locator_present(self.driver,self.text_field_reable)

            if status:
                is_readonly= element.get_attribute('readonly')
                print("is readonly",is_readonly)

        except Exception as e:
            print("❌ Exception in input_field_data_entered:", e)
            return False