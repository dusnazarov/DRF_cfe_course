# Generated by Django 4.2.1 on 2023-07-24 09:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_product_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='user',
        ),
    ]
