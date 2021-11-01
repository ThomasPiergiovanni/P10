# pylint: disable=C0116, E1101
"""Test register rating view module.
"""
from django.test import TestCase

from authentication.tests.unit.models.test_custom_user import (
    CustomUserTest
)
from supersub.models.ratings import Ratings
from supersub.tests.unit.models.test_category import CategoryTest
from supersub.tests.unit.models.test_favorites import FavoritesTest
from supersub.tests.unit.models.test_product import ProductTest
from supersub.tests.unit.models.test_ratings import RatingsTest


class RegisterRatingViewTest(TestCase):
    """Test product register favorite view class.
    """
    @classmethod
    def setUpTestData(cls):
        CategoryTest.emulate_category()
        ProductTest.emulate_product()
        CustomUserTest.emulate_custom_user()
        RatingsTest.emulate_ratings()

    def setUp(self):
        self.client.login(email='testuser@email.com', password='_Xxxxxxx')

    def test_post_with_status_code_200(self):
        response = self.client.post(
            '/register_rating/3',
            data={'ratings': 1},
            follow=True
        )
        self.assertEqual(response.status_code, 200)

    def test_post_with_rating_saved(self):
        response = self.client.post(
            '/register_rating/4',
            data={'ratings': 5},
            follow=True
        )
        new_rating = Ratings.objects.get(
            product_id__exact=4,
            custom_user_id__exact=1,
            rate__exact=5
        )
        self.assertTrue(new_rating)

    def test_post_with_redirect(self):
        response = self.client.post(
            '/register_rating/4',
            data={'ratings': 5},
            follow=True
        )
        self.assertEqual(
            response.redirect_chain[0][0],
            '/product_detail/4'
        )
