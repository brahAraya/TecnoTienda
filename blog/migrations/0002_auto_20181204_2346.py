# Generated by Django 2.1.2 on 2018-12-05 02:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Tiendas',
            new_name='Tienda',
        ),
        migrations.RenameModel(
            old_name='ventas',
            new_name='Venta',
        ),
    ]
