# Generated by Django 4.2 on 2023-12-14 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_products_shirts_brand_shirts_description'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Products',
            new_name='Product',
        ),
    ]
