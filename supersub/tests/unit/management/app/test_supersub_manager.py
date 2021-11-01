# pylint: disable=C0116, E1101, W0212, R0904
"""Test supersub manager module.
"""
from django.core.paginator import Paginator
from django.test import TestCase, RequestFactory

from authentication.tests.unit.models.test_custom_user import (
    CustomUserTest
)
from supersub.forms.main_search_form import MainSearchForm
from supersub.forms.navbar_search_form import NavbarSearchForm
from supersub.management.app.supersub_manager import SupersubManager
from supersub.models.favorites import Favorites
from supersub.models.product import Product
from supersub.models.ratings import Ratings
from supersub.tests.unit.models.test_category import CategoryTest
from supersub.tests.unit.models.test_favorites import FavoritesTest
from supersub.tests.unit.models.test_product import ProductTest
from supersub.tests.unit.models.test_ratings import RatingsTest


class SupersubManagerTest(TestCase):
    """Test supersub manager class.
    """
    @classmethod
    def setUpTestData(cls):
        cls.emulate_data()
        CategoryTest.emulate_category()
        ProductTest.emulate_product()
        CustomUserTest.emulate_custom_user()
        RatingsTest.emulate_ratings()
        cls.prod1 = Product.objects.get(pk=1)
        cls.prod2 = Product.objects.get(pk=2)
        cls.prod3 = Product.objects.get(pk=3)
        cls.prod4 = Product.objects.get(pk=4)
        cls.prods_list = cls.emulate_prods_list(cls.prod1, cls.prod2)
        cls.prods_ids = cls.emulate_prods_ids_list(cls.prod1, cls.prod2)
        cls.request_GET = RequestFactory().get('', data={'page': 1})
        cls.request_POST = RequestFactory().post(
            '', data={'page': 1, 'product': cls.prod1.name}
        )
        cls.paginator = Paginator(cls.prods_list, 6)
        FavoritesTest.emulate_favorites()

    @classmethod
    def emulate_data(cls):
        cls._data = {'ctxt': {}, 'render': "", 'redirect': ""}

    @classmethod
    def emulate_prods_list(cls, prod_one, prod_two):
        prods = []
        prods.append(prod_one)
        prods.append(prod_two)
        return prods

    @classmethod
    def emulate_prods_ids_list(cls, prod_one, prod_two):
        prods_ids = []
        prods_ids.append(prod_one.id)
        prods_ids.append(prod_two.id)
        return prods_ids

    def setUp(self):
        self.manager = SupersubManager()

    def test__get_data(self):
        data = self.manager._get_data()
        self.assertEqual(data, self._data)

    def test__get_page_from_session_vars_with_prod_name(self):
        page = self.manager._get_page_from_session_vars(
            self.request_GET, self.prods_ids
        )
        self.assertEqual(
            page[0].name,
            'Pain 100% mie nature PT - Harrys - 500 g'
        )

    def test__get_results_prods_with_prods_list(self):
        # manager = SupersubManager()
        products = (
            self.manager._SupersubManager__get_results_prods(self.prods_ids)
        )
        self.assertEqual(products, self.prods_list)

    def test__get_product_with_product(self):
        product = self.manager._get_product(self.prod1.id)
        self.assertEqual(product, self.prod1)

    def test__get_page_with_prod_name(self):
        page = self.manager._get_page(self.request_GET, self.prods_list)
        self.assertEqual(
            page[0].name,
            'Pain 100% mie nature PT - Harrys - 500 g'
        )

    def test__get_paginator_with_num_pages(self):
        paginator = (
            self.manager._SupersubManager__get_paginator(self.prods_list)
        )
        self.assertEqual(paginator.num_pages, self.paginator.num_pages)

    def test__get_paginator_with_prod_name(self):
        paginator = (
            self.manager._SupersubManager__get_paginator(self.prods_list)
        )

        def get_paginator_product_name(paginator):
            for page in paginator:
                if page.number == 1:
                    product = page.object_list[0]
                return product.name

        self.assertEqual(
            get_paginator_product_name(paginator),
            get_paginator_product_name(self.paginator)
        )

    def test__request_page_number_with_page_number(self):
        page_number = (
            self.manager.
            _SupersubManager__get_request_page_number(self.request_GET)
        )
        self.assertEqual(page_number, '1')

    def test__get_form_with_form(self):
        form = self.manager._get_form(self.request_POST)
        self.assertTrue(
            type(form),
            type(MainSearchForm()) or type(NavbarSearchForm())
        )

    def test__get_page_from_form_with_prod_name(self):
        page = self.manager._get_page_from_form(
            self.request_POST, self.prod1
        )
        self.assertEqual(
            page[0].name,
            'Wasa tartine croustillante fibres - 230 g'
        )
        self.assertEqual(
            page[1].name,
            'Biscuit pomme noisette'
        )

    def test__get_session_prods_with_prod_id(self):
        prods = self.manager._SupersubManager__get_session_prods(self.prod1)
        self.assertEqual(prods[0].id, 2)

    def test__get_prods_no_a_with_prod_id(self):
        prods = (
            self.manager._SupersubManager__get_prods_no_a(self.prod3)
        )
        self.assertEqual(prods[2].id, 1)

    def test__get_prods_a_with_prod_id(self):
        prods = (
            self.manager._SupersubManager__get_prods_a(self.prod2)
        )
        self.assertEqual(prods[0].id, 4)

    def test__get_session_prods_ids_with_prods_list(self):
        prods_ids = (
            self.manager
            ._SupersubManager__get_session_prods_ids(self.prods_list)
        )
        self.assertEqual(prods_ids, self.prods_ids)

    def test__add_vars_to_session_with_prod_id_and_prods_ids(self):
        setattr(
            self.request_POST,
            'session', {'prod_id': '', 'prods_ids': ''}
        )
        self.manager._add_vars_to_session(self.request_POST, self.prod1)
        self.assertEqual(self.request_POST.session['prod_id'], 1)
        self.assertEqual(self.request_POST.session['prods_ids'][0], 2)

    def test__delete_session_vars_with_none(self):
        setattr(
            self.request_GET,
            'session', {'prod_id': 1, 'prods_ids': [2, 3]}
        )
        self.manager._delete_session_vars(self.request_GET)
        self.assertEqual(
            self.request_GET.session.get('prod_id', None),
            None
        )
        self.assertEqual(
            self.request_GET.session.get('prods_ids', None),
            None
        )

    def test__get_session_vars_with_prod_id_and_prods_ids(self):
        setattr(
            self.request_GET,
            'session',
            {
                'prod_id': 1,
                'prods_ids': [2, 3]
            }
        )
        prod_id, prods_ids = (
            self.manager._get_session_vars(self.request_GET)
        )
        self.assertEqual(prod_id, 1)
        self.assertEqual(prods_ids, [2, 3])

    def test__filter_favorites_with(self):
        favorites = self.manager._filter_favorites(1)
        self.assertEqual(favorites[0].product_id, 1)
        self.assertEqual(favorites[1].product_id, 2)

    def test__get_favorite_with_class_type_is_true(self):
        favorite = self.manager._get_favorite(1, 1)
        self.assertTrue(favorite, type(Favorites()))

    def test__get_favorite_with_class_type_is_none(self):
        favorite = self.manager._get_favorite(1, 2)
        self.assertFalse(favorite, type(Favorites()))

    def test__save_favorite_with_class_type_is_true(self):
        self.manager._save_favorite(3, 1)
        favorite = Favorites.objects.get(product_id__exact=3)
        self.assertTrue(favorite, type(Favorites()))

    def test_get_user_product_rating_with_emulated_ratings(self):
        user_rating = self.manager._get_user_product_rating(1,1)
        rating = Ratings.objects.filter(
            product_id__exact=1,
            custom_user_id__exact=1
        )
        self.assertEqual(
            rating[0].product_id,
            user_rating.product_id
        )
        self.assertEqual(
            rating[0].custom_user_id,
            user_rating.custom_user_id
        )
    def test_get_user_product_rating_with_none_ratings(self):
        user_rating = self.manager._get_user_product_rating(2,2)
        self.assertIsNone(user_rating)
    
    def test_save_rating_with_exiting_rating(self):
        self.manager._save_rating(2,2,5)
        rating = Ratings.objects.get(
            product_id__exact=2,
            custom_user_id__exact=2
        )
        self.assertEqual(rating.rate, 5)
