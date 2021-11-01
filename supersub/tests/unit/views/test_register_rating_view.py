# pylint: disable=C0116, W0212
"""Test register favorite module.
"""
from django.test import TestCase

from supersub.views.register_rating_view import RegisterRatingView


class TestRegisterRatingView(TestCase):
    """Test register rating class.
    """
    @classmethod
    def setUpTestData(cls):
        cls.register_rating = RegisterRatingView()

    def test_init__with_register_rating(self):
        self.assertTrue(self.register_rating)

    def test_init_with_attr_data_redirect(self):
        self.assertEqual(
            self.register_rating._data['redirect'],
            'supersub:product_detail'
        )
