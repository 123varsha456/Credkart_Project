from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By


class CredKart_CheckOut:
    Click_Product_MacBook_XPATH = (By.XPATH, "/html/body/div/div[2]/div[3]/div/div/a[2]/h3")
    Click_AddToCart_XPATH = (By.XPATH, "//input[@value='Add to Cart']")
    Click_ProceedToCheckOut_XPATH = (By.XPATH, "//a[@class='btn btn-success btn-lg']")
    Enter_First_Name_XPATH = (By.XPATH, "//input[@id='first_name']")
    Enter_Last_Name_XPATH = (By.XPATH, "//input[@id='last_name']")
    Enter_Phone_XAPTH = (By.XPATH, "//input[@id='phone']")
    Enter_Address_XAPTH = (By.XPATH, "//textarea[@id='address']")
    Enter_Zip_XPATH = (By.XPATH, "//input[@id='zip']")
    DropDown_State_XPATH = (By.XPATH, "//select[@id='state']")
    Enter_Owner_Name_XPATH = (By.XPATH, "//input[@id='owner']")
    Enter_CVV_XPATH = (By.XPATH, "//input[@id='cvv']")
    DropDown_Year_XPATH = (By.XPATH, "//select[@id='exp_year']")
    DropDown_Month_XPATH = (By.XPATH, "//select[@id='exp_month']")
    Enter_Card_Number_XPATH = (By.XPATH, "//input[@id='cardNumber']")
    Click_Checkout_XPATH = (By.XPATH, "//button[@id='confirm-purchase']")
    Success_Message = (By.XPATH, "/html/body/div/div[1]/p[1]")
    Get_order_no=(By.CSS_SELECTOR,"body > div:nth-child(2) > div:nth-child(1) > p:nth-child(3) > a:nth-child(1)")
    Click_Homepage_XPATH=(By.XPATH,"//a[@class='navbar-brand']")


    def __init__(self, driver):
        self.driver = driver

    def Click_MacBook(self):
        self.driver.find_element(*CredKart_CheckOut.Click_Product_MacBook_XPATH).click()

    def Add_to_Cart(self):
        self.driver.find_element(*CredKart_CheckOut.Click_AddToCart_XPATH).click()

    def Proceed_Checkout(self):
        self.driver.find_element(*CredKart_CheckOut.Click_ProceedToCheckOut_XPATH).click()

    def First_Name(self,fname):
        self.driver.find_element(*CredKart_CheckOut.Enter_First_Name_XPATH ).send_keys(fname)

    def Last_Name(self, lname):
        self.driver.find_element(*CredKart_CheckOut.Enter_Last_Name_XPATH).send_keys(lname)

    def Phone_Number(self,number):
        self.driver.find_element(*CredKart_CheckOut.Enter_Phone_XAPTH).send_keys(number)

    def Address(self,address):
        self.driver.find_element(*CredKart_CheckOut.Enter_Address_XAPTH).send_keys(address)

    def Zip(self,code):
        self.driver.find_element(*CredKart_CheckOut.Enter_Zip_XPATH).send_keys(code)

    def State(self,city):
        self.driver.find_element(*CredKart_CheckOut.DropDown_State_XPATH).send_keys(city)
    def OwnerName(self,name):
        self.driver.find_element(*CredKart_CheckOut.Enter_Owner_Name_XPATH).send_keys(name)
    def CVV(self,number):
        self.driver.find_element(*CredKart_CheckOut.Enter_CVV_XPATH).send_keys(number)
    def Year(self,value):
        self.driver.find_element(*CredKart_CheckOut.DropDown_Year_XPATH).send_keys(value)
    def Month(self,name):
        self.driver.find_element(*CredKart_CheckOut.DropDown_Month_XPATH).send_keys(name)
    def CardNumber1(self,number):
        self.driver.find_element(*CredKart_CheckOut.Enter_Card_Number_XPATH).send_keys(number)
    def CardNumber2(self,number):
        self.driver.find_element(*CredKart_CheckOut.Enter_Card_Number_XPATH).send_keys(number)
    def CardNumber3(self,number):
        self.driver.find_element(*CredKart_CheckOut.Enter_Card_Number_XPATH).send_keys(number)
    def CardNumber4(self,number):
        self.driver.find_element(*CredKart_CheckOut.Enter_Card_Number_XPATH).send_keys(number)
    def CheckOut_Button(self):
        self.driver.find_element(*CredKart_CheckOut. Click_Checkout_XPATH).click()
    def Order_Status(self):
        try:
            self.driver.find_element(*CredKart_CheckOut.Success_Message)
            return True
        except:
            return False

    def Get_CardOrder_No(self):
        try:
          OrderNumber=self.driver.find_element(*CredKart_CheckOut.Get_order_no).text
          return OrderNumber
        except NoSuchElementException:
            pass

    def Click_HomePage(self):
        self.driver.find_element(*CredKart_CheckOut.Click_Homepage_XPATH).click()



