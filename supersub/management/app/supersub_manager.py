# pylint: disable=E1101, R0201, R0903, W0702, W0703
"""Supersub manager app module.
"""
from django.core.paginator import Paginator

from supersub.forms.main_search_form import MainSearchForm
from supersub.forms.navbar_search_form import NavbarSearchForm
from supersub.models.favorites import Favorites
from supersub.models.product import Product


class SupersubManager():
    """Supersub manager app class.
    """
    def _get_data(self):
        """Method that define and get the data dictionnary variable.
        """
        data = {'ctxt': {}, 'render': "", 'redirect': ""}
        return data

    def _get_page_from_session_vars(self, request, prods_ids):
        """Method that get page objects (Products) based on previously
        strored sessions variable.
        """
        prods_candidates = self.__get_results_prods(prods_ids)
        page_obj = self._get_page(request, prods_candidates)
        return page_obj

    def __get_results_prods(self, prods_ids):
        """Method that gets Products list from DB based on session variable.
        """
        prods_candidates = []
        for prod_id in prods_ids:
            prods_candidates.append(self._get_product(prod_id))
        return prods_candidates

    def _get_product(self, id_prod):
        """Method that gets and return Product from DB.
        """
        return Product.objects.get(pk=id_prod)

    def _get_page(self, request, objects_list):
        """Method that get one page.
        """
        paginator = self.__get_paginator(objects_list)
        page_number = self.__get_request_page_number(request)
        return paginator.get_page(page_number)

    def __get_paginator(self, objects_list):
        """Method that return a Paginator object.
        """
        return Paginator(objects_list, 6)

    def __get_request_page_number(self, request):
        """Method that return a request from a specific page.
        """
        return request.GET.get('page')

    def _get_form(self, request):
        """Method that returns a form.
        """
        form = NavbarSearchForm(request.POST)
        form = MainSearchForm(request.POST)
        return form

    def _get_page_from_form(self, request, product):
        """Method that get page objects (Products) based on form input.
        """
        prods_candidates = self.__get_session_prods(product)
        page_obj = self._get_page(request, prods_candidates)
        return page_obj

    def __get_session_prods(self, product):
        """ Method that gets more or equaly healthy Product (i.e. subs)
        based on form input.
        """
        if product.nutriscore_grade in 'a':
            return self.__get_prods_a(product)
        else:
            return self.__get_prods_no_a(product)

    def __get_prods_a(self, product):
        """Method that gets products when the selected product is from
        nutriscore a.
        """
        return (
            Product.objects.filter(category_id=product.category_id)
            .filter(nutriscore_grade__lte=product.nutriscore_grade)
            .exclude(id__exact=product.id)
            .order_by('id').order_by('nutriscore_grade')[:60]
        )

    def __get_prods_no_a(self, product):
        """Method that gets products when the selected product is NOT from
        nutriscore a.
        """
        return (
            Product.objects.filter(category_id=product.category_id)
            .filter(nutriscore_grade__lte=product.nutriscore_grade)
            .exclude(nutriscore_grade__exact=product.nutriscore_grade)
            .order_by('id').order_by('nutriscore_grade')[:60]
        )

    def _add_vars_to_session(self, request, match_prod):
        """Method that adds product and subs into session vars.
        """
        prods = self.__get_session_prods(match_prod)
        prods_ids = self.__get_session_prods_ids(prods)
        request.session['prod_id'] = match_prod.id
        request.session['prods_ids'] = prods_ids

    def __get_session_prods_ids(self, prods_candidates):
        """Method that gets subs and store their ids into
        a list.
        """
        prods_ids = []
        for candidate in prods_candidates:
            prods_ids.append(candidate.id)
        return prods_ids

    def _delete_session_vars(self, request):
        """Method that delete session vars.
        """
        prod_id, prods_ids = self._get_session_vars(request)
        if prod_id and prods_ids:
            del request.session['prod_id']
            del request.session['prods_ids']

    def _get_session_vars(self, request):
        """Method that gets sessions variables (product and subs ids).
        """
        prod_id = request.session.get('prod_id', None)
        prods_ids = request.session.get('prods_ids', None)
        return prod_id, prods_ids

    def _filter_favorites(self, id_user):
        """Method that filter and return Favorites objects from DB. Used
        for  retunrning the authenticated user favorites.
        """
        return (
            Favorites.objects
            .filter(custom_user_id__exact=id_user)
            .select_related('product').order_by('id')
        )

    def _get_favorite(self, id_prod, id_user):
        """Method that get and return Favorites object from DB. Used
        for  checking if that favorite is not already savec by the querrying
        user.
        """
        try:
            return Favorites.objects.get(
                product_id__exact=id_prod,
                custom_user_id__exact=id_user
            )
        except Exception:
            return None

    def _save_favorite(self, id_prod, id_user):
        """Method that saves Favorites object from DB.
        """
        Favorites(
            product_id=id_prod,
            custom_user_id=id_user
        ).save()
