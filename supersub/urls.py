"""Urls module
"""
from django.urls import path


from .views.favorites_view import FavoritesView
from .views.index_view import IndexView
from .views.legal_mentions_view import LegalMentionsView
from .views.product_detail_view import ProductDetailView
from .views.register_favorite_view import RegisterFavoriteView
from .views.register_rating_view import RegisterRatingView
from .views.result_view import ResultView

app_name = 'supersub'

urlpatterns = [
    path('', IndexView.as_view(), name='index'),
    path(
        'product_detail/<int:id_prod>', ProductDetailView.as_view(),
        name='product_detail'
    ),
    path('favorites/', FavoritesView.as_view(), name='favorites'),
    path('results/', ResultView.as_view(), name='results'),
    path(
        'register_favorite/<int:id_prod>', RegisterFavoriteView.as_view(),
        name='register_favorite'
    ),
    path(
        'register_rating/<int:id_prod>', RegisterRatingView.as_view(),
        name='register_rating'
    ),
    path('legal_mentions/', LegalMentionsView.as_view(), name='legal_mentions')
]
