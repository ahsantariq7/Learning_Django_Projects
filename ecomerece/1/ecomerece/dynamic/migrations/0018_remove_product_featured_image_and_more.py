# Generated by Django 4.0.6 on 2022-08-29 17:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0017_product_slug_alter_product_table'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product',
            name='featured_image',
        ),
        migrations.RemoveField(
            model_name='product_image',
            name='image_url',
        ),
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=False, upload_to='Featured Images'),
        ),
        migrations.AddField(
            model_name='product_image',
            name='image',
            field=models.ImageField(default=False, upload_to='Product Images'),
        ),
    ]
