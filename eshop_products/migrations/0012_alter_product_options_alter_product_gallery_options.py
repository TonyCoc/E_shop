# Generated by Django 4.0 on 2022-01-22 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0011_product_gallery'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'محصولات', 'verbose_name_plural': 'محصول'},
        ),
        migrations.AlterModelOptions(
            name='product_gallery',
            options={'verbose_name': 'گالری ها', 'verbose_name_plural': 'گالری محصولات'},
        ),
    ]
