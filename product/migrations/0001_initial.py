# Generated by Django 2.2.6 on 2019-11-05 15:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('name', models.CharField(max_length=50)),
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Date', models.DateTimeField(default=datetime.datetime(2019, 11, 5, 21, 52, 17, 838144))),
                ('image', models.ImageField(null=True, upload_to='')),
                ('price', models.IntegerField()),
                ('seller', models.CharField(max_length=50)),
                ('category', models.ManyToManyField(to='product.Category')),
            ],
        ),
    ]
