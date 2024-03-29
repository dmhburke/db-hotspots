# Generated by Django 2.2.1 on 2019-05-24 19:16

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0018_auto_20190524_1513'),
    ]

    operations = [
        migrations.CreateModel(
            name='AddSpot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='New', max_length=30)),
                ('location', models.CharField(blank=True, choices=[('Alphabet City', 'Alphabet City'), ('Astoria', 'Astoria'), ('Battery Park', 'Battery Park'), ('Bed-Stuy', 'Bed-Stuy'), ('DUMBO', 'DUMBO'), ('East Village', 'East Village'), ('Financial District', 'Financial District'), ('Lower East Side', 'Lower East Side'), ('NoHo', 'NoHo'), ('SoHo', 'SoHo'), ('Times Square', 'Times Square'), ('Theater District', 'Theater District'), ('Tribeca', 'Tribeca'), ('Upper East Side', 'Upper East Side'), ('West Village', 'West Village'), ('Williamsburg', 'Williamsburg')], max_length=30, null=True)),
                ('category', models.CharField(blank=True, choices=[('FOOD', 'Food'), ('COCKTAILS', 'Cocktails'), ('WINE', 'Wine'), ('BEER', 'Beer'), ('COFFEE', 'Coffee'), ('OTHER', 'Other')], max_length=30, null=True)),
                ('spotpic', models.FileField(blank=True, null=True, upload_to='spotpictures')),
                ('perfect_for', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('Something quick', 'Something quick'), ('Last-min plans', 'Last-min plans'), ('Impressing guests', 'Impressing guests'), ('Date night', 'Date night'), ('Big group', 'Big group'), ('Peace & quiet', 'Peace & quiet'), ('Living large', 'Living large'), ('Sunny days', 'Sunny days')], max_length=107, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('date', models.DateTimeField(auto_now=True, null=True)),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='SpotLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, choices=[('Alphabet City', 'Alphabet City'), ('Astoria', 'Astoria'), ('Battery Park', 'Battery Park'), ('Bed-Stuy', 'Bed-Stuy'), ('DUMBO', 'DUMBO'), ('East Village', 'East Village'), ('Financial District', 'Financial District'), ('Lower East Side', 'Lower East Side'), ('NoHo', 'NoHo'), ('SoHo', 'SoHo'), ('Times Square', 'Times Square'), ('Theater District', 'Theater District'), ('Tribeca', 'Tribeca'), ('Upper East Side', 'Upper East Side'), ('West Village', 'West Village'), ('Williamsburg', 'Williamsburg')], max_length=30, null=True)),
                ('category', models.CharField(blank=True, choices=[('FOOD', 'Food'), ('COCKTAILS', 'Cocktails'), ('WINE', 'Wine'), ('BEER', 'Beer'), ('COFFEE', 'Coffee'), ('OTHER', 'Other')], max_length=30, null=True)),
                ('name', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.AddSpot')),
            ],
        ),
    ]
