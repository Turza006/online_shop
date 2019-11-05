# Generated by Django 2.2.6 on 2019-11-05 15:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cart',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('buyer_id', models.IntegerField()),
                ('product_id', models.IntegerField()),
                ('quantity', models.IntegerField(default=1)),
                ('seller_id', models.IntegerField()),
                ('date', models.DateTimeField(default=datetime.datetime(2019, 11, 5, 21, 52, 17, 780145))),
            ],
        ),
    ]
