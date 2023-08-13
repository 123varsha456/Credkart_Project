import time

##Yane Run kra---
# pytest -v --html=Reports/myreport.html --alluredir="AllureReports" testCases/test_CheckOut.py --browser chrome

from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from pageObjects.LoginPage import Login
from pageObjects.CheckOutPage import CredKart_CheckOut


class Test_CredKart_CheckOut:

    def test_checkout(self, setup):
        self.driver = setup
        self.lp = Login(self.driver)
        self.lp.Login_URL()
        self.lp.Enter_Email("Credencetest@test.com")
        self.lp.Enter_Password("Credence@123")
        self.lp.CLick_Login_Button()
        self.cop = CredKart_CheckOut(self.driver)
        # Click on Product--Macbook
        self.cop.Click_MacBook()
        # Click on add to cart
        self.cop.Add_to_Cart()
        self.cop.Proceed_Checkout()
        self.cop.First_Name("Credence")
        self.cop.Last_Name("Pune")
        self.cop.Phone_Number("9091929355")
        self.cop.Address("Dhankawdi, Pune")
        self.cop.Zip("411013")
        self.cop.State("Pune")
        self.cop.OwnerName("Tushar")
        self.cop.CVV("043")
        self.cop.Year("2024")
        self.cop.Month("feb")
        self.cop.CardNumber1("5281")
        self.cop.CardNumber2("0370")
        self.cop.CardNumber3("4891")
        self.cop.CardNumber4("6168")
        self.cop.CheckOut_Button()
        self.cop.Get_CardOrder_No()
        if self.lp.Login_Status()==True:
            # self.driver.save_screenshot("screenSHOTS\\test_checkout_pass.PNG")
            assert True
        else:
            # self.driver.save_screenshot("screenSHOTS\\test_checkout_fail.PNG")
            assert False




        ##Ya khalch as linyaaivji as vrchya sarkh lihitat pageObjects mdhe

        # self.driver.find_element(By.XPATH, "//input[@value='Add to Cart']").click()
        # Proceed to Checkout
        # self.driver.find_element(By.XPATH, "//a[@class='btn btn-success btn-lg']").click()
        # time.sleep(3)
        # # Enter First_Name
        # self.driver.find_element(By.XPATH, "//input[@id='first_name']").send_keys(Crede"nce")
        # # Enter Last_Name
        # self.driver.find_element(By.XPATH, "//input[@id='last_name']").send_keys("Pune")
        # # Enter Phone
        # self.driver.find_element(By.XPATH, "//input[@id='phone']").send_keys("9091929355")
        # # Enter Address
        # self.driver.find_element(By.XPATH, "//textarea[@id='address']").send_keys("Dhankawdi, Pune")
        # # Enter Zip
        # self.driver.find_element(By.XPATH, "//input[@id='zip']").send_keys("411013")
        # # Select state
        # state = Select(self.driver.find_element(By.XPATH, "//select[@id='state']"))
        # state.select_by_visible_text("Pune")
        # # Enter  Owner name
        # self.driver.find_element(By.XPATH, "//input[@id='owner']").send_keys("Tushar")
        # # Enter CVV
        # self.driver.find_element(By.XPATH, "//input[@id='cvv']").send_keys("043")
        #
        # # Select Year
        # year = Select(self.driver.find_element(By.XPATH, "//select[@id='exp_year']"))
        # year.select_by_index(2)
        #
        # # Select Month
        # month = Select(self.driver.find_element(By.XPATH, "//select[@id='exp_month']"))
        # month.select_by_index(2)
        #
        # # Enter card number\
        # # 5281 0370 4891 6168
        # self.driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("5281")
        # self.driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("0370")
        # self.driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("4891")
        # self.driver.find_element(By.XPATH, "//input[@id='cardNumber']").send_keys("6168")
        # # Click on Checkout button
        # self.driver.find_element(By.XPATH, "//button[@id='confirm-purchase']").click()
        #
        # print(self.driver.find_element(By.XPATH, "/html/body/div/div[1]/p[1]").text)
