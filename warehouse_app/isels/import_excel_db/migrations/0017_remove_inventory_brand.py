# Generated by Django 4.2.4 on 2023-08-30 09:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('import_excel_db', '0016_alter_inventory_shape'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='inventory',
            name='brand',
        ),
    ]
