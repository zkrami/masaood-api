# Generated by Django 2.2.3 on 2019-07-21 13:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('media', '0005_auto_20190714_1734'),
    ]

    operations = [
        migrations.AddField(
            model_name='media',
            name='type',
            field=models.CharField(default='image', max_length=30),
        ),
    ]
