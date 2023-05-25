from store.models import Category, Product, Brand, Adress

def categories(request):
    return {
        'categories': Category.objects.all()
        
    }


def brands(request):
    return {
        'brands': Brand.objects.all()
    }

def cat_related_products (request):
    return {
        'cat_related_products': Product.objects.filter(product_status='published', featured=True)
    }

def adress(request):
    try:
        adress = Adress.objects.get(user=request.user)
    except:
        adress =None
    return {
        'adress': adress,
    }

