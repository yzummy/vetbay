# Generated by Django 2.0.2 on 2018-02-11 03:58

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    replaces = [('account', '0018_company'), ('account', '0019_auto_20180210_1543'), ('account', '0020_auto_20180210_1909'), ('account', '0021_auto_20180210_1934'), ('account', '0022_auto_20180210_1937'), ('account', '0020_auto_20180210_2109'), ('account', '0023_merge_20180210_2128'), ('account', '0024_user_is_veteran'), ('account', '0023_auto_20180210_2122'), ('account', '0024_auto_20180210_2132'), ('account', '0025_merge_20180210_2153')]

    dependencies = [
        ('account', '0017_auto_20180206_0957'),
        ('order', '0033_auto_20180123_0832'),
        ('impersonate', '0001_initial'),
        ('social_django', '0008_partial_timestamp'),
        ('cart', '0005_auto_20180108_0814'),
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('company_name', models.CharField(max_length=256, unique=True)),
                ('company_desc', models.CharField(blank=True, max_length=256)),
                ('company_logo', models.ImageField(blank=True, null=True, upload_to='')),
                ('company_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='user',
            name='company',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='account.Company'),
        ),
        migrations.AddField(
            model_name='user',
            name='is_veteran',
            field=models.NullBooleanField(default=False),
        ),
    ]