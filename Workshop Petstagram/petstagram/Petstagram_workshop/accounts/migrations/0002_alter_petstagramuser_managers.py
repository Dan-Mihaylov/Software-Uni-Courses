# Generated by Django 5.0.1 on 2024-03-08 15:38

import Petstagram_workshop.accounts.managers
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='petstagramuser',
            managers=[
                ('objects', Petstagram_workshop.accounts.managers.PetstagramUserManager()),
            ],
        ),
    ]