# Generated by Django 2.1.5 on 2019-03-08 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0014_auto_20190308_2155'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='name',
            field=models.CharField(default='', max_length=200, verbose_name='Movie name'),
        ),
    ]