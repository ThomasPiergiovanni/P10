# pylint: disable=C0116, E1101, W0212
"""Test resest DB module
"""
from django.test import TestCase

from authentication.models import CustomUser
from authentication.tests.unit.models.test_custom_user import (
    CustomUserTest
)
from pur_beurre.custom_settings.tests_variables import (
    OFF_API_FILTERED_PRODUCTS, OFF_API_FILTERED_CATEGORIES
)
from supersub.management.commands.reset_db import Command
from supersub.models.category import Category
from supersub.models.favorites import Favorites
from supersub.models.product import Product
from supersub.tests.unit.models.test_category import CategoryTest
from supersub.tests.unit.models.test_favorites import FavoritesTest
from supersub.tests.unit.models.test_product import ProductTest


class CommandTest(TestCase):
    """Test resest DB class
    """
    @classmethod
    def setUpTestData(cls):
        """Method that setup data for the whole class
        """
        cls.emulate_off_api_manager_categories()
        cls.emulate_off_api_manager_products()
        cls.db_manager = Command()

    @classmethod
    def emulate_off_api_manager_categories(cls):
        """Emulation of off api manager categories attribute. It consist of
        valid categories that have been filtered out from api response
        to ensureit suits db requirements.
        """
        cls.categories = OFF_API_FILTERED_CATEGORIES

    @classmethod
    def emulate_off_api_manager_products(cls):
        """Emulation of off api manager products attribute. It consist of
        valid products that have been filtered out from api response to ensure
        it suits db requirements
        """
        cls.products = OFF_API_FILTERED_PRODUCTS

    def test_drop_categories_with_categories(self):
        CategoryTest.emulate_category()
        init_categories = Category.objects.all()
        for category in init_categories:
            self.assertIsNotNone(category)
        self.db_manager._Command__drop_categories()
        post_categories = Category.objects.all()
        for category in post_categories:
            self.assertIsNone(category)

    def test_get_categories_with_categories(self):
        CategoryTest.emulate_category()
        self.db_manager._Command__get_categories()
        self.assertEqual(
            self.db_manager.categories_in_db[0].name,
            "CategorieOne")

    def test_insert_categories_with_category(self):
        self.db_manager.off_api_manager.categories = self.categories
        self.db_manager._Command__insert_categories()
        category = Category.objects.order_by('id')[0]
        self.assertEqual(category.name, "Snacks")

    def test_drop_products_with_products(self):
        ProductTest.emulate_product()
        self.db_manager._Command__drop_products()
        products = Product.objects.all()
        for product in products:
            self.assertIsNone(product)

    def test_insert_products_with_product(self):
        CategoryTest.emulate_category()
        self.db_manager.categories_in_db = Category.objects.all()
        self.db_manager.off_api_manager.products = self.products
        self.db_manager._Command__insert_products(
            self.db_manager.categories_in_db[0]
        )
        product = Product.objects.order_by('id')[1]
        self.assertEqual(product.name, "Prince Chocolat 2")

    def test_drop_favorites_with_favorites(self):
        FavoritesTest()
        self.db_manager._Command__drop_favorites()
        favorites = Favorites.objects.all()
        for favorite in favorites:
            self.assertIsNone(favorite)

    def test_drop_users_with_users(self):
        CustomUserTest()
        self.db_manager._Command__drop_users()
        custom_users = CustomUser.objects.all()
        for custom_user in custom_users:
            self.assertIsNone(custom_user)
