# Generated by Django 2.1.2 on 2018-12-09 23:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0017_registro'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendedor',
            name='usuarioVendedor',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Registro'),
        ),
    ]