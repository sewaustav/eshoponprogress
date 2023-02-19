from . import views
from django.urls import path

from .views import *

urlpatterns = [
    path('', views.home, name="home_page"),
    path('profile/', profile, name='prof')
]

