# Generated by Django 2.0.2 on 2018-02-11 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0023_auto_20180210_2122'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='is_veteran',
            field=models.NullBooleanField(default=False),
        ),
    ]