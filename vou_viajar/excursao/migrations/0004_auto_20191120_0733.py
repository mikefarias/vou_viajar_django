# Generated by Django 2.1.3 on 2019-11-20 10:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('conta', '0001_initial'),
        ('excursao', '0003_auto_20191118_1348'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrcamentoServico',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('servico', models.IntegerField()),
                ('tipo_servico', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='excursao.TipoServico')),
            ],
        ),
        migrations.AddField(
            model_name='orcamento',
            name='agencia',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='conta.Agencia'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orcamento',
            name='cotacao',
            field=models.IntegerField(default=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orcamento',
            name='excursao',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='excursao.Excursao'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orcamento',
            name='horario_chegada',
            field=models.DateTimeField(default='2019-11-18 09:00:00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orcamento',
            name='horario_partida',
            field=models.DateTimeField(default='2019-11-18 10:00:00'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orcamento',
            name='observacao',
            field=models.CharField(default='', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orcamento',
            name='prestador_servico',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='excursao.PrestadorServico'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='orcamento',
            name='selecionado',
            field=models.BooleanField(blank=True, default=False, null=True),
        ),
        migrations.AddField(
            model_name='orcamento',
            name='servico',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='excursao.OrcamentoServico'),
            preserve_default=False,
        ),
    ]
