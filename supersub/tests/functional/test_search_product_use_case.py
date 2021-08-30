# pylint: disable=C0116
"""Test search product use case test module. Functional test
"""
from time import sleep

from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver

from pur_beurre.custom_settings import *
from supersub.tests.unit.models.test_category import CategoryTest
from supersub.tests.unit.models.test_product import ProductTest


class SearchProductUseCaseTest(StaticLiveServerTestCase):
    """Tes search product use case test class
    """
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.browser = webdriver.Edge(r'/usr/local/bin/msedgedriver')
        cls.browser.implicitly_wait(10)
        CategoryTest().emulate_category()
        ProductTest().emulate_product()

    @classmethod
    def tearDownClass(cls):
        cls.browser.quit()
        super().tearDownClass()

    def setUp(self):
        # The user logs to the app page
        self.browser.get('%s%s' % (self.live_server_url, ''))

    def test_user_lands_on_home_page(self):
        # The user notices the page name and the header title
        self.assertIn("P8 - Pur-beurre", self.browser.title)
        self.assertIn(
            'DU GRAS, OUI MAIS DE QUALITÉ',
            self.browser.find_element_by_tag_name('h1').text
        )

        # The user notices a navbar composed of an image
        navbar_image = self.browser.find_element_by_tag_name('img')
        self.assertTrue(navbar_image)

        # ...  a title
        navbar_text = self.browser.find_element_by_id(
            'navbar_pur_beurre_texte'
        ).text
        self.assertIn("Pur Beurre", navbar_text)

        # ... a form
        navbar_inputbox = self.browser.find_element_by_id(
            'navbar_search_form'
        )
        self.assertEqual(navbar_inputbox.get_attribute('method'), 'post')

        # ... a user, a carrot and a logout icons
        self.assertTrue(self.browser.find_element_by_id('user_icon'))
        self.assertTrue(self.browser.find_element_by_id('carrot_icon'))
        self.assertTrue(self.browser.find_element_by_id('logout_icon'))

    def test_search_product_use_case(self):
        # The user types "Pain" on the main form
        sleep(2)
        self.browser.find_element_by_id('id_main_form').send_keys('Pain')
        sleep(2)

        # The user clicks then "Chercher" button ans sees the proposed
        # substitutes products
        self.browser.find_element_by_id('index_search_button').click()
        sleep(2)
        self.assertTrue(
           self.browser.find_element_by_id('result_searched_product')
        )
