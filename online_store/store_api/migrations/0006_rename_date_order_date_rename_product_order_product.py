# Generated by Django 4.1 on 2022-08-29 06:31

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store_api', '0005_rename_date_order_date_rename_product_order_product'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='date',
            new_name='Date',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='product',
            new_name='Product',
        ),
    ]