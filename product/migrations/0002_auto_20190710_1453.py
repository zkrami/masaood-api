# Generated by Django 2.2.3 on 2019-07-10 14:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='abstractproduct',
            name='gender',
            field=models.CharField(choices=[('female', 'Female'), ('male', 'Male')], max_length=20),
        ),
        migrations.AlterField(
            model_name='abstractproduct',
            name='status',
            field=models.CharField(choices=[('unavailable', 'unavailable'), ('available', 'available')], max_length=20),
        ),
    ]
