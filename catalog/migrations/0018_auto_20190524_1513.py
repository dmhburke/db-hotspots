# Generated by Django 2.2.1 on 2019-05-24 19:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0017_spotlocation'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='spotlocation',
            name='name',
        ),
        migrations.DeleteModel(
            name='AddSpot',
        ),
        migrations.DeleteModel(
            name='SpotLocation',
        ),
    ]
