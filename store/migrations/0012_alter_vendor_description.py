# Generated by Django 4.2 on 2023-05-02 13:48

import ckeditor_uploader.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0011_product_image2_alter_product_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vendor',
            name='description',
            field=ckeditor_uploader.fields.RichTextUploadingField(blank=True, default='Описание продавца', null=True, verbose_name='text'),
        ),
    ]
