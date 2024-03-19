from browser import Browser
from selenium.webdriver.common.by import By
from selenium.common import NoSuchElementException


class AcountPage(Browser):

    DECONECTEAZA_BUTTON = (By.CLASS_NAME, "logout-btn")
    INFORMATII_PERSONALE_BUTTON = (By.XPATH, "//div[contains(text(),'Informatii personale')]")
    NUME_FIELD = (By.ID, "lastname")
    TRIMITE_BUTTON = (By.XPATH, "//span[contains(text(),'Trimite')]")
    PRENUME_FIELD = (By.ID, "firstname")
    MASINILE_MELE_BUTTON = (By.XPATH, "//div[contains(text(),'Masinile mele')]")
    NO_MACHINE_MESSAGE = (By.XPATH, "//div[@class='col-12 bg-white']")

    def click_logout_button(self):
        self.driver.find_element(*self.DECONECTEAZA_BUTTON).click()

    def click_informatii_persoanle_button(self):
        self.driver.find_element(*self.INFORMATII_PERSONALE_BUTTON).click()

    def field_name_change(self, nume):
        self.driver.find_element(*self.NUME_FIELD).clear()
        self.driver.find_element(*self.NUME_FIELD).send_keys(nume)

    def click_trimite_button(self):
        self.driver.find_element(*self.TRIMITE_BUTTON).click()

    def field_firstname_change(self, prenume):
            self.driver.find_element(*self.PRENUME_FIELD).clear()
            self.driver.find_element(*self.PRENUME_FIELD).send_keys(prenume)

    def click_masinile_mele_button(self):
        self.driver.find_element(*self.MASINILE_MELE_BUTTON).click()

    def verify_machine_mesage(self, expected_message):
        try:
            actual_message = self.driver.find_element(*self.NO_MACHINE_MESSAGE).text
        except NoSuchElementException:
            actual_message = "None"

        assert actual_message == expected_message, f'Exista masina inregistrata'

