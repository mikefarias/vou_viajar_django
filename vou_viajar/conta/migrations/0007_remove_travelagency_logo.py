# Generated by Django 2.1.3 on 2020-04-06 17:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('conta', '0006_auto_20200406_1414'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='travelagency',
            name='logo',
        ),
    ]
