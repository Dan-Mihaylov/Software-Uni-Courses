# Generated by Django 5.0.2 on 2024-02-13 16:12

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('make', models.CharField(max_length=30)),
                ('model', models.CharField(max_length=30)),
                ('engine_type', models.CharField(choices=[('P', 'Petrol'), ('D', 'Diesel'), ('H', 'Hybrid'), ('E', 'Electric')], max_length=15)),
                ('year', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1890, 'Value must be bigger than 1889'), django.core.validators.MaxValueValidator(2024, 'Value cannot be bigger than 2024')])),
                ('added_on', models.DateTimeField(auto_now_add=True)),
                ('modified_on', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]