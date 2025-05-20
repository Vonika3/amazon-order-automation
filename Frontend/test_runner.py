import time
import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from Helper.utils import LoginPage

class TestRunner:
    @pytest.fixture(scope="class")
    def test_setup_class(self,request):
        service = Service("/Users/vonika./Desktop/New/amazon-order-automation/Driver/chromedriver")
        driver = webdriver.Chrome(service=service)
        driver.get("https://www.amazon.in")
        request.cls.driver = driver
        request.cls.login = LoginPage(driver)
        yield
        driver.quit()

    @pytest.mark.usefixtures("test_setup_class")
    def test_login_to_amazon(self):
        time.sleep(3)
        self.login.signin()
        self.login.email_input()
        self.login.ConinuteBtn()
        self.login.PasswordInput()
        self.login.Search()
        self.login.AddToCart()
        self.login.NavigateToCart()
        self.login.ProceedToBuy()
        self.login.COD()
        self.login.PaymentMethod()
        self.login.ConfirmOrder()
        time.sleep(10)


