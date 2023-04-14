from django.shortcuts import render, get_object_or_404
from .models import Product, Category



def category_list(request, category_slug=None):
    category = get_object_or_404(Category, slug=category_slug)
    products = Product.objects.filter(category=category)
    return render(request, 'store/category.html', {'category': category, 'products': products})




def all_products(request):
    products = Product.objects.all()
    related_products = Product.objects.all()[:3]
    return render(request, 'store/home.html', {'products': products, 'related_products': related_products})





def product_detail(request, slug):
    related_products = Product.objects.all()[:3]
    product = get_object_or_404(Product, slug=slug, in_stock=True)
    return render(request, 'store/detail_product.html', {'product': product, 'related_products': related_products})