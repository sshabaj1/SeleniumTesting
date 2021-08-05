import unittest
from selenium import webdriver
import page
from logzero import logger
import logzero
from datetime import datetime
from models import *
import time



logzero.logfile(datetime.now().strftime('TestQaEasy %Y-%m-%d.log'))



class CoffeQaSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome(r'C:\Users\senad\Documents\Driver\chromedriver.exe')
        self.driver.get('https://www.coffee-qa.perfect-sitebank.com/contact/')


    def test_qa_page_easy(self):
        date_time = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')
        scenario_name = 'Test QA Page Easy'
        

        
        logger.info('Testing QA Page Easy...')
        qaPage = page.QaPage(self.driver)

        qaPage.enter_full_name = 'First Last'
        logger.info('First Name Enterd Successfully')
    
        qaPage.enter_email_adresss = 'test.mail@gmail.com'
        logger.info('Email Enterd Successfully')
    
        qaPage.enter_mailing_address = 'Tirana, Zogi Zi'
        logger.info('Address Enterd Successfully')
    
        qaPage.enter_phone_number = '+355 000 000 000'
        logger.info('Phone Number Enterd Successfully')
    
        qaPage.click_send_message_button()
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

        time.sleep(3)


    


    def tearDown(self):
        self.driver.close()

    

if __name__ == '__main__':
    unittest.main()