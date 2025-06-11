from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time


from Locator.login_page import LoginLocators

class LoginPage:
    Locators = LoginLocators()
    Data = {}
    def __init__(self, driver):
        self.driver = driver


    def signin(self):
        self.driver.find_element(*LoginPage.Locators.SingInPage).click()

    def email_input(self):
        time.sleep(3)
        email='tryingautomationamazon@gmail.com'
        self.driver.find_element(*LoginPage.Locators.email_input).send_keys(email)

    def ConinuteBtn(self):
        time.sleep(3)
        self.driver.find_element(*LoginPage.Locators.ConinuteBtn).click()
    def PasswordInput(self):
        time.sleep(3)
        password='tryingautomation'
        element=self.driver.find_element(*LoginPage.Locators.PasswordInput)
        element.send_keys(password)
        element.send_keys(Keys.RETURN)

    def Search(self):
        time.sleep(3)
        item='earphones noise wire'
        element=self.driver.find_element(*LoginPage.Locators.Search)
        element.send_keys(item)
        element.send_keys(Keys.RETURN)

    def AddToCart(self):
        time.sleep(3)
        self.driver.find_element(*LoginPage.Locators.AddToCart).click()

    def NavigateToCart(self):
        time.sleep(3)
        self.driver.find_element(*LoginPage.Locators.NavigateToCart).click()

    def ProceedToBuy(self):
        time.sleep(3)
        self.driver.find_element(*LoginPage.Locators.ProceedToBuy).click()

    def COD(self):
        time.sleep(3)
        self.driver.find_element(*LoginPage.Locators.COD).click()
    def PaymentMethod(self):
        time.sleep(3)
        self.driver.find_element(*LoginPage.Locators.PaymentMethod).click()

    def ConfirmOrder(self):
        time.sleep(3)
        self.driver.find_element(*LoginPage.Locators.ConfirmOrder).click()