# Generated by Django 3.2.6 on 2021-08-20 05:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0002_rename_movies_movie'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='summary',
            field=models.CharField(default='Summary', max_length=500),
        ),
    ]