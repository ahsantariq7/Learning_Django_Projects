# Generated by Django 4.0.6 on 2022-08-19 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dynamic', '0004_shop_by_brand1_delete_shop_by_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shop_by_brand1',
            name='brand_logo',
            field=models.ImageField(upload_to='media'),
        ),
    ]
