"""Products module model
"""
from django.db import models
from django.db.models import Avg

from authentication.models import CustomUser
from supersub.models.category import Category


class Product(models.Model):
    """Products class model. Category attribute is a foreign from Catgeory
    class.
    """
    id_origin = models.CharField(max_length=200)
    name = models.CharField(max_length=200, unique=True)
    nutriscore_grade = models.CharField(max_length=8)
    fat = models.DecimalField(max_digits=8, decimal_places=3)
    saturated_fat = models.DecimalField(max_digits=8, decimal_places=3)
    sugar = models.DecimalField(max_digits=8, decimal_places=3)
    salt = models.DecimalField(max_digits=8, decimal_places=3)
    image = models.URLField(max_length=200)
    url = models.URLField(max_length=200)
    categories = models.TextField()
    category = models.ForeignKey(Category, models.CASCADE)
    relation_custom_user = models.ManyToManyField(
        CustomUser, through='Favorites'
    )

    def product_rating(self):
        avg_rating = self.ratings_set.all().aggregate(Avg('rate'))
        avg_rating = avg_rating['rate__avg']
        if avg_rating:
            avg_rating =int(avg_rating)
        return avg_rating
