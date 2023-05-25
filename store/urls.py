from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home_page, name='home_page'),

    path('category/<cid>', views.category_product, name='category_product'),
    path('brands/<bid>', views.brands_product_list, name='brands_product_list'),


    path('products/', views.products, name='products'),
    path('product/<pid>', views.product_detail, name='product_detail'),

    path('vendors/', views.vendor_list, name='vendor_list'),
    path('vendors/<vid>', views.vendor_detail, name='vendor_detail'),

    # add_review
    path('review/<pid>', views.add_review, name='add_review'),
    path('search/', views.search_view, name='search'),
    
    # Filter
    path('filter-products/', views.filter_products, name='filter_products'),
    
]
