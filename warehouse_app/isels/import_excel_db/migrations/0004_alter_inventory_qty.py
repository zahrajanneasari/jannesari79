# Generated by Django 4.2.4 on 2023-08-28 04:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('import_excel_db', '0003_alter_inventory_qty'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='QTY',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
