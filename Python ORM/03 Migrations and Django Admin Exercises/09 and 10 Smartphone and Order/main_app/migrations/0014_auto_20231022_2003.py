# Generated by Django 4.2.4 on 2023-10-22 19:03

from django.db import migrations


def get_price(apps, schema_editor):
    Smartphone = apps.get_model('main_app', 'Smartphone')

    for phone in Smartphone.objects.all():
        phone.price = len(phone.brand) * 120
        phone.save()

    change_category(apps, schema_editor)


def change_category(apps, schema_editor):
    Smartphone = apps.get_model('main_app', 'Smartphone')

    for phone in Smartphone.objects.all():
        if phone.price >= 750:
            phone.category = 'Expensive'
        else:
            phone.category = 'Cheap'

        phone.save()


def reverse_changes(apps, schema_editor):
    Smartphone = apps.get_model('main_app', 'Smartphone')

    for phone in Smartphone.objects.all():
        phone.price = 0
        phone.category = 'empty'
        phone.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0013_smartphone'),
    ]

    operations = [
        migrations.RunPython(get_price, reverse_code=reverse_changes)
    ]