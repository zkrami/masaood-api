# Generated by Django 2.2.3 on 2019-08-20 14:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0013_abstractproduct_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='abstractproduct',
            name='order',
            field=models.IntegerField(default=None, null=True),
        ),
    ]
