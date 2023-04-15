from django.urls import path
from .views import index, detail, uncos_view, articles_view, NewsListView, news_search
from .views import NewsListView

urlpatterns = [
    path('', index, name='index'),
    path('<int:pk>/', detail, name='detail'),
    path('uncos/', uncos_view, name='uncos'),
    path('articles/', articles_view, name='articles'),
    path('news/', NewsListView.as_view(), name='news'),
    path('search/', news_search, name='news_search'),  # добавленный URL-адрес для вида news_search
]
