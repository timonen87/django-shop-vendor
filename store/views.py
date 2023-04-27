from django.shortcuts import render, get_list_or_404
from store.models import Category, Product, ProductImages, ProductReview, CartOrder, CartOrderItems, Vendor, Adress, WishList, Brand




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


def product_detail(request, pid):
    product = Product.objects.get(pid=pid)
    # product = get_list_or_404(Product, pid=pid)

    p_image = product.p_images.all()

    context = {
         'product': product,
         'p_image': p_image,
    }

    return render(request, 'store/detail_product.html', context)


def category_product(request, cid):
    # Берем категорию из базы данных по id
    category = Category.objects.get(cid=cid)
    # Теперь забираем список продуктов из категории и доюавляем в контекст
    category_products = Product.objects.filter(product_status='published', category=category)
    context = {
        'category': category,
        'category_products': category_products,
    }
    return render(request, 'store/products.html', context)

def brands_product_list(request, bid):
    brands = Brand.objects.all()
    brand = Brand.objects.get(bid=bid)
    brands_product_list = Product.objects.filter(product_status='published', brand=brand)
    context = {
        'brands': brands,
        'brand': brand,
        'brands_product_list': brands_product_list,
    }
    return render(request, 'store/brands_list.html', context)



def vendor_list(request):
    vendors = Vendor.objects.all()
    context = {
        'vendors': vendors,
    }
    return render(request, 'store/vendor_list.html', context)

def vendor_detail(request, vid):
    vendor = Vendor.objects.get(vid=vid)
    vendor_product_list = Product.objects.filter(product_status='published', vendor=vendor)
    
    context = {
        'vendor': vendor,
        'products' : vendor_product_list,
    }
    return render(request, 'store/vendor_list.html', context)
