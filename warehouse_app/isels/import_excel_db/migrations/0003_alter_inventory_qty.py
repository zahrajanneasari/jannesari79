# Generated by Django 4.2.4 on 2023-08-28 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('import_excel_db', '0002_alter_inventory_qty_alter_inventory_depth_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='QTY',
            field=models.IntegerField(blank=True, default=1),
            preserve_default=False,
        ),
    ]