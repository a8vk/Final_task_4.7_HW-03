from django.shortcuts import render
from django.views.generic.list import ListView
from .models import New
from .filters import NewFilter


# Create your views here.
def index(request):
    news = New.objects.order_by('-data_pub')  # от более свежей к самой старой
    return render(request, 'default.html', {'news': news})


def detail(request, pk):
    new = New.objects.get(pk=pk)
    return render(request, 'detail.html', context={'new': new})


def uncos_view(request):
    return render(request, 'uncos.html', {})


def articles_view(request):
    return render(request, 'articles.html', {})


class NewsListView(ListView):
    model = New
    paginate_by = 10
    ordering = ['-data_pub']
    template_name = 'default.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        paginator = context['paginator']
        current_page = context['page_obj']
        start_index = max(current_page.number - 2, 1)
        end_index = min(current_page.number + 2, paginator.num_pages)
        page_range = range(start_index, end_index + 1)
        context['page_range'] = page_range
        return context


def news_search(request):
    news_list = New.objects.all()
    news_filter = NewFilter(request.GET, queryset=news_list)
    return render(request, 'news_search.html', {'filter': news_filter, 'news_list': news_filter.qs})