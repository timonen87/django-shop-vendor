from django.urls import reverse
from django.db import models
from shortuuid.django_fields import ShortUUIDField
from django.utils.html import mark_safe
from userauth.models import User


STATUS_CHOICE =(
    ('pocessing', "В процессе"),
    ('shipped', "В пути"),
    ('devilered', "Доствален"), 
)

STATUS = (
    ('draft', "В проекте"),
    ('disabled', "Отключен"),
    ('in_review', "На рассмотрении"), 
    ('published', "Опубликовано"), 
)


RATING = (
    ('1', "★☆☆☆☆"),
    ('2', "★★☆☆☆"),
    ('3', "★★★☆☆"), 
    ('4', "★★★★☆"), 
    ('5', "★★★★★"), 
)

def user_directory_path(instance, filename):
    return 'user_{0}/{1}'.format(instance.user.id, filename)
    # return f'user_{instance.user.id}/{filename}'

class Category(models.Model):
    # pip install django-shortuuidfield
    cid = ShortUUIDField(unique=True, length=10, max_length=20, prefix='cat', alphabet='abcdmfgldnsef12343ct')
    title = models.CharField(max_length=100, default='Батарейки')
    image = models.ImageField(upload_to='category', default='category.jpg')

    class Meta:
        verbose_name= 'Категория'
        verbose_name_plural= 'Категории'

    def category_image(self):
        return mark_safe('<img src="/media/%s" with="50" height="50" />' % (self.image))
        # return mark_safe(f'<img src="{self.image}" with="50" height="50" />')

    # def get_absolute_url(self):
    #     return reverse('store:category_list', args=[self.slug])

    def __str__(self):
        return self.title
    
# class Tags(models.Model):
#     pass

class Brand(models.Model):
    bid = ShortUUIDField(unique=True, length=10, max_length=20, prefix='brand_', alphabet='abcdmfgldnsef12343ct')
    title = models.CharField(max_length=100, default='')
    image = models.ImageField(upload_to='brand', default='brand.jpg')

    class Meta:
        verbose_name= 'Бренд'
        verbose_name_plural= 'Бренды'

    def category_image(self):
        return mark_safe('<img src="/media/%s" with="50" height="50" />' % (self.image))
        # return mark_safe(f'<img src="{self.image}" with="50" height="50" />')


    def __str__(self):
        return self.title


class Vendor(models.Model):
    vid = ShortUUIDField(unique=True, length=10, max_length=20, prefix='cat', alphabet='abcdmfgldnsef12343ct')
    title = models.CharField(max_length=100, default='Название')
    image = models.ImageField(upload_to='user_directory_path', default='vendor.jpg')
    description = models.TextField(null=True, blank=True, default='Описание продавца')

    adress = models.CharField(max_length=100, default='111555, ул.Ленина 24, Москва')
    contact = models.CharField(max_length=100, default='+7 999 456 4555')
    chat_resp_time = models.CharField(max_length=100, default='100')
    shipping_on_time = models.CharField(max_length=100, default='100')
    days_return = models.CharField(max_length=100, default='100')
    warranty_period = models.CharField(max_length=100, default='100')

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    # date = models.DateTimeField(auto_now_add=True, name=True, blank=True)

    
    class Meta:
        verbose_name= 'Продавец'
        verbose_name_plural= 'Продавцы'

    def vendor_image(self):
        return mark_safe('<img src="/media/%s" with="50" height="50" />' % (self.image))
        # return mark_safe(f'<img src="{self.image}" with="50" height="50" />')

    def __str__(self):
        return self.title
    

