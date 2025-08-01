import pytest
from pages.input_field import Inputfieldpages
class Test_111:

  def test_add(self,driver,base_url):
   try:
        driver.get(base_url)
        print("deriver------",driver.title)
        inputfieldes=Inputfieldpages(driver)
        assert "Workspace | LetCode with Koushik" in driver.title  # Optional: validate page loaded
        status=inputfieldes.click_input_field()
        print("in test case run",status)

        if status is True:
          print("print proceed to further")
          data = {
              "fullname": "Tej",
              "key_value": "TabKey"
          }
          print("i am tej paratta singh")
          print("datatta",data)
          inputfieldes.input_field_data_entered(**data)
   except Exception as e:
        print("error appearing in the inputfield click testcase",e)
