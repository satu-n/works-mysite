# Generated by Django 2.0 on 2019-05-18 15:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sprig', '0004_auto_20190519_0012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='deadline',
            field=models.DateTimeField(blank=True, null=True, verbose_name='納期'),
        ),
    ]
