import django_filters
from django.forms.widgets import DateInput
from .models import New


CATEGORIES_CHOICES = [
    ('uncos', 'Новости'),
    ('articles', 'Статьи'),
]


class NewsFilter(django_filters.FilterSet):
    title = django_filters.CharFilter(lookup_expr='icontains', label='Поиск по названию')
    category = django_filters.ChoiceFilter(choices=CATEGORIES_CHOICES, label='Поиск по категории')
    pub_date = django_filters.DateFilter(widget=DateInput(attrs={'type': 'date'}), label='Поиск по дате')

    class Meta:
        model = New
        fields = ['title', 'category', 'pub_date']
