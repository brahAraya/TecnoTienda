# Generated by Django 2.1.2 on 2018-12-09 04:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0011_auto_20181209_0019'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='porcentaje_desc',
            field=models.IntegerField(default=0),
        ),
    ]
