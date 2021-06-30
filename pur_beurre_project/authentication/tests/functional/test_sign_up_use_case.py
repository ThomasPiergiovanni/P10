"""Module for sign up use case functional test
"""
from time import sleep

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver


class SignUpUseCaseTest(StaticLiveServerTestCase):
    """Sign up use case test class
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser = webdriver.Edge(
            'C:\Program Files\EdgeDriver\msedgedriver.exe'
        )
        cls.browser.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()
    
    def setUp(self):
        # The user logs to the sign up page
        self.browser.get(
            '%s%s' % (
                self.live_server_url,
                '/authentication/sign_up/'
            )
        )
    
    def test_sign_up_use_case(self):
        # The user types its first name, email and its password twice in 
        # the form
        sleep(2)
        self.browser.find_element_by_id('id_first_name_input')\
            .send_keys('Testeruser')
        sleep(1)
        self.browser.find_element_by_id('id_email_input')\
            .send_keys('testeruser@email.com')
        sleep(1)
        self.browser.find_element_by_id('id_pwd1_input')\
            .send_keys('_Yyyyyyy')
        sleep(1)
        self.browser.find_element_by_id('id_pwd2_input')\
            .send_keys('_Yyyyyyy')
        sleep(1)

        # The user clicks then "Envoyer" button and lands on the sign in page
        self.browser.find_element_by_id('id_sign_up_button').click()
        self.assertIn(
            'Connection',
            self.browser.find_element_by_tag_name('h2').text
        )
        self.assertTrue(
            self.browser.find_element_by_id('id_signin_email_input')
        )
        self.assertTrue(
            self.browser.find_element_by_id('id_signin_password_input')
        )
        sleep(2)

        
 
