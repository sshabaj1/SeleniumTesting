import unittest
from selenium import webdriver
import page
from logzero import logger
import logzero
from datetime import datetime
from models import *
import time



logzero.logfile(datetime.now().strftime('TestQaMedium %Y-%m-%d.log'))



class CoffeQaSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r'C:\Users\senad\Documents\Driver\chromedriver.exe')
        self.driver.get('https://www.coffee-qa.perfect-sitebank.com/contact/')


    def test_qa_page_medium(self):
        date_time = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
        scenario_name = 'Test QA Page Medium'
        scenario_status = "Success"
        scenario_message = "Page Tested Without Errors"
        

        
        logger.info('Testing QA Page Medium...')
        qaPage = page.QaPage(self.driver)

        qaPage.enter_full_name = 'First Last'
        
        for char in qaPage.enter_full_name:
            if char.isdigit():
                scenario_status = "Error Occured"
                scenario_message = "The first name must not contain numbers"
                logger.info('Error: First name must not contain numbers')
            else:
                logger.info('First Name Enterd Successfully')

    
        qaPage.enter_email_adresss = 'testing.test@gmail.com'

        if len(qaPage.enter_email_adresss) < 10:
            scenario_status = "Error Occured"
            scenario_message = "The email cannot be with less than 10 characters"
            logger.info('Error: The email cannot be with less than 10 characters')
        else:
            logger.info('Email Enterd Successfully')


        qaPage.enter_mailing_address = 'Tirana, Zogi Zi'

        if len(qaPage.enter_mailing_address) < 10:
            scenario_status = "Error Occured"
            scenario_message = "The mailing adress is not completed"
            logger.info('Error: The mailing adress is not completed')
        else:
            logger.info('Address Enterd Successfully')

    
        qaPage.enter_phone_number = '+355 000 000'
        if len(qaPage.enter_phone_number) < 10:
            scenario_status = "Error Occured"
            scenario_message = "The phone number is not correct"
            logger.info('Error: The phone number is not correct')
        else:
            logger.info('Phone Number Enterd Successfully')
    
        qaPage.click_send_message_button()
        logger.info('Send Message Button Clicked Successfully')
        
        
        cursor.execute("""INSERT INTO Testing (
            datetime,
            scenario_name,
            scenario_status,
            scenario_message
            ) VALUES (?,?,?,?)""", (date_time, scenario_name, scenario_status, scenario_message))
        db.commit()

        time.sleep(3)
    


    def tearDown(self):
        self.driver.close()

    

if __name__ == '__main__':
    unittest.main()