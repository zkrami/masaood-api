# Generated by Django 2.2.3 on 2019-07-17 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0006_order_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='total',
            field=models.DecimalField(decimal_places=4, max_digits=10),
        ),
    ]
