# Generated by Django 3.2.4 on 2022-03-14 11:52

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dagracemarketapp', '0005_remove_product_user'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='product_name',
        ),
    ]
