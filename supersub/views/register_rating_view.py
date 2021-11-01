# pylint: disable=W0212
"""Register rating view module.
"""
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.urls import reverse

from supersub.forms.ratings_form import RatingsForm
from supersub.views.custom_view import CustomView


class RegisterRatingView(CustomView):
    """Register rating view class.
    """
    def __init__(self):
        super().__init__()
        self._data['redirect'] = 'supersub:product_detail'

    def post(self, request, id_prod):
        """Register rating method on client post request. On the attempt
        of registering its rating, the user is redirected to the product
        detail page.
        """
        form = RatingsForm(request.POST)
        if form.is_valid():
            form_value = form.cleaned_data['ratings']
            self._save_rating(id_prod, request.user.id, form_value)
        return HttpResponseRedirect(
            reverse(self._data['redirect'], args=[id_prod])
        )
