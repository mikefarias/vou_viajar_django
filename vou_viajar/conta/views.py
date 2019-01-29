from django.shortcuts import render

from .forms import AgenciaForm
from .models import Agencia

# Create your views here.

def login(request):
    return render(request, 'conta/login.html')

def adicionar_agencia(request):
    form = None
    if request.method == 'POST':
        agencia = Agencia()
        form = AgenciaForm(request.POST, instance=agencia)
        if form.is_valid():
            form.save()
            messages.success(request, 'Agência cadastrada com sucesso!')
            return redirect('index')
    else:
        form = AgenciaForm()
    return render(
        request,
        'conta/adicionar_agencia.html',
        {'form': form},
    )
