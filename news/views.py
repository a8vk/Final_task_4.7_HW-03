from django.shortcuts import render
from .filters import F
from .models import Product


def product_list(request):
    f = F(request.GET, queryset=Product.objects.all())
    return render(request, 'template.html', {'filter': f})
