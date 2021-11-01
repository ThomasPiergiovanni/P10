# pylint: disable=E1101
"""Ratings module model
"""
from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

from authentication.models import CustomUser
from supersub.models.product import Product


class Ratings(models.Model):
    """Ratings class model. Composed of Custom User and Product classes
    foreign keys.
    """
    custom_user = models.ForeignKey(CustomUser, models.CASCADE)
    product = models.ForeignKey(Product, models.CASCADE)
    rate = models.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )

    def __str__(self):
        return self.product.name
