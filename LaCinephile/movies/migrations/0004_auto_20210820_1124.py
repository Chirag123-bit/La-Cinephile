# Generated by Django 3.2.6 on 2021-08-20 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0003_movie_summary'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='desc',
            field=models.TextField(default='Summary'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='summary',
            field=models.CharField(max_length=500),
        ),
    ]
