# Generated by Django 4.1.5 on 2023-01-25 13:03

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='NewContent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.CharField(max_length=50, verbose_name='Продукт')),
                ('price', models.FloatField(verbose_name='Цена')),
                ('autor', models.CharField(max_length=50, verbose_name='Продавец')),
                ('description', models.TextField(verbose_name='Описание')),
                ('date_of_publication', models.DateTimeField(default=datetime.datetime(2023, 1, 25, 16, 3, 5, 371200))),
            ],
            options={
                'verbose_name': 'NewContent',
                'verbose_name_plural': 'NewContent',
            },
        ),
        migrations.DeleteModel(
            name='Content',
        ),
    ]
