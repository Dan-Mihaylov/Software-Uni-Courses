# Generated by Django 4.2.4 on 2023-10-20 14:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_auto_20231020_1433'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='barcode',
            field=models.PositiveIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='category',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='supplier',
            field=models.CharField(max_length=150, null=True),
        ),
    ]
