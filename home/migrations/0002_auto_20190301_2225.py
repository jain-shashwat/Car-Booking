# Generated by Django 2.1.5 on 2019-03-01 16:55

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='last_date',
            field=models.DateField(default=datetime.datetime(2019, 3, 1, 16, 55, 28, 457474, tzinfo=utc)),
        ),
    ]
