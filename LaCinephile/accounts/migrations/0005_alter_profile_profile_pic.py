# Generated by Django 3.2.6 on 2021-09-10 07:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_auto_20210907_1340'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_pic',
            field=models.FileField(default='static/images/sample_user.jpg', upload_to='static/uploads'),
        ),
    ]