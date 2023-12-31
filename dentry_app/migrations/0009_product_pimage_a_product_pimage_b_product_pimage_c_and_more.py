# Generated by Django 4.2.2 on 2023-09-08 20:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dentry_app', '0008_alter_product_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='pimage_a',
            field=models.ImageField(default=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='product',
            name='pimage_b',
            field=models.ImageField(default=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='product',
            name='pimage_c',
            field=models.ImageField(default=True, upload_to='images'),
        ),
        migrations.AddField(
            model_name='product',
            name='pimage_d',
            field=models.ImageField(default=True, upload_to='images'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pimage',
            field=models.ImageField(default=True, upload_to='image'),
        ),
    ]