class Product(models.Model):
    pid = ShortUUIDField(unique=True, length=10, max_length=20, alphabet='abcdmfgldnsef12343ct')

    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='category')
    vendor = models.ForeignKey(Vendor, on_delete=models.SET_NULL, null=True)
    brand = models.ForeignKey(Brand, on_delete=models.SET_NULL, null=True)

    title = models.CharField(max_length=100, default='Название товара до 100 симвоволов')
    image = models.ImageField(upload_to='user_directory_path', default='product.jpg')
    description = models.TextField(null=True, blank=True, default='Описание товара')

    price = models.DecimalField(max_digits=9999999999999, decimal_places=2, default=100.00)
    old_price = models.DecimalField(max_digits=9999999999999, decimal_places=2, default=150.00)

    specifications= models.TextField(blank=True, null=True)
    type = models.CharField(max_length=100, default='Джинсы')
    stock_count = models.CharField(max_length=100, default='8')
    life = models.CharField(max_length=100, default='100 дней')
    maide_data = models.DateTimeField(auto_now_add=True, null=True, blank=True)
    # tags = models.ForeignKey(Tags, on_delete=models.SET_NULL, null=True)

    product_status = models.CharField(choices=STATUS, max_length=10, default='in_review')

    status = models.BooleanField(default=True)
    in_stock = models.BooleanField(default=True)
    featured = models.BooleanField(default=False)
    digital = models.BooleanField(default=False)

    sku = ShortUUIDField(unique=True, length=4, max_length=10, prefix='sku', alphabet='1234567890')

    date = models.DateTimeField(auto_now_add=True)
    upload = models.DateTimeField(null=True, blank=True)

    class Meta:
        verbose_name= 'Продукт'
        verbose_name_plural= 'Продукты'

    def product_image(self):
        return mark_safe('<img src="/media/%s" with="50" height="50" />' % (self.image))
        # return mark_safe(f'<img src="{self.image}" with="50" height="50" />')

    def __str__(self):
        return self.title

    def get_procentage(self):
        new_price = (self.price / self.old_price) * 100
        return new_price
    
    # def get_absolute_url(self):
    #     return reverse('store:category_list', args=[self.slug])
    

class ProductImages(models.Model):
    images = models.ImageField(upload_to='product-images', default='product.jpg')
    product = models.ForeignKey(Product, related_name='p_images', on_delete=models.SET_NULL, null=True)
    date = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name= 'Изображение'
        verbose_name_plural= 'Изображения'


########################### Cart, Order, OrderItems and Adresss #####################################################
########################### Cart, Order, OrderItems and Adresss #####################################################
########################### Cart, Order, OrderItems and Adresss #####################################################
########################### Cart, Order, OrderItems and Adresss #####################################################

class CartOrder(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=9999999999999, decimal_places=2, default=10.00)
    paid_status = models.BooleanField(default=False)
    order_date = models.DateTimeField(auto_now_add=True)
    product_status = models.CharField(choices=STATUS_CHOICE, max_length=30, default='processing')

    class Meta:
        verbose_name_plural= 'Заказы'
    

class CartOrderItems(models.Model):
    order = models.ForeignKey(CartOrder, on_delete=models.CASCADE)
    invoice_no = models.CharField(max_length=200)
    product_status = models.CharField(max_length=200)
    item = models.CharField(max_length=200)
    image = models.CharField(max_length=200)
    qty = models.IntegerField(default=0)
    price = models.DecimalField(max_digits=9999999999999, decimal_places=2, default=10.00)
    total = models.DecimalField(max_digits=9999999999999, decimal_places=2, default=10.00)

    class Meta:
        verbose_name_plural= 'Товары в корзине'

    
    def order_image(self):
        return mark_safe('<img src="/media/%s" with="50" height="50" />' % (self.image))
        # return mark_safe(f'<img src="{self.image}" with="50" height="50" />')


########################### Product Review, wishlists. Adress #####################################################
########################### Product Review, wishlists. Adress #####################################################
########################### Product Review, wishlists. Adress #####################################################


class ProductReview(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=None)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural= 'Отзывы о товаре'

    def __str__(self):
        return self.product.title
    
    def get_rating(self):
        return self.rating

class WishList(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    product = models.ForeignKey(Product, on_delete=models.SET_NULL, null=True)
    review = models.TextField()
    rating = models.IntegerField(choices=RATING, default=None)
    date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural= 'Избранное'

    def __str__(self):
        return self.product.title



class Adress(models.Model):
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    adress = models.CharField(max_length=100, null=True)
    status = models.BooleanField(default=False)

    class Meta:
        verbose_name_plural= 'Адрес'

    