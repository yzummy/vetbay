# Generated by Django 2.0.2 on 2018-02-11 03:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0022_auto_20180210_1937'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='is_veteran',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='company',
            name='company_logo',
            field=models.ImageField(blank=None, default=1, upload_to=''),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='user',
            name='company',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.Company'),
        ),
    ]
