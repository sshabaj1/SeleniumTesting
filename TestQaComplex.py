import unittest
from selenium import webdriver
import page
from logzero import logger
import logzero
from datetime import datetime
from models import *
import time
from string import ascii_letters, digits
import re
import phonenumbers




logzero.logfile(datetime.now().strftime('TestQaComplex %Y-%m-%d.log'))



class CoffeQaSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r'C:\Users\senad\Documents\Driver\chromedriver.exe')
        self.driver.get('https://www.coffee-qa.perfect-sitebank.com/contact/')


    def test_qa_page_complex(self):
        date_time = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
        scenario_name = 'Test QA Page Complex'
        scenario_status = "Success"
        scenario_message = "Page Tested Without Errors"
        

        
        logger.info('Testing QA Page Complex...')
        qaPage = page.QaPage(self.driver)

        qaPage.enter_full_name = 'First Last'
        full_name = qaPage.enter_full_name.replace(' ', '')
        print(full_name)
        
        for char in qaPage.enter_full_name:
            if len(qaPage.enter_full_name) < 5:
                scenario_status = "Error Occured"
                scenario_message = "The full name must contain a minimum of 5 characters"
                logger.info('Error: The full name must contain a minimum of 5 characters')
            if set(full_name).difference(ascii_letters + digits):
                scenario_status = "Error Occured"
                scenario_message = "The full name must not contain numbers or special characters"
                logger.info('Error: The full name must not contain numbers or special characters')

            else:
                logger.info('Full Name Enterd Successfully')

    
        qaPage.enter_email_adresss = 'testing.test@gmail.com'


        pattern = r"\"?([-a-zA-Z0-9.`?{}]+@\w+\.\w+)\"?" 
    
        email = qaPage.enter_email_adresss

        if not re.match(pattern, email):
            scenario_status = "Error Occured"
            scenario_message = "The email is incorrect"
            logger.info('The email is incorrect')            
        else:
            logger.info('Email Enterd Successfully')


        qaPage.enter_mailing_address = 'Tirana, Zogi Zi'

        if len(qaPage.enter_mailing_address) < 10:
            scenario_status = "Error Occured"
            scenario_message = "The mailing adress is not completed"
            logger.info('Error: The mailing adress is not completed')
        else:
            logger.info('Address Enterd Successfully')

    
        qaPage.enter_phone_number = '+355684634347'
        my_number = phonenumbers.parse(qaPage.enter_phone_number, "AL")

        if phonenumbers.is_valid_number(my_number):
            logger.info('Phone Number Enterd Successfully')
            
        else:
            scenario_status = "Error Occured"
            scenario_message = "The phone number is not correct"
            logger.info('Error: The phone number is not correct')
            
    
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