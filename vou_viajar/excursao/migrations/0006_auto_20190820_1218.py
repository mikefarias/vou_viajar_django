# Generated by Django 2.1.3 on 2019-08-20 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excursao', '0005_auto_20190820_1209'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='excursao',
            name='destino',
        ),
        migrations.AddField(
            model_name='excursao',
            name='destino',
            field=models.ManyToManyField(to='excursao.Destino'),
        ),
    ]
