"""Ratings form module
"""
from django import forms


class RatingsForm(forms.Form):
    """Ratings form class. Used for rating products.
    """
    choices_list = [
        (None, ""),
        (1, "Une étoiles"),
        (2, "Deux étoiles"),
        (3, "Trois étoiles"),
        (4, "Quatre étoiles"),
        (5, "Cinq étoiles")
    ]
    ratings = forms.IntegerField(
        label="Note le produit:",
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'rating_form_attr'
            },
            choices = choices_list,
        )
    )