from django.urls import path
from .views import (
    NewsListView,
    NewDetailView,
    UncosNewsListView,
    ArticlesNewsListView,
    NewsSearchView,
    news_search,
)

urlpatterns = [
    path('', NewsListView.as_view(), name='index'),
    path('<int:pk>/', NewDetailView.as_view(), name='detail'),
    path('uncos/', UncosNewsListView.as_view(), name='uncos'),
    path('articles/', ArticlesNewsListView.as_view(), name='articles'),
    path('news/', NewsSearchView.as_view(), name='news'),
    path('search/', news_search, name='news_search'),
]
