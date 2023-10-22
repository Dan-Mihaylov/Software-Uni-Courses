import random

from django.db import migrations



class Migration(migrations.Migration):

    def populate_barcode(apps, schema_editors):
        Product = apps.get_model("main_app", "Product")
        for product in Product.objects.all():
            product.barcode = random.randint(100000000, 999999999)
            product.save()

    dependencies = [
        ('main_app', '0004_product_barcode_alter_product_category_and_more'),
    ]

    operations = [
        migrations.RunPython(populate_barcode)
    ]
