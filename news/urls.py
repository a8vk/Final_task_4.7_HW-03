from django.urls import path
from .views import product_list

urlpatterns = [
    path('first/', product_list),
]
