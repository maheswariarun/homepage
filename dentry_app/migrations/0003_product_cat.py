# Generated by Django 4.2.2 on 2023-08-10 13:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dentry_app', '0002_product_delete_data_list'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='cat',
            field=models.IntegerField(choices=[(1, 'book'), (2, 'Jewell'), (3, 'Clothes')], default=1, verbose_name='Catagory'),
        ),
    ]