# Generated by Django 2.1.3 on 2020-04-06 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('conta', '0004_auto_20200406_1239'),
    ]

    operations = [
        migrations.AlterField(
            model_name='travelagency',
            name='logo',
            field=models.ImageField(default='static/logo_agency/none/no-img.jpg', upload_to='static/logo_agency'),
        ),
    ]
