# Generated by Django 2.1.3 on 2020-04-07 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conta', '0009_auto_20200407_1102'),
    ]

    operations = [
        migrations.AddField(
            model_name='travelagency',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='img/logo_agency'),
        ),
        migrations.AddField(
            model_name='travelagency',
            name='name',
            field=models.CharField(default='Vou Viajar', max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(blank=True, null=True, upload_to='img/profile'),
        ),
    ]
