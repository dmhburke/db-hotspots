# Generated by Django 2.2.1 on 2019-06-21 01:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0031_auto_20190620_2118'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='number_rating',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
