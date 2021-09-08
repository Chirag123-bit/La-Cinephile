# Generated by Django 3.2.6 on 2021-09-08 08:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('halls', '0011_auto_20210907_0826'),
    ]

    operations = [
        migrations.AddField(
            model_name='ticket',
            name='status',
            field=models.CharField(choices=[(1, 'Active'), (2, 'Canceled'), (3, 'Expired')], default=1, max_length=100),
        ),
        migrations.AlterField(
            model_name='movie_hall',
            name='time',
            field=models.CharField(choices=[('7AM - 10AM', '7AM - 10AM'), ('11AM - 2PM', '11AM - 2PM'), ('3PM - 6PM', '3PM - 6PM'), ('7PM - 10PM', '7PM - 10PM')], default='7PM - 10PM', max_length=100),
        ),
    ]
