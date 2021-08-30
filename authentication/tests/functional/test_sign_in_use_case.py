# pylint: disable=C0116
"""Test module for sign in use case functional test
"""
from time import sleep

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from webdrivermanager.edge import EdgeDriverManager

from authentication.tests.unit.models.test_custom_user import CustomUserTest
# from pur_beurre.custom_settings import *

class SignInUseCaseTest(StaticLiveServerTestCase):
    """Sign in use case test class
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser = webdriver.Edge(r'/home/travis/build/ThomasPiergiovanni/P10/msedgedriver.exe')
        cls.browser.implicitly_wait(10)
        CustomUserTest.emulate_custom_user()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def setUp(self):
        # The user logs to the sign up page
        self.browser.get(
            '%s%s' % (
                self.live_server_url,
                '/authentication/sign_in/'
            )
        )

    def test_sign_in_use_case(self):
        # The user types its email and password.
        sleep(2)
        self.browser.find_element_by_id('id_signin_email_input')\
            .send_keys('testuser@email.com')
        sleep(1)
        self.browser.find_element_by_id('id_signin_password_input')\
            .send_keys('_Xxxxxxx')
        sleep(1)

        # The user clicks then "Se connecter" button and lands on the
        # home page.
        self.browser.find_element_by_id('id_sign_in_button').click()
        self.assertIn(
            'DU GRAS, OUI MAIS DE QUALITÉ',
            self.browser.find_element_by_tag_name('h1').text
        )
        sleep(1)
