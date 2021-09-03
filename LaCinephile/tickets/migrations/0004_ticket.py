# Generated by Django 3.2.6 on 2021-09-03 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('halls', '0010_movie_hall_discount'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('tickets', '0003_remove_categories_valid'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ticket',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seats', models.TextField(null=True)),
                ('discount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='tickets.categories')),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='halls.movie_hall')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]