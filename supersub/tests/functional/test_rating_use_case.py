# pylint: disable=C0116, W0611
"""Test rating use case test module. Functional test
"""
import os

from time import sleep

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

from authentication.tests.unit.models.test_custom_user import CustomUserTest
from supersub.tests.unit.models.test_category import CategoryTest
from supersub.tests.unit.models.test_product import ProductTest


class RatingUseCaseTest(StaticLiveServerTestCase):
    """Test rating use case test class
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        firefox_options = webdriver.FirefoxOptions()
        if os.name == 'nt':
            firefox_options.headless = False
            cls.browser = webdriver.Firefox(
                executable_path=str(
                    r'D:\02_oc\10_p10\pur_beurre'
                    r'\custom_settings\geckodriver.exe'
                ),
                options=firefox_options,
            )
        if os.name == 'posix':
            firefox_options.headless = True
            cls.browser = webdriver.Firefox(
                executable_path=str('/usr/local/bin/geckodriver'),
                options=firefox_options,
            )
        cls.browser.implicitly_wait(30)
        CategoryTest().emulate_category()
        ProductTest().emulate_product()
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

    def test_rating_use_case(self):
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
        sleep(2)

        # The user types "Pain" on the main form
        self.browser.find_element_by_id('id_main_form').send_keys('Pain')
        sleep(2)

        # The user clicks then "Chercher" button ans sees the proposed
        # substitutes products
        self.browser.find_element_by_id('index_search_button').click()
        sleep(2)
        self.assertTrue(
           self.browser.find_element_by_id('result_searched_product')
        )

        # On the results page, the user clicks on a product to see its details
        self.browser.find_element_by_id('subsitute_product').click()
        sleep(2)
        self.assertTrue(
           self.browser.find_element_by_id('result_ratings_form')
        )

        # On the product deatil page, the user rate the product giving a
        # three star and then click the sublit button
        self.browser.find_element_by_xpath(
            "//div[@id='rating_inputtype_select']/select[@name='ratings']"
            "/option[@value='3']"
        ).click()
        sleep(2)
        self.browser.find_element_by_id('rate_button').click()
        sleep(2)
        self.assertTrue(
            self.browser.find_element_by_id("three_star_three")
        )
