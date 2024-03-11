from selenium.common import NoSuchElementException
from browser import Browser
from selenium.webdriver.common.by import By
import time


class AiUitatParolaPage(Browser):

    EMAIL_INPUT = (By.ID, "email")
    BUTON_TRIMITE = (By.XPATH, "/html/body/main/div/div/div/div/div[1]/form/button")
    NOTIFICATION_MESSAGE = (By.CLASS_NAME, "invalid-feedback")

    def navigate_to_forgot_password_page(self):
        self.driver.get("https://www.tiriacauto.ro/password/reset")

    def set_email(self, email):
        self.driver.find_element(*self.EMAIL_INPUT).send_keys(email)
        time.sleep(10)

    def click_buton_trimite(self):
        self.driver.find_element(*self.BUTON_TRIMITE).click()
        time.sleep(10)

    def clean_email_text_field(self):
        self.driver.find_element(*self.EMAIL_INPUT).clear()

    def verify_mesaj_eroare(self,expected_message):
        try:
            actual_message = self.driver.find_element(*self.NOTIFICATION_MESSAGE).text
        except NoSuchElementException:
            actual_message = "None"

        assert actual_message == expected_message, f'Error, the message is incorrect'

        time.sleep(10)