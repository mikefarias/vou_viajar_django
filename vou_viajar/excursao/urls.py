from django.urls import path

from . import views

urlpatterns = [
    path('menu_excursao', views.menu_excursao, name='menu_excursao'),
    path('adicionar_excursao', views.adicionar_excursao, name='adicionar_excursao'),
    path('listar_excursao', views.listar_excursao, name='listar_excursao'),
]

