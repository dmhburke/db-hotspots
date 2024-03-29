# Generated by Django 2.2.1 on 2019-07-22 21:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0041_auto_20190722_1700'),
    ]

    operations = [
        migrations.CreateModel(
            name='SingleLocationRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('perfect_for', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Something quick', 'Something quick'), ('Last-min plans', 'Last-min plans'), ('Breakfast', 'Breakfast'), ('Impressing guests', 'Impressing guests'), ('Date night', 'Date night'), ('Big group', 'Big group'), ('Peace & quiet', 'Peace & quiet'), ('Living large', 'Living large'), ('Sunny days', 'Sunny days')], max_length=117, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('country', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('category1', models.CharField(blank=True, max_length=30, null=True)),
                ('category2', models.CharField(blank=True, max_length=30, null=True)),
                ('category3', models.CharField(blank=True, max_length=30, null=True)),
                ('postcode', models.CharField(blank=True, max_length=30, null=True)),
                ('suburb', models.CharField(blank=True, max_length=30, null=True)),
                ('date', models.DateTimeField(auto_now=True, null=True)),
                ('temperature', models.DecimalField(blank=True, decimal_places=8, max_digits=10, null=True)),
                ('count_ratings', models.IntegerField(blank=True, null=True)),
                ('ave_ratings', models.DecimalField(blank=True, decimal_places=0, max_digits=1, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='CleanReviewModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=60)),
                ('rating', models.CharField(blank=True, max_length=30, null=True)),
                ('perfect_for', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Something quick', 'Something quick'), ('Last-min plans', 'Last-min plans'), ('Breakfast', 'Breakfast'), ('Impressing guests', 'Impressing guests'), ('Date night', 'Date night'), ('Big group', 'Big group'), ('Peace & quiet', 'Peace & quiet'), ('Living large', 'Living large'), ('Sunny days', 'Sunny days')], max_length=117, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('city', models.CharField(blank=True, max_length=30, null=True)),
                ('country', models.CharField(blank=True, max_length=30, null=True)),
                ('address', models.CharField(blank=True, max_length=50, null=True)),
                ('category1', models.CharField(blank=True, max_length=30, null=True)),
                ('category2', models.CharField(blank=True, max_length=30, null=True)),
                ('category3', models.CharField(blank=True, max_length=30, null=True)),
                ('postcode', models.CharField(blank=True, max_length=30, null=True)),
                ('suburb', models.CharField(blank=True, max_length=30, null=True)),
                ('date', models.DateTimeField(auto_now=True, null=True)),
                ('temperature', models.DecimalField(blank=True, decimal_places=8, max_digits=10, null=True)),
                ('ave_ratings', models.DecimalField(blank=True, decimal_places=0, max_digits=1, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
