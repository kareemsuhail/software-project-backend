# Generated by Django 2.0.1 on 2018-04-19 18:01

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainEndPoint', '0002_auto_20180419_2056'),
    ]

    operations = [
        migrations.AlterField(
            model_name='budget',
            name='start_date',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
