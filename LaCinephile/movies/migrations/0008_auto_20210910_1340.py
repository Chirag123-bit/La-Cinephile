# Generated by Django 3.2.6 on 2021-09-10 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0007_up_comming_external_site'),
    ]

    operations = [
        migrations.AlterField(
            model_name='now_showing',
            name='poster',
            field=models.ImageField(upload_to='movies'),
        ),
        migrations.AlterField(
            model_name='up_comming',
            name='poster',
            field=models.ImageField(upload_to='movies'),
        ),
    ]
