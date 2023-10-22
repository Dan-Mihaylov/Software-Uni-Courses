# Generated by Django 4.2.4 on 2023-10-22 19:23

from django.db import migrations


def get_total_price(apps, schema_editor):
    Order = apps.get_model('main_app', 'Order')

    for order in Order.objects.all():
        order.total_price = order.product_price * order.amount
        order.save()


def reverse_total_price(apps, schema_editor):
    Order = apps.get_model('main_app', 'Order')

    for order in Order.objects.all():
        order.total_price = 0
        order.save()


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0015_order'),
    ]

    operations = [
        migrations.RunPython(get_total_price, reverse_code=reverse_total_price)
    ]