# Generated by Django 2.2.1 on 2019-05-20 20:13

from django.db import migrations
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_addspot'),
    ]

    operations = [
        migrations.AddField(
            model_name='addspot',
            name='perfect_for',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('YES', 'Yes'), ('NO', 'No')], max_length=6, null=True),
        ),
    ]
