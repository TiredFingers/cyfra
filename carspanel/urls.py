from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("store", views.calc_store_load, name='store'),
]
