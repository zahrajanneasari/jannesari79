# Generated by Django 4.2.4 on 2023-08-30 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('import_excel_db', '0011_inventory_qty_inventory_brand_inventory_coordinate_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inventory',
            name='shape',
            field=models.CharField(choices=[('مستطیل', 'مستطیل'), ('استوانه', 'استوانه'), ('مربع', 'مربع'), ('دایره', 'دایره')], default='', max_length=50, null=True),
        ),
    ]
