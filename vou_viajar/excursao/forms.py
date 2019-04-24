from django import forms

from .models import Excursao

class ExcursaoForm(forms.ModelForm):
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

