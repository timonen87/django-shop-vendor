from django.shortcuts import render, get_list_or_404, redirect
from django.template.loader import render_to_string
from django.views.generic.list import ListView
from django.http import JsonResponse, HttpResponse
from store.models import Category, Product, ProductImages, ProductReview, CartOrder, CartOrderItems, Vendor, Adress, WishList, Brand
from django.db.models import Count, Avg
from store.forms import ProductReviewForm
from django.db.models import Q



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


def products(request):
    products = Product.objects.filter(product_status='published')
    context = {
        'products': products,
    }
    return render(request, 'store/catalog/base_catalog.html', context)


def product_detail(request, pid):
    product = Product.objects.get(pid=pid)
    # product = get_list_or_404(Product, pid=pid)
    r_products = Product.objects.filter(category=product.category).exclude(pid=pid)

    p_image = product.p_images.all()

    review_form = ProductReviewForm()

    reviews = ProductReview.objects.filter(product=product).order_by('-date')
    average_rating = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))

    make_review = True

    if request.user.is_authenticated:
        user_review_count = ProductReview.objects.filter(user=request.user, product=product).count()

        if user_review_count > 0:
            make_review = False

    context = {
        'title': product.title,
        'product': product,
        'p_image': p_image,
        'average_rating': average_rating,
        'r_products': r_products,
        'make_review': make_review,
        'reviews': reviews,
        'review_form': review_form,
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
    return render(request, 'store/catalog/category_list.html', context)

def brands_product_list(request, bid):
    brands = Brand.objects.all()
    brand = Brand.objects.get(bid=bid)
    brands_product_list = Product.objects.filter(product_status='published', brand=brand)
    context = {
        'brands': brands,
        'brand': brand,
        'brands_product_list': brands_product_list,
    }
    return render(request, 'store/catalog/brands_list.html', context)



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
        'products': vendor_product_list,
    }
    return render(request, 'store/vendor_list.html', context)


# Добавение отзыва через ajax
def add_review(request, pid):
    product = Product.objects.get(pid=pid)
    user = request.user

    review = ProductReview.objects.create(
        user=user,
        product=product,
        review = request.POST['review'],
        rating = request.POST['rating'],
    )

    context = {
        'user': user.username,
        'review': request.POST['review'],
        'rating': request.POST['rating'],
    }

    average_reviews = ProductReview.objects.filter(product=product).aggregate(rating=Avg('rating'))


    return JsonResponse(
       {
        'bool': True,
        'context': context,
        'average_reviews': average_reviews,
       }

    )


def search_view(request):
    products = Product.objects.all()
    query = request.GET.get('q')
    if query:
        products = products.filter(
            Q(title__contains=query)|
            Q(description__contains=query)|
            Q(sku__contains=query)
        ).distinct()
    # products = Product.objects.filter(title__iregex=query).order_by('-date')
    print(query)

    context = {
        'products': products,
        'query': query
    }

    return render(request, 'store/search.html', context)


def filter_products(request):
    categories = request.GET.getlist('category[]')
    brand = request.GET.getlist('brand[]')
    type_product = request.GET.getlist('type_product[]')

    products = Product.objects.filter(product_status='published')

    if len(categories) > 0:
        products = Product.objects.filter(category__id__in = categories).distinct()
    
    if len(brand) > 0:
        products = Product.objects.filter(brand__id__in = brand).distinct()


    data = render_to_string('store/async/filter_product.html', {'products': products})

    
    return JsonResponse({'data': data})


class JsonFilterProducts(ListView):
    def get_queryset(self):
        queryset = Product.objects.filter(
            Q(category__in = self.request.GET.getlist('category'))|
            Q(brand__in = self.request.GET.getlist('brand'))
        ).distinct().values('pid', 'image', 'title', 'old_price', 'price' )
        return queryset
    
    def get(self, request, *args, **kwargs):
        queryset = list(self.get_queryset())
        return JsonResponse({'data': queryset}, safe=False)


