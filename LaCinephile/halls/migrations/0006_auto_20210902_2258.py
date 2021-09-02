# Generated by Django 3.2.6 on 2021-09-02 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('halls', '0005_auto_20210902_2256'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie_hall',
            name='day',
            field=models.CharField(choices=[('Sunday', 'Sunday'), ('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday')], default='Sunday', max_length=100),
        ),
        migrations.AlterField(
            model_name='movie_hall',
            name='time',
            field=models.CharField(choices=[('7AM - 10AM', '7AM - 10AM'), ('11AM - 2PM', '11AM - 2PM'), ('3PM - 6PM', '3PM - 6PM'), ('7PM - 10PM', '7PM - 10PM')], default="7PM - 10PM'", max_length=100),
        ),
    ]
