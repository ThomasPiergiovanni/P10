"""Ratings form module
"""
from django import forms


class RatingsForm(forms.Form):
    """Ratings form class. Used for rating products.
    """
    choices_list = [
        (1, "Une étoile"),
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
                'choices': choices_list,
                'id': 'rating_form_attr'
            }
        )
    )
