# Generated by Django 4.0.6 on 2022-08-06 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_employee'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='phone',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='stratcontract',
            name='phone',
            field=models.CharField(max_length=100),
        ),
    ]
