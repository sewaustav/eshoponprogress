# Generated by Django 4.1.5 on 2023-02-15 20:31

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0009_alter_newcontent_date_of_publication_postcountviews'),
    ]

    operations = [
        migrations.AlterField(
            model_name='newcontent',
            name='date_of_publication',
            field=models.DateTimeField(default=datetime.datetime(2023, 2, 15, 21, 31, 8, 912973)),
        ),
        migrations.DeleteModel(
            name='PostCountViews',
        ),
    ]
