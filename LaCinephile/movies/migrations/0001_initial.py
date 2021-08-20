# Generated by Django 3.2.6 on 2021-08-18 06:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('poster', models.ImageField(upload_to='static/images/movies')),
                ('trailer', models.URLField()),
                ('imdb', models.FloatField()),
                ('desc', models.TextField()),
                ('actors', models.CharField(max_length=300)),
                ('director', models.CharField(max_length=100)),
            ],
        ),
    ]