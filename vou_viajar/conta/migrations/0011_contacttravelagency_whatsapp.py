# Generated by Django 2.1.3 on 2020-04-07 19:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conta', '0010_auto_20200407_1621'),
    ]

    operations = [
        migrations.AddField(
            model_name='contacttravelagency',
            name='whatsapp',
            field=models.CharField(default=79996063994, max_length=11),
            preserve_default=False,
        ),
    ]
