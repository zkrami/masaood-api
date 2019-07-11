# Generated by Django 2.2.3 on 2019-07-11 11:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Center',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nameEn', models.CharField(max_length=255)),
                ('nameAr', models.CharField(max_length=255)),
                ('lat', models.FloatField()),
                ('lng', models.FloatField()),
                ('createdAt', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
