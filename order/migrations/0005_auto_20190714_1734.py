# Generated by Django 2.2.3 on 2019-07-14 17:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0005_auto_20190711_1639'),
        ('order', '0004_orderproduct_createdat'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='orderproduct',
            unique_together={('order', 'product')},
        ),
    ]