# Generated by Django 2.2.1 on 2019-06-08 11:28

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('catalog', '0021_auto_20190601_1433'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='New', max_length=30)),
                ('location', models.CharField(blank=True, choices=[('Alphabet City', 'Alphabet City'), ('Astoria', 'Astoria'), ('Battery Park', 'Battery Park'), ('Bed-Stuy', 'Bed-Stuy'), ('DUMBO', 'DUMBO'), ('East Village', 'East Village'), ('Financial District', 'Financial District'), ('Lower East Side', 'Lower East Side'), ('NoHo', 'NoHo'), ('SoHo', 'SoHo'), ('Times Square', 'Times Square'), ('Theater District', 'Theater District'), ('Tribeca', 'Tribeca'), ('Upper East Side', 'Upper East Side'), ('West Village', 'West Village'), ('Williamsburg', 'Williamsburg')], max_length=30, null=True)),
                ('category', models.CharField(blank=True, choices=[('FOOD', 'Food'), ('COCKTAILS', 'Cocktails'), ('WINE', 'Wine'), ('BEER', 'Beer'), ('COFFEE', 'Coffee'), ('OTHER', 'Other')], max_length=30, null=True)),
                ('rating', models.DecimalField(blank=True, decimal_places=1, max_digits=3, null=True, validators=[django.core.validators.MaxValueValidator(10), django.core.validators.MinValueValidator(0)])),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
