from django import forms

from core.models import Evento


class EventoForm(forms.ModelForm):
    inicio_evento = forms.SplitDateTimeField(
        widget=forms.SplitDateTimeWidget(date_attrs={'type': 'date'}, time_attrs={'type': 'time'}))
    fim_evento = forms.SplitDateTimeField(
        widget=forms.SplitDateTimeWidget(date_attrs={'type': 'date'}, time_attrs={'type': 'time'}))

    class Meta:
        model = Evento
        fields = [
            'titulo',
            'descricao',
            'origem',
            'destino',
            'inicio_evento',
            'fim_evento'
        ]