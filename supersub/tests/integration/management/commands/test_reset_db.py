# pylint: disable=C0116, E1101, W0212
"""Test reset DB module. Integration test
"""
from django.test import TestCase

from supersub.management.commands.reset_db import Command
from supersub.models.category import Category
from supersub.models.product import Product
from supersub.tests.unit.models.test_category import CategoryTest
from supersub.tests.unit.models.test_product import ProductTest


class CommandTest(TestCase):
    """Test reset DB class
    """

    @classmethod
    def setUpTestData(cls):
        """Method that setup data for the whole class
        """
        cls.db_manager = Command()
        CategoryTest.emulate_category()
        ProductTest.emulate_product()

    def test_reset_db_with_handle_command_execution(self):
        init_category = Category.objects.order_by('id')[0]
        init_product = Product.objects.order_by('id')[0]
        options = {'all': False}
        self.db_manager.handle(**options)
        post_category = Category.objects.order_by('id')[0]
        post_product = Product.objects.order_by('id')[0]
        category_message = "Category is not reset"
        product_message = "Product is not reset"
        self.assertNotEqual(
            init_category.name, post_category.name, category_message
        )
        self.assertNotEqual(
            init_product.name, post_product.name, product_message
        )
