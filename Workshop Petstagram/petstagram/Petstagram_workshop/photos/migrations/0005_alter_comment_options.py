# Generated by Django 5.0.1 on 2024-03-08 15:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0004_comment_like'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ['-added_on']},
        ),
    ]
