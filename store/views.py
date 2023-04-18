from django.shortcuts import render



def category_list(request):
    return render(request, 'store/category.html')


def all_products(request):
    return render(request, 'store/home.html')



def product_detail(request):
    return render(request, 'store/detail_product.html')