# Generated by Django 4.2 on 2023-05-25 13:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0015_alter_product_image_alter_product_image2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(default='product.jpg', upload_to='user_directory_path'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image2',
            field=models.ImageField(default='product2.jpg', upload_to='user_directory_path'),
        ),
        migrations.AlterField(
            model_name='productimages',
            name='images',
            field=models.ImageField(default='product.jpg', upload_to='user_directory_path'),
        ),
    ]
