# Generated by Django 4.0 on 2022-01-18 12:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products_category', '0001_initial'),
        ('eshop_products', '0008_product_categories'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='categories',
            field=models.ManyToManyField(blank=True, null=True, to='eshop_products_category.category'),
        ),
    ]
