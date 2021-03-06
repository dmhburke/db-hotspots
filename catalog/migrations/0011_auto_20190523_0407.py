# Generated by Django 2.2.1 on 2019-05-23 08:07

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0010_auto_20190521_0632'),
    ]

    operations = [
        migrations.RenameField(
            model_name='addspot',
            old_name='know_before_go',
            new_name='notes',
        ),
        migrations.RemoveField(
            model_name='addspot',
            name='what_good',
        ),
        migrations.AddField(
            model_name='addspot',
            name='location',
            field=models.CharField(blank=True, choices=[('WestVillage', 'West Village'), ('EastVillage', 'East Village')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='addspot',
            name='perfect_for',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Quick', 'Something quick'), ('Last_min', 'Last-minute plans')], max_length=14, null=True),
        ),
    ]
