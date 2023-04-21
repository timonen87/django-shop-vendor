from django.contrib import admin
from store.models import Category, Product, ProductImages, ProductReview, CartOrder, CartOrderItems, Vendor, Adress, WishList


class ProductImagesAdmin(admin.TabularInline):
    model = ProductImages


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImagesAdmin]
    list_display = ['product_image', 'title',  'price', 'user', 'featured', 'product_status' ]


class CategoryAdmin(admin.ModelAdmin):
    list_display = [ 'title', 'category_image' ]

class VendoryAdmin(admin.ModelAdmin):
    list_display = [ 'title', 'vendor_image' ]

class CartOrderAdmin(admin.ModelAdmin):
    list_display = [ 'user', 'price', 'paid_status', 'order_date', 'product_status' ]

class CartOrderItemsAdmin(admin.ModelAdmin):
    list_display = [ 'order', 'invoice_no', 'item', 'image', 'qty', 'price', 'total' ]

class ProductReviewAdmin(admin.ModelAdmin):
    list_display = [ 'user', 'product', 'review', 'rating' ]

class WishListAdmin(admin.ModelAdmin):
    list_display = [ 'user', 'product', 'date' ]
    
class AdresstAdmin(admin.ModelAdmin):
    list_display = [ 'user', 'adress', 'status' ]

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
admin.site.register(Vendor, VendoryAdmin)
admin.site.register(CartOrder, CartOrderAdmin)
admin.site.register(CartOrderItems, CartOrderItemsAdmin)
admin.site.register(ProductReview, ProductReviewAdmin)
admin.site.register(WishList, WishListAdmin)
admin.site.register(Adress, AdresstAdmin)







