# Generated by Django 2.2.6 on 2019-11-04 15:36

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='Date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 4, 21, 36, 45, 79440)),
        ),
    ]