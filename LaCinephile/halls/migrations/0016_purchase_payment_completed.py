# Generated by Django 3.2.6 on 2021-09-09 03:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('halls', '0015_auto_20210909_0840'),
    ]

    operations = [
        migrations.AddField(
            model_name='purchase',
            name='payment_completed',
            field=models.BooleanField(default=False),
        ),
    ]