# Generated by Django 4.0 on 2021-12-24 09:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eshop_products', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='active',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(default='none', max_length=200),
        ),
        migrations.AddField(
            model_name='product',
            name='price',
            field=models.IntegerField(default='0'),
        ),
    ]
