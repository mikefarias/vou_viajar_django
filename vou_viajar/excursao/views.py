from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages

from .models import Excursao
from .forms import ExcursaoForm

def adicionar_excursao(request):
    form = None
    if request.method == 'POST':
        excursao = Excursao()
        form = ExcursaoForm(request.POST, instance=excursao)
        if form.is_valid():
            form.save()
            messages.success(request, 'Excursão cadastrada com sucesso!')
            return redirect('index')
    else:
        form = ExcursaoForm()
    return render(
        request,
        'excursao/adicionar_excursao.html',
        {'form': form},
    )

