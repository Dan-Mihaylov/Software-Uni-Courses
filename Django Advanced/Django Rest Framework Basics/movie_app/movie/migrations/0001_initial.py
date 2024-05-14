# Generated by Django 5.0.4 on 2024-04-13 22:26

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('year', models.PositiveSmallIntegerField()),
                ('genre', models.CharField(max_length=100)),
                ('director', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='movie.director')),
            ],
        ),
    ]