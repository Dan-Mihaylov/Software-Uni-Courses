# Generated by Django 5.0.1 on 2024-01-24 23:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0002_alter_photo_photo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='modified_on',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
