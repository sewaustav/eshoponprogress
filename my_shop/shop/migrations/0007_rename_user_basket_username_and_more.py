# Generated by Django 4.1.5 on 2023-01-31 11:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0006_basket_alter_newcontent_date_of_publication'),
    ]

    operations = [
        migrations.RenameField(
            model_name='basket',
            old_name='user',
            new_name='username',
        ),
        migrations.AlterField(
            model_name='newcontent',
            name='date_of_publication',
            field=models.DateTimeField(default=datetime.datetime(2023, 1, 31, 12, 31, 42, 554499)),
        ),
    ]
