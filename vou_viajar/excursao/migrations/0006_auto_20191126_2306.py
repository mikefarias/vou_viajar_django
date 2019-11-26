# Generated by Django 2.1.3 on 2019-11-26 23:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('excursao', '0005_auto_20191120_0748'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrcamentoDetalhesTransporte',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='orcamentoservico',
            name='tipo_servico',
        ),
        migrations.RemoveField(
            model_name='orcamento',
            name='servico',
        ),
        migrations.AddField(
            model_name='orcamento',
            name='tipo_servico',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.PROTECT, to='excursao.TipoPrestadorServico'),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='OrcamentoServico',
        ),
        migrations.AddField(
            model_name='orcamentodetalhestransporte',
            name='orcamento',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='excursao.Orcamento'),
        ),
        migrations.AddField(
            model_name='orcamentodetalhestransporte',
            name='transporte',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='excursao.Transporte'),
        ),
    ]
