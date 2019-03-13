from django.shortcuts import render, get_object_or_404
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from products.models import Product


def index(request):
    products = Product.objects.order_by('-submit_time').filter(is_published=True)
    paginator = Paginator(products, 6)
    page = request.GET.get('page')
    paged_products = paginator.get_page(page)

    context = {
        'products': paged_products
    }
    return render(request, 'pages/index.html', context)




def about(request):
    return render(request, 'pages/about.html')


def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    context = {
        'product': product
    }
    return render(request, 'products/product.html', context)
