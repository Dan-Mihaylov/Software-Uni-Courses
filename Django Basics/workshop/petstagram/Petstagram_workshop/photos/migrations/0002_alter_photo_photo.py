# Generated by Django 5.0.1 on 2024-01-24 23:19

import Petstagram_workshop.photos.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='photo',
            field=models.ImageField(upload_to='pet-photos/', validators=[Petstagram_workshop.photos.validators.validate_file_size]),
        ),
    ]
