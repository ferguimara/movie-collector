# Generated by Django 3.2.4 on 2021-07-07 03:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='rating',
            field=models.FloatField(default=5.0),
        ),
        migrations.AddField(
            model_name='movie',
            name='release_year',
            field=models.CharField(default=2000, max_length=4),
        ),
        migrations.AddField(
            model_name='movie',
            name='title',
            field=models.CharField(default='hello', max_length=100),
        ),
    ]
