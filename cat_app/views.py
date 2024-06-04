from django.shortcuts import render
from .models import Product

def product_list(request):
    products = Product.objects.all()

    brand = request.GET.get('brand')
    type_ = request.GET.get('type')
    min_price = request.GET.get('min_price')
    max_price = request.GET.get('max_price')

    if brand:
        products = products.filter(brand__icontains=brand)

    if type_:
        products = products.filter(type__icontains=type_)

    if min_price:
        products = products.filter(price__gte=min_price)

    if max_price:
        products = products.filter(price__lte=max_price)

    context = {
        'products': products,
    }
    return render(request, 'catalog/product_list.html', context)
