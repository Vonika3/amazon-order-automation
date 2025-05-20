from selenium.webdriver.common.by import By


class LoginLocators:
    email_input = (By.CSS_SELECTOR, "[id='ap_email_login']")
    SingInPage = (By.CSS_SELECTOR, "[id='nav-link-accountList-nav-line-1']")
    ConinuteBtn = (By.CSS_SELECTOR,"[class='a-button-input']")
    PasswordInput = (By.CSS_SELECTOR,"[type='password']")
    Search = (By.CSS_SELECTOR,"[id='twotabsearchtextbox']")
    AddToCart = (By.CSS_SELECTOR,"[name='submit.addToCart']")
    NavigateToCart = (By.CSS_SELECTOR,"[id='nav-cart-count']")
    ProceedToBuy = (By.CSS_SELECTOR,"[name='proceedToRetailCheckout']")
    COD = (By.CSS_SELECTOR,"[value='instrumentId=0h_PE_CUS_18b1c868-2e63-40e2-8b24-414fe05d88c8%2FCash&isExpired=false&paymentMethod=COD&tfxEligible=false']")
    PaymentMethod = (By.CSS_SELECTOR,"[data-testid='bottom-continue-button']")
    ConfirmOrder = (By.CSS_SELECTOR,"[id='submitOrderButtonId']")