# Generated by Django 4.0.6 on 2022-08-15 17:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('core', '0013_remove_contact_user_remove_employee_user_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='stratcontract1',
            name='user',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
