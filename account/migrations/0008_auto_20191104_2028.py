# Generated by Django 2.2.6 on 2019-11-04 14:28

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0007_auto_20191104_2027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='date',
            field=models.DateTimeField(default=datetime.datetime(2019, 11, 4, 20, 28, 25, 782116)),
        ),
    ]