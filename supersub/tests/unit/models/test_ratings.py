# pylint: disable=E1101, C0116, W0212, R0801
"""Test Ratings module.
"""
from django.db import models
from django.test import TestCase

from authentication.models import CustomUser
from authentication.tests.unit.models.test_custom_user import CustomUserTest
from supersub.models.product import Product
from supersub.models.ratings import Ratings
from supersub.tests.unit.models.test_category import CategoryTest
from supersub.tests.unit.models.test_product import ProductTest


class RatingsTest(TestCase):
    """Test Ratings class.
    """
    @classmethod
    def setUpTestData(cls):
        CategoryTest().emulate_category()
        ProductTest().emulate_product()
        CustomUserTest().emulate_custom_user()
        cls.emulate_ratings()

    @classmethod
    def emulate_ratings(cls):
        Ratings.objects.create(product_id=1, custom_user_id=1, rate=3)
        Ratings.objects.create(product_id=2, custom_user_id=1, rate=4)
        Ratings.objects.create(product_id=1, custom_user_id=2, rate=2)

    def test_ratings_with_instance(self):
        ratings = Ratings.objects.get(pk=1)
        self.assertIsInstance(ratings, Ratings)
        self.assertEqual(ratings.product_id, 1)
        self.assertEqual(ratings.rate, 3)

    def test_str_with_product_name(self):
        ratings = Ratings.objects.get(pk=1)
        self.assertEqual(
            ratings.__str__(),
            'Pain 100% mie nature PT - Harrys - 500 g'
        )

    def test_ratings_with_attr_product(self):
        ratings_field = Ratings._meta.get_field('product')
        self.assertTrue(ratings_field)
        self.assertEqual(
            type(ratings_field),
            type(models.ForeignKey(Product, models.CASCADE))
        )

    def test_ratings_with_attr_custom_user(self):
        ratings_field = Ratings._meta.get_field('custom_user')
        self.assertTrue(ratings_field)
        self.assertEqual(
            type(ratings_field),
            type(models.ForeignKey(CustomUser, models.CASCADE))
        )

    def test_ratings_with_attr_rate(self):
        ratings_field = Ratings._meta.get_field('rate')
        self.assertTrue(ratings_field)
        self.assertEqual(type(ratings_field), type(models.IntegerField()))

    def test_prodcut_ratings_with_product(self):
        product = Product.objects.get(pk=1)
        self.assertEqual(product.product_rating(), int(2.5))

    def test_prodcut_count_with_product(self):
        product = Product.objects.get(pk=1)
        self.assertEqual(product.product_count(), 2)
