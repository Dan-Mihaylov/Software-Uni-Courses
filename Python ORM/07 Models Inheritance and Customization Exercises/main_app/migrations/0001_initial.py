# Generated by Django 4.2.4 on 2023-11-05 12:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Assassin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('weapon_type', models.CharField(max_length=100)),
                ('assassination_technique', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DemonHunter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('weapon_type', models.CharField(max_length=100)),
                ('demon_slaying_ability', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Mage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('elemental_power', models.CharField(max_length=100)),
                ('spellbook_type', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FelbladeDemonHunter',
            fields=[
                ('demonhunter_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main_app.demonhunter')),
                ('felblade_ability', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('main_app.demonhunter',),
        ),
        migrations.CreateModel(
            name='Necromancer',
            fields=[
                ('mage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main_app.mage')),
                ('raise_dead_ability', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('main_app.mage',),
        ),
        migrations.CreateModel(
            name='ShadowbladeAssassin',
            fields=[
                ('assassin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main_app.assassin')),
                ('shadowstep_ability', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('main_app.assassin',),
        ),
        migrations.CreateModel(
            name='TimeMage',
            fields=[
                ('mage_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main_app.mage')),
                ('time_magic_mastery', models.CharField(max_length=100)),
                ('temporal_shift_ability', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('main_app.mage',),
        ),
        migrations.CreateModel(
            name='VengeanceDemonHunter',
            fields=[
                ('demonhunter_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main_app.demonhunter')),
                ('vengeance_mastery', models.CharField(max_length=100)),
                ('retribution_ability', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('main_app.demonhunter',),
        ),
        migrations.CreateModel(
            name='ViperAssassin',
            fields=[
                ('assassin_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='main_app.assassin')),
                ('venomous_strikes_mastery', models.CharField(max_length=100)),
                ('venomous_bite_ability', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
            bases=('main_app.assassin',),
        ),
    ]
