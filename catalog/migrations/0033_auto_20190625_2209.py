# Generated by Django 2.2.1 on 2019-06-26 02:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0032_profile_number_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addreview',
            name='category',
            field=models.CharField(blank=True, choices=[('', '----'), ('FOOD', 'Food'), ('COCKTAILS', 'Cocktails'), ('WINE', 'Wine'), ('BEER', 'Beer'), ('COFFEE', 'Coffee'), ('OTHER', 'Other')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='addreview',
            name='location',
            field=models.CharField(blank=True, choices=[('', '----'), ('Alphabet City', 'Alphabet City'), ('Astoria', 'Astoria'), ('Battery Park', 'Battery Park'), ('Bed-Stuy', 'Bed-Stuy'), ('Brooklyn Heights', 'Brooklyn Heights'), ('Central Park', 'Central Park'), ('Chelsea', 'Chelsea'), ('Clinton Hill', 'Clinton Hill'), ('Cobble Hill', 'Cobble Hill'), ('DUMBO', 'DUMBO'), ('East Village', 'East Village'), ('Financial District', 'Financial District'), ('Fort Greene', 'Fort Greene'), ('Harlem', 'Harlem'), ("Hell's Kitchen", "Hell's Kitchen"), ('Kips Bay', 'Kips Bay'), ('Korea Town', 'Korea Town'), ('Long Island City', 'Long Island City'), ('Lower East Side', 'Lower East Side'), ('NoHo', 'NoHo'), ('NoMad', 'NoMad'), ('SoHo', 'SoHo'), ('Times Square', 'Times Square'), ('Theater District', 'Theater District'), ('Tribeca', 'Tribeca'), ('Upper East Side', 'Upper East Side'), ('West Village', 'West Village'), ('Williamsburg', 'Williamsburg')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='reviewrecord',
            name='category',
            field=models.CharField(blank=True, choices=[('', '----'), ('FOOD', 'Food'), ('COCKTAILS', 'Cocktails'), ('WINE', 'Wine'), ('BEER', 'Beer'), ('COFFEE', 'Coffee'), ('OTHER', 'Other')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='reviewrecord',
            name='location',
            field=models.CharField(blank=True, choices=[('', '----'), ('Alphabet City', 'Alphabet City'), ('Astoria', 'Astoria'), ('Battery Park', 'Battery Park'), ('Bed-Stuy', 'Bed-Stuy'), ('Brooklyn Heights', 'Brooklyn Heights'), ('Central Park', 'Central Park'), ('Chelsea', 'Chelsea'), ('Clinton Hill', 'Clinton Hill'), ('Cobble Hill', 'Cobble Hill'), ('DUMBO', 'DUMBO'), ('East Village', 'East Village'), ('Financial District', 'Financial District'), ('Fort Greene', 'Fort Greene'), ('Harlem', 'Harlem'), ("Hell's Kitchen", "Hell's Kitchen"), ('Kips Bay', 'Kips Bay'), ('Korea Town', 'Korea Town'), ('Long Island City', 'Long Island City'), ('Lower East Side', 'Lower East Side'), ('NoHo', 'NoHo'), ('NoMad', 'NoMad'), ('SoHo', 'SoHo'), ('Times Square', 'Times Square'), ('Theater District', 'Theater District'), ('Tribeca', 'Tribeca'), ('Upper East Side', 'Upper East Side'), ('West Village', 'West Village'), ('Williamsburg', 'Williamsburg')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='singlelocation',
            name='category',
            field=models.CharField(blank=True, choices=[('', '----'), ('FOOD', 'Food'), ('COCKTAILS', 'Cocktails'), ('WINE', 'Wine'), ('BEER', 'Beer'), ('COFFEE', 'Coffee'), ('OTHER', 'Other')], max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='singlelocation',
            name='location',
            field=models.CharField(blank=True, choices=[('', '----'), ('Alphabet City', 'Alphabet City'), ('Astoria', 'Astoria'), ('Battery Park', 'Battery Park'), ('Bed-Stuy', 'Bed-Stuy'), ('Brooklyn Heights', 'Brooklyn Heights'), ('Central Park', 'Central Park'), ('Chelsea', 'Chelsea'), ('Clinton Hill', 'Clinton Hill'), ('Cobble Hill', 'Cobble Hill'), ('DUMBO', 'DUMBO'), ('East Village', 'East Village'), ('Financial District', 'Financial District'), ('Fort Greene', 'Fort Greene'), ('Harlem', 'Harlem'), ("Hell's Kitchen", "Hell's Kitchen"), ('Kips Bay', 'Kips Bay'), ('Korea Town', 'Korea Town'), ('Long Island City', 'Long Island City'), ('Lower East Side', 'Lower East Side'), ('NoHo', 'NoHo'), ('NoMad', 'NoMad'), ('SoHo', 'SoHo'), ('Times Square', 'Times Square'), ('Theater District', 'Theater District'), ('Tribeca', 'Tribeca'), ('Upper East Side', 'Upper East Side'), ('West Village', 'West Village'), ('Williamsburg', 'Williamsburg')], max_length=30, null=True),
        ),
    ]
