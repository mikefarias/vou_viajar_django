# Generated by Django 2.1.3 on 2020-04-07 14:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conta', '0008_auto_20200407_0944'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='img/logo_agency'),
        ),
    ]
