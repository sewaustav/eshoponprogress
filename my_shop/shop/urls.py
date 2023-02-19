from django.urls import path
from .views import *


urlpatterns = [
    path('form', create_post, name='main-site'),
    path('', show_all, name='main'),
    path('product/<int:pk>', ProductDetailView.as_view(), name='id_prod'),
    path('signup', signup, name='signup'),
    path('search', search, name='search_results'),
    path('basket', basket, name='basket'),
    path('mybasket', view_basket, name='mybasket'),
    path('signup/success', success, name='success'),
]