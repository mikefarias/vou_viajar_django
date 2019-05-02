from django.urls import path

from . import views

urlpatterns = [
    path('adicionar_excursao', views.adicionar_excursao, name='adicionar_excursao'),
]
