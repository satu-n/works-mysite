# Generated by Django 2.0 on 2019-05-19 01:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprig', '0009_auto_20190519_1019'),
    ]

    operations = [
        migrations.AlterField(
            model_name='step',
            name='loc',
            field=models.IntegerField(null=True, verbose_name='位置番号'),
        ),
    ]
