# Generated by Django 2.1.3 on 2019-08-12 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('excursao', '0002_auto_20190130_0415'),
    ]

    operations = [
        migrations.CreateModel(
            name='Destino',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_turistico', models.CharField(max_length=100)),
                ('pais', models.CharField(max_length=100)),
                ('estado', models.CharField(max_length=100)),
                ('cidade', models.CharField(max_length=100)),
                ('bairro', models.CharField(max_length=100)),
                ('cep', models.CharField(max_length=100)),
            ],
        ),
    ]
