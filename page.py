from locator import *
from element import BasePageElement


class EnterFullName(BasePageElement):
    locator = 'p_name'
    

class EnterEmailAddress(BasePageElement):
    locator = 'p_email'

class EnterMailingAddress(BasePageElement):
    locator = 'p_subject'

class EnterPhoneNumber(BasePageElement):
    locator = 'p_phone'

class BasePage():
    def __init__(self, driver):
        self.driver = driver

class QaPage(BasePage):
    enter_full_name = EnterFullName()
    enter_email_adresss = EnterEmailAddress()
    enter_mailing_address = EnterMailingAddress()
    enter_phone_number = EnterPhoneNumber()
    

    def click_send_message_button(self):
        element = self.driver.find_element(*QaPageLocators.SEND_MESSAGE_BUTTON)
        element.click()

