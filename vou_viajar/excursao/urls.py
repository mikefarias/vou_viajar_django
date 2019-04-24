from django.urls import path

from . import views

urlpatterns = [
    path(
        'cadastrar_excursao',
        views.adicionar_excursao,
        name='adicionar_excursao',
    ),
]
