# Generated by Django 2.2.3 on 2019-08-01 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0009_product_barcode'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='code',
            field=models.CharField(default='', max_length=20, unique=True),
        ),
        migrations.AlterField(
            model_name='size',
            name='code',
            field=models.CharField(default='', max_length=20, unique=True),
        ),
    ]
