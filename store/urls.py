from django.urls import path

from . import views

app_name = 'store'

urlpatterns = [
    path('', views.home_page, name='home_page'),
    path('products/', views.product_list, name='product_list'),
    # path('product/', views.product_detail, name='product_detail'),
    # path('search/<slug:category_slug>/', views.category_list, name='category_list'),
]
