# Generated by Django 4.2 on 2023-04-29 13:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0007_rename_country_shippingaddress_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='shippingaddress',
            name='date_added',
            field=models.DateField(auto_now_add=True),
        ),
    ]
