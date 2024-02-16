# Generated by Django 5.0.2 on 2024-02-14 14:03

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Album',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('album_name', models.CharField(max_length=30, unique=True)),
                ('artist', models.CharField(max_length=30)),
                ('genre', models.CharField(choices=[('Pop', 'Pop Music'), ('Jazz', 'Jazz Music'), ('R&B', 'R&B Music'), ('Rock', 'Rock Music'), ('Country', 'Country Music'), ('Dance', 'Dance Music'), ('Hip Hop', 'Hip Hop Music'), ('Other', 'Other')], max_length=30)),
                ('description', models.TextField(blank=True, null=True)),
                ('image_url', models.URLField()),
                ('price', models.FloatField(validators=[django.core.validators.MinValueValidator(0)])),
                ('owner', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='albums', to='account.profile')),
            ],
        ),
    ]
