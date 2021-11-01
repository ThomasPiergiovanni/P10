"""Ratings form module
"""
from django import forms


class RatingsForm(forms.Form):
    """Ratings form class. Used for rating products.
    """
    choices_list = [
        (None, ""),
        (1, "Très mauvais (une étoile)"),
        (2, "Mauvais (deux étoiles)"),
        (3, "Moyen (trois étoiles)"),
        (4, "Bon (quatre étoiles)"),
        (5, "Très bon (cinq étoiles)")
    ]
    ratings = forms.IntegerField(
        label="Note le produit:",
        widget=forms.Select(
            attrs={
                'class': 'form-control',
                'id': 'rating_form_attr'
            },
            choices=choices_list,
        )
    )
