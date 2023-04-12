from .models import Product, Category
from django_filters import FilterSet, CharFilter


class F(FilterSet):
    name = CharFilter()

    class Meta:
        model = Product
        fields = ['name']