import time

from pageObjects.Devnagri import Register

class Test_register_001:
    def test_devnagriregister(self,setup):
        self.driver=setup
        self.rg=Register(self.driver)
        time.sleep(2)
        self.rg.Login_URL()
        self.rg.HOMEPAGE()
        self.rg.NEWUSER()
        time.sleep(2)
        self.rg.FIRSTNAME("Varsha")
        self.rg.LASTNAME("Bhalkhede")
        self.rg.EMAIL("varshabhalkhede@gmail.com")
        self.rg.MOBAILNUMBER("8237272195")
        self.rg.ORGANIZATIONNAME("Credence")
        self.rg.PASSWORD("Varsharani@123")
        self.rg.CONFIRMPASSWORD("Varsharani@123")


        if self.rg.REGISTERSUCCESSFULL()==True:
            self.driver.save_screenshot("screenSHOTS\\test_devnagriregister_pass.PNG")
            assert True
        else:
            self.driver.save_screenshot("screenSHOTS\\test_devnagriregister_fail.PNG")
            assert False




