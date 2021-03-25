# Generated by Django 2.1 on 2021-03-10 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20210310_1308'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='gcash_number',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='paypal_email',
            field=models.EmailField(blank=True, max_length=100, null=True, unique=True),
        ),
    ]
