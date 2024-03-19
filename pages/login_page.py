from browser import Browser
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException
import time

class LoginPage(Browser):

    EMAIL_INPUT = (By.NAME, "email")
    PAROLA = (By.ID, "password")
    LOGIN_BUTTON = (By.XPATH, "//span[contains(text(),'Login')]")
    AI_UITAT_PAROLA_BUTTON = (By.XPATH,"//a[@class='txt-form']")
    COOKIE_BUTTON = (By.ID, "CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll")
    NOTIFICATION_MESSAGE = (By.CLASS_NAME, "invalid-feedback")

    def navigate_to_login_page(self):
        self.driver.get("https://www.tiriacauto.ro/contul-meu")

    def click_accept_cookie(self):
        msg_exp = "Accept toate cookie-urile"
        try:
            act_msg = self.driver.find_element(*self.COOKIE_BUTTON).text
        except NoSuchElementException:
            act_msg = "None"
        if msg_exp == act_msg:
             self.driver.find_element(*self.COOKIE_BUTTON).click()
             time.sleep(5)
        else:
            pass


    def set_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)

    def set_password(self, password):
        self.driver.find_element(*self.PAROLA).send_keys(password)

    def click_login_button(self):
        self.driver.find_element(*self.LOGIN_BUTTON).click()

    def click_ai_uitat_parola(self):
        self.driver.find_element(*self.AI_UITAT_PAROLA_BUTTON).click()

    def verify_mesaj_eroare(self,expected_message):
        try:
            actual_message = self.driver.find_element(*self.NOTIFICATION_MESSAGE).text
        except NoSuchElementException:
            actual_message = "None"

        assert actual_message == expected_message, f'Error, the message is incorrect'


    def curent_url(self, expected_url):
        try:
            actual_url = self.driver.current_url
        except NoSuchElementException:
            actual_url = "None"
        assert actual_url == expected_url, f'Error, the message is incorrect'