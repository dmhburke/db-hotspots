# Generated by Django 2.2.1 on 2019-07-16 02:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0035_auto_20190715_2210'),
    ]

    operations = [
        migrations.AlterField(
            model_name='masteraddmodel',
            name='name',
            field=models.CharField(max_length=60),
        ),
    ]
