# pylint: disable=W0212
"""Product detail view module.
"""
from django.shortcuts import render

from supersub.views.custom_view import CustomView
from supersub.forms.ratings_form import RatingsForm


class ProductDetailView(CustomView):
    """Product detail view class.
    """
    def __init__(self):
        super().__init__()
        self._data['render'] = 'supersub/product_detail.html'

    def get(self, request, id_prod):
        """Product detail page view method on client get request.
        """
        self._data['ctxt']['prod'] = self._get_product(id_prod)
        self._data['ctxt']['ratings_form'] = RatingsForm()
        self._data['ctxt']['user'] = request.user
        self._data['ctxt']['user_product_rating'] = (
            self._get_user_product_rating(id_prod, request.user)
        )
        return render(request, self._data['render'], self._data['ctxt'])
