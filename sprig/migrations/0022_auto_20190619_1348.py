# Generated by Django 2.0 on 2019-06-19 04:48

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprig', '0021_auto_20190619_1344'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 19, 14, 48, 52, 775098), verbose_name='納期'),
        ),
        migrations.AlterField(
            model_name='task',
            name='start',
            field=models.DateTimeField(default=datetime.datetime(2019, 6, 19, 13, 48, 52, 774827), null=True, verbose_name='着手日時'),
        ),
    ]