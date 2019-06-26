# Generated by Django 2.2.1 on 2019-05-23 13:15

from django.db import migrations, models
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0011_auto_20190523_0407'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='addspot',
            name='id',
        ),
        migrations.AlterField(
            model_name='addspot',
            name='name',
            field=models.CharField(default='New', max_length=30, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='addspot',
            name='perfect_for',
            field=multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Quick', 'Something quick'), ('Last_min', 'Last-min plans'), ('Impress', 'Impressing guests'), ('Date', 'Date night'), ('Group', 'Big group'), ('Cozy', 'Peace & quiet'), ('Expensive', 'Living large'), ('Outdoor', 'Sunny days')], max_length=56, null=True),
        ),
    ]
