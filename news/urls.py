from django.urls import path
from .views import index, detail, uncos_view, articles_view
from .views import NewsListView

urlpatterns = [
    path('', NewsListView.as_view(), name='default'),
    path('<int:pk>', detail, name='detail'),
    path('uncos.html', uncos_view, name='uncos'),
    path('articles.html', articles_view, name='articles'),
]
