# Generated by Django 2.2.1 on 2019-06-01 17:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0019_addspot_spotlocation'),
    ]

    operations = [
        migrations.CreateModel(
            name='TestEntryModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default='New', max_length=30, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TestStoreModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=30, null=True)),
            ],
        ),
    ]
