# Generated by Django 5.1.7 on 2025-03-29 14:00

import django.core.validators
import django.utils.timezone
import pokemon_app.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('move_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pokemon',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, validators=[pokemon_app.validators.validate_name])),
                ('level', models.IntegerField(default=1, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)])),
                ('date_encountered', models.DateField(default='2008-01-01')),
                ('date_captured', models.DateTimeField(default=django.utils.timezone.now)),
                ('description', models.TextField(default='Unknown', validators=[django.core.validators.MinLengthValidator(7), django.core.validators.MaxLengthValidator(150)])),
                ('captured', models.BooleanField(default=False)),
                ('moves', models.ManyToManyField(related_name='pokemon', to='move_app.move')),
            ],
        ),
    ]
