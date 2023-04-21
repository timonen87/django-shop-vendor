from django.shortcuts import render
from store.models import Category, Product, ProductImages, ProductReview, CartOrder, CartOrderItems, Vendor, Adress, WishList




def home_page(request):
    products = Product.objects.filter(product_status='published').order_by('-date')
    related_products = Product.objects.filter(product_status='published', featured=True)
    context = {
        'products': products,
        'related_products': related_products,
  
    }
    return render(request, 'store/home.html', context)


def product_list(request):
    products = Product.objects.all()
    context = {
        'products': products,
    }
    return render(request, 'store/home.html', context)



def product_detail(request):

    return render(request, 'store/detail_product.html')