# Generated by Django 2.1.2 on 2018-12-07 19:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20181207_1609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='vendedor',
            name='ventas',
        ),
        migrations.AddField(
            model_name='venta',
            name='vendedor',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Vendedor'),
        ),
    ]
