# pylint: disable=C0116
"""Test ratings form module.
"""
from django.test import TestCase

from supersub.forms.ratings_form import RatingsForm


class RatingsTest(TestCase):
    """Test Ratings form  class.
    """
    def setUp(self):
        self.ratings_form = RatingsForm()
        self.choices_list = [
            (None, ""),
            (1, "Très mauvais (une étoile)"),
            (2, "Mauvais (deux étoiles)"),
            (3, "Moyen (trois étoiles)"),
            (4, "Bon (quatre étoiles)"),
            (5, "Très bon (cinq étoiles)")
        ]

    def test_ratingsform_with_attr_rating_label(self):
        self.assertEqual(
            self.ratings_form.fields['ratings'].label, "Note le produit:"
        )

    def test_ratingsform_with_attr_ratings_class(self):
        self.assertEqual(
            self.ratings_form.fields['ratings']
            .widget.choices, self.choices_list
        )

    def test_ratingsform_with_attr_rating_id(self):
        self.assertEqual(
            self.ratings_form.fields['ratings']
            .widget.attrs['id'], 'rating_form_attr'
        )

    def test_ratingsform_with_validation_wo_input(self):
        form = RatingsForm(data={'ratings': None})
        self.assertFalse(form.is_valid())

    def test_ratingsform_with_validation_with_input(self):
        form = RatingsForm(data={'ratings': 2})
        self.assertTrue(form.is_valid())
