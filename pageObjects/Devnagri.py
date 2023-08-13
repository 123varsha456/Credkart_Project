import time

from selenium.webdriver.common.by import By

class Register:
    HomePage_XPATH=(By.XPATH,"//a[contains(@class,'button-blue')]")
    Newuser_XPATH=(By.XPATH,"//div[contains(text(),'New user')]")
    Enter_Firstname_XPATH=(By.XPATH,"//input[@id='first_name']")
    Enter_Lastname_XPATH=(By.XPATH,"//input[@id='last_name']")
    Enter_Email_XPATH=(By.XPATH,"//input[@id='email']")
    Enter_Phonenumber_XPATH=(By.XPATH,"//input[@id='phone']")
    Enter_Organizationname_XPATH = (By.XPATH, "//input[@id='organization_name']")
    Enter_Password_XPATH = (By.XPATH, "//input[@id='password']")
    Enter_Confirmpassword_XPATH = (By.XPATH, "//input[@id='password_confirmation']")
    Enter_Register_Button_XPATH=(By.XPATH,"//button[@type='submit']")


    def __init__(self,driver):
        self.driver=driver

    def Login_URL(self):
        self.driver.get("https://account.devnagri.com/registerThe")

    def HOMEPAGE(self):
        self.driver.find_element(*Register.HomePage_XPATH).click()

    def NEWUSER(self):
        self.driver.find_element(*Register.Newuser_XPATH).click()

    def FIRSTNAME(self,name):
        self.driver.find_element(*Register.Enter_Firstname_XPATH).send_keys(name)

    def LASTNAME(self,name):
        self.driver.find_element(*Register.Enter_Lastname_XPATH).send_keys(name)

    def EMAIL(self,value):
        self.driver.find_element(*Register.Enter_Email_XPATH).send_keys(value)

    def MOBAILNUMBER(self,value):
        self.driver.find_element(*Register.Enter_Phonenumber_XPATH).send_keys(value)

    def ORGANIZATIONNAME(self,name):
        self.driver.find_element(*Register.Enter_Organizationname_XPATH).send_keys(name)

    def PASSWORD(self,value):
        self.driver.find_element(*Register.Enter_Password_XPATH).send_keys(value)

    def CONFIRMPASSWORD(self,value):
        self.driver.find_element(*Register.Enter_Confirmpassword_XPATH).send_keys(value)

    def REGISTERSUCCESSFULL(self):
        try:
            self.driver.find_element(*Register. Enter_Register_Button_XPATH).click()
            return True
        except:
            return False
