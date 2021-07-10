# pylint: disable=W0212, E1101
"""Result view module.
"""
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from supersub.models.product import Product
from supersub.views.custom_view import CustomView


class ResultView(CustomView):
    """Result view class.
    """
    def __init__(self):
        super().__init__()
        self.data['render'] = 'supersub/results.html'
        self.data['redirect'] = 'supersub:index'

    def get(self, request):
        """Result page view method on client get request. Renders the selected
        product(after its capture on a previous post request)
        and its potential substitutes
        """
        prod_id, prods_ids = self.manager._get_session_vars(request)
        self.data['ctxt']['searched_prod'] = self.manager._get_product(prod_id)
        self.data['ctxt']["page_obj"] = (
            self.manager._get_page_from_session_vars(request, prods_ids))
        return render(request, self.data['render'], self.data['ctxt'])

    def post(self, request):
        """Result page view method on client post request. Renders the
        selected product and its potential substitutes. In case that the
        product is not recognized by the system, a warning message is
        displayed and the user is redirected to the index page. If no product
        is typed into the form and submitted an error messages is displayed
        and the user is redirected to the index page.
        """
        form = self.manager._get_form(request)
        if form.is_valid():
            match_prods = (
                Product.objects.filter(
                    name__contains=form.cleaned_data['product']
                )[:1]
            )
            if match_prods:
                self.data['ctxt']['searched_prod'] = match_prods[0]
                self.data['ctxt']["page_obj"] = (
                    self.manager._get_page_from_form(request, match_prods[0])
                )
                self.manager._add_vars_to_session(request, match_prods[0])
                self.data['ctxt']['user'] = request.user
                return render(
                    request, self.data['render'], self.data['ctxt']
                )
            messages.add_message(
                request, messages.WARNING,
                "Ce produit n'a pas été reconnu ou n'existe pas."
            )
        else:
            messages.add_message(
                request, messages.ERROR, "Saisissez un produit"
            )
        return HttpResponseRedirect(reverse(self.data['redirect']))
