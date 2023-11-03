# Generated by Django 4.2.4 on 2023-08-28 05:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('import_excel_db', '0004_alter_inventory_qty'),
    ]

    operations = [
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Empcode', models.CharField(default='', max_length=10)),
                ('firstName', models.CharField(max_length=150, null=True)),
                ('middleName', models.CharField(max_length=100, null=True)),
                ('lastName', models.CharField(max_length=100, null=True)),
                ('email', models.CharField(max_length=30, null=True)),
                ('phoneNo', models.CharField(default='', max_length=12, null=True)),
                ('address', models.CharField(default='', max_length=500, null=True)),
                ('DOB', models.DateField(blank=True, null=True)),
                ('gender', models.CharField(default='', max_length=5, null=True)),
                ('qualification', models.CharField(default='', max_length=50, null=True)),
                ('salary', models.FloatField(default='', max_length=50, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Inventory',
        ),
    ]
