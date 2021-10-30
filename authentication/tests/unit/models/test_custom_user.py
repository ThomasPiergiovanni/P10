# pylint: disable=C0116, W0212, E1101
"""Test custom user model module(unitary test).
"""
from django.db import models
from django.test import TestCase

from authentication.models import CustomUser


class CustomUserTest(TestCase):
    """Test custom user model module class.
    """
    @classmethod
    def setUpTestData(cls):
        cls.emulate_custom_user()

    @classmethod
    def emulate_custom_user(cls):
        CustomUser.objects.create_user(
            id=1,
            email='testuser@email.com',
            password='_Xxxxxxx',
            first_name='tester'
        )
        CustomUser.objects.create_user(
            id=2,
            email='testuser2@email.com',
            password='_Yxxxxxx',
            first_name='tester2'
        )

    def test_custom_user_with_attr_username(self):
        user_field = CustomUser._meta.get_field('email')
        self.assertTrue(user_field)
        self.assertEqual(type(user_field), type(models.EmailField()))
        self.assertEqual(user_field.max_length, 250)
        self.assertEqual(user_field.unique, True)

    def test_custom_user_with_attr_first_name(self):
        user_field = CustomUser._meta.get_field('first_name')
        self.assertTrue(user_field)
        self.assertEqual(type(user_field), type(models.TextField()))
        self.assertEqual(user_field.max_length, 100)
        self.assertEqual(user_field.null, False)

    def test_custom_user_with_instance(self):
        user = CustomUser.objects.get(pk=1)
        self.assertIsInstance(user, CustomUser)
        self.assertEqual(user.id, 1)
        self.assertEqual(user.email, 'testuser@email.com')

    def test__str__with_email(self):
        user = CustomUser.objects.get(pk=1)
        self.assertEqual(user.__str__(), 'testuser@email.com')
