from django.shortcuts import render
from store.models import Product, Category


def category_list(request):
    context = {
        'categories': Category.objects.all()
    }
    return render(request, 'store/category.html', context)


def all_products(request):
    products = Product.objects.all()
    context = {
        'products': products,
        'related_products': products[:3],
        'categories': Category.objects.all()
    }
    return render(request, 'store/home.html', context)



def product_detail(request):

    return render(request, 'store/detail_product.html')