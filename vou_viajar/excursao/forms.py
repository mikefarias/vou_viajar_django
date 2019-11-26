from django import forms

from .models import Excursao, Destino, Transporte, PrestadorServico, TipoPrestadorServico, Orcamento, Roteiro
class ExcursaoForm(forms.ModelForm):

    titulo = forms.CharField(label='Título', help_text='Em até 50 caracteres')
    descricao = forms.CharField(label='Descrição',  help_text='Em até 100 caracteres')
    destino = forms.ModelMultipleChoiceField(
        queryset=Destino.objects.all()),
    horario_inicio = forms.SplitDateTimeField(
        widget=forms.SplitDateTimeWidget(
            date_attrs={'type': 'date'},
            time_attrs={'type': 'time'},
        )
    )
    horario_fim = forms.SplitDateTimeField(
        widget=forms.SplitDateTimeWidget(
            date_attrs={'type': 'date'},
            time_attrs={'type': 'time'},
        )
    )

    class Meta:
        model = Excursao
        fields = [
            'titulo',
            'descricao',
            'origem',
            'destino',
            'horario_inicio',
            'horario_fim',
        ]


class DestinoForm(forms.ModelForm):
    
    class Meta:
        model = Destino
        fields = [
            'nome_turistico',
            'pais',
            'estado',
            'cidade',
            'bairro',
            'cep',
        ]

class PrestadorForm(forms.ModelForm):

    categoria = forms.ModelMultipleChoiceField(queryset=TipoPrestadorServico.objects.all()),
    nome = forms.CharField(label='Nome do Prestador de Serviço')
    cnpj_cpf = forms.CharField(label='CPNJ/CPF')
    pessoa_juridica = forms.BooleanField(label='Pessoa Jurídica')
    cadastur = forms.CharField(label='Cadastur')
    email = forms.EmailField(label='E-mail')
    telefone = forms.CharField(label='Telefone')
    endereco = forms.CharField(label='Endereço')
    horario_funcionamento = forms.CharField(label='Horário de Funcionamento')

    class Meta: 
        model = PrestadorServico
        fields = [
            'categoria',
            'nome',
            'cnpj_cpf',
            'pessoa_juridica',
            'cadastur',
            'email',
            'telefone',
            'endereco',
            'horario_funcionamento',
        ]

class TransporteForm(forms.ModelForm):

    prestador_servico = forms.ModelChoiceField(queryset=PrestadorServico.objects.all(), label='Prestador de Serviço')
    modelo = forms.CharField(label='Modelo do Transporte')
    marca = forms.CharField(label='Marca')
    ano = forms.IntegerField(label='Ano')
    poltronas = forms.IntegerField(label='Quantidade de Poltronas')
    banheiro = forms.BooleanField(label='Tem banheiro?', required=False)
    frigobar = forms.BooleanField(label='Tem frigobar?', required=False)
    ar_condicionado = forms.BooleanField(label='Tem ar-condicionado?', required=False)
    som = forms.BooleanField(label='Tem som?', required=False)
    tv = forms.BooleanField(label='Tem TV?', required=False)
    observacao = forms.CharField(label='Observações sobre o veículo')

    class Meta:
        model = Transporte
        fields = [
            'prestador_servico',
            'modelo',
            'marca',
            'ano',
            'poltronas',
            'banheiro',
            'frigobar',
            'ar_condicionado',
            'som',
            'tv',
            'observacao',
        ]


class OrcamentoForm(forms.ModelForm):
    excursao = forms.ModelChoiceField(queryset=Excursao.objects.all(), label='Excursão')
    tipo_prestador_servico = forms.ModelChoiceField(queryset=TipoPrestadorServico.objects.all(), label='Categoria Prestação de Serviço')
    prestador_servico = forms.ModelChoiceField(queryset=PrestadorServico.objects.all(), label='Prestador de Serviço')
    cotacao = forms.IntegerField(label='Cotação')
    horario_partida = forms.SplitDateTimeField(
        widget=forms.SplitDateTimeWidget(
            date_attrs={'type': 'date'},
            time_attrs={'type': 'time'},
        ),
        label='Horário Partida',
        help_text='Data e hora que o transporte ficará disponível para agência'
    )
    horario_chegada = forms.SplitDateTimeField(
        widget=forms.SplitDateTimeWidget(
            date_attrs={'type': 'date'},
            time_attrs={'type': 'time'},
        ),
        label='Horário Chegada',
        help_text='Data e hora que o transporte deverá ser devolvido'
    )
    selecionado = forms.BooleanField(label='Selecionado', required=False)
    observacao = forms.CharField()

    class Meta:
        model = Orcamento
        fields = [
            'excursao',
            'tipo_prestador_servico', 
            'prestador_servico',
            'cotacao',
            'horario_partida',
            'horario_chegada',
            'selecionado',
            'observacao'
        ]

class RoteiroForm(forms.ModelForm):
    excursao = forms.ModelChoiceField(queryset=Excursao.objects.all(), label = 'Excursão')
    horario_inicio = forms.SplitDateTimeField(
        widget=forms.SplitDateTimeWidget(
            date_attrs={'type': 'date'},
            time_attrs={'type': 'time'},
        ),
        label='Horário Início',
        help_text='Horário de início da atividade'
    )
    horario_fim = forms.SplitDateTimeField(
        widget=forms.SplitDateTimeWidget(
            date_attrs={'type': 'date'},
            time_attrs={'type': 'time'},
        ),
        label='Horário Fim',
        help_text='Horário do fim da atividade'
    )
    pago = forms.BooleanField(label='Pago', required=False)
    incluso = forms.BooleanField(label='Incluso', required=False)
    custo = forms.IntegerField(label='Custo')
    observacao = forms.CharField()

    class Meta: 
        model = Roteiro
        fields = [
            'excursao',
            'horario_inicio',
            'horario_fim',
            'pago',
            'incluso',
            'custo',
            'observacao'
        ]