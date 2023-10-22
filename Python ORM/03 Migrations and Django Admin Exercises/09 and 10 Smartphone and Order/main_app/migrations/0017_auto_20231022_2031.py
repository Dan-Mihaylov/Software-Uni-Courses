from datetime import datetime, timedelta

from django.db import migrations


def change_delivery_warranty(apps, schema_editor):
    Order = apps.get_model('main_app', 'Order')

    for order in Order.objects.all():
        if order.status == 'Pending':
            order.delivery = order.order_date + timedelta(days=3)
        elif order.status == 'Completed':
            order.warranty = '24 months'
        elif order.status == 'Cancelled':
            order.delete()
            continue

        order.save()


def reset_default_delivery_warranty(apps, schema_editor):
    Order = apps.get_model('main_app', 'Order')

    for order in Order.objects.all():
        order.warranty = 'No warranty'
        if order.delivery:
            order.delivery = None
        order.save()





class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0016_auto_20231022_2023'),
    ]

    operations = [
        migrations.RunPython(change_delivery_warranty, reverse_code=reset_default_delivery_warranty)
    ]
