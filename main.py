import unittest
from selenium import webdriver
import page
from logzero import logger
import logzero
from datetime import datetime
from models import *

logzero.logfile(datetime.now().strftime('%Y-%m-%d.log'))



class CoffeQaSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r'C:\Users\senad\Documents\Driver\chromedriver.exe')
        self.driver.get('https://www.coffee-qa.perfect-sitebank.com/contact/')


    def test_qa_page_easy(self):
        date_time = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
        scenario_name = 'Test QA Page Easy'
        scenario_status = 'Error Occurred'
        scenario_message = 'An error occurred'


        logger.info('Testing QA Page Easy...')
        qaPage = page.QaPage(self.driver)
        

        qaPage.enter_full_name = 'First Last'
        print(f'Full Name Is: ', qaPage.enter_full_name)
        logger.info('First Name Enterd Successfully')
        

        qaPage.enter_email_adresss = 'test.mail@gmail.com'
        print(f'Email Is: ', qaPage.enter_email_adresss)
        logger.info('Email Enterd Successfully')
        

        qaPage.enter_mailing_address = 'Tirana, Zogi Zi'
        print(f'Mailing Adress Is: ', qaPage.enter_mailing_address)
        logger.info('Address Enterd Successfully')

        qaPage.enter_phone_number = '+355 000 000 000'
        print(f'Phone Number Is: ', qaPage.enter_phone_number)
        logger.info('Phone Number Enterd Successfully')

        qaPage.click_send_message_button()
        print('Send Message Button Clicked Successfully')
        logger.info('Send Message Button Clicked Successfully')
        scenario_status = "Success"
        scenario_message = 'Page Tested Without Errors'

        cursor.execute("""INSERT INTO Testing (
            datetime,
            scenario_name,
            scenario_status,
            scenario_message
            ) VALUES (?,?,?,?)""", (date_time, scenario_name, scenario_status, scenario_message))
        db.commit()
        


    def tearDown(self):
        self.driver.close()

    

if __name__ == '__main__':
    unittest.main()