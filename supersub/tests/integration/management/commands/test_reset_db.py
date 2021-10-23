# pylint: disable=C0116, E1101, W0212
"""Test reset DB module
"""
from django.test import TestCase

from pur_beurre.custom_settings.tests_variables import (
    OFF_API_FILTERED_PRODUCTS, OFF_API_FILTERED_CATEGORIES
)
from supersub.management.commands.reset_db import Command
from supersub.models.category import Category
from supersub.models.product import Product


class CommandTest(TestCase):
    """Test reset DB class
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
    
    def test_reset_db_with_handle_command_execution(self):
        init_category = Category.objects.order_by('id')[0]
        init_product = Product.objects.order_by('id')[0]
        self.db_manager.handle()
        post_category = Category.objects.order_by('id')[0]
        post_product = Product.objects.order_by('id')[0]
        category_message = "Category is not reset"
        product_message = "Product is not reset"
        self.assertTrue(init_category)
        self.assertTrue(init_product)
        self.assertTrue(post_category)
        self.assertTrue(post_product)
        self.assertNotEqual(
            init_category.id, post_category.id, category_message
        )
        self.assertNotEqual(
            init_product.id, post_product.id, product_message
        )