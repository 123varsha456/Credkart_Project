from pageObjects.CheckOutPage import CredKart_CheckOut
from pageObjects.LoginPage import Login
from utilities import XLutils


class Test_Chekout:
    excelCheckout_path = "D:\\Cred_Kart_Project_Copy\\TestData\\CheckOutTestData1.xlsx"

    def test_checkout_ddt(self,setup):
        self.driver=setup
        self.lp=Login(self.driver)
        self.lp.Login_URL()
        self.lp.Enter_Email("Credencetest@test.com")
        self.lp.Enter_Password("Credence@123")
        self.lp.CLick_Login_Button()
        self.cop=CredKart_CheckOut(self.driver)

        Order_number=[]
        self.rows=XLutils.RowCount(self.excelCheckout_path,"Sheet1")

        for r in range(2,self.rows+1):

            self.First_name = XLutils.ReadData(self.excelCheckout_path,"Sheet1",r,2)
            self.Last_name=XLutils.ReadData(self.excelCheckout_path,"Sheet1",r,3)
            self.Phone_no=XLutils.ReadData(self.excelCheckout_path,"Sheet1",r,4)
            self.Address=XLutils.ReadData(self.excelCheckout_path,"Sheet1",r,5)
            self.Zip=XLutils.ReadData(self.excelCheckout_path,"Sheet1",r,6)
            self.State=XLutils.ReadData(self.excelCheckout_path,"Sheet1",r,7)
            self.Owner_no=XLutils.ReadData(self.excelCheckout_path,"Sheet1",r,8)



            self.cop.Click_MacBook()
            self.cop.Add_to_Cart()
            self.cop.Proceed_Checkout()
            self.cop.First_Name(self.First_name)
            self.cop.Last_Name(self.Last_name)
            self.cop.Phone_Number(self.Phone_no)
            self.cop.Address(self.Address)
            self.cop.Zip(self.Zip)
            self.cop.State(self.State)
            self.cop.OwnerName("Tushar")
            self.cop.CVV("043")
            self.cop.Year("2024")
            self.cop.Month("May")
            self.cop.CardNumber1("5281")
            self.cop.CardNumber2("0370")
            self.cop.CardNumber3("4891")
            self.cop.CardNumber4("6168")
            self.cop.CheckOut_Button()
            if self.cop.Order_Status()==True:
              Order_number.append(self.cop.Get_CardOrder_No())
              XLutils.WriteData(self.excelCheckout_path,"Sheet1",2,9,self.cop.Get_CardOrder_No())

            else:
             pass
            self.cop.Click_HomePage()

        print(len(Order_number))
        print(Order_number)
        if len(Order_number)==(self.rows-1):
            assert True
        else:
            assert False







