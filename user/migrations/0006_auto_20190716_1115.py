# Generated by Django 2.2.3 on 2019-07-16 11:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_user_verified'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='username',
            field=models.CharField(default='', max_length=150),
        ),
    ]
