from django.urls import path

from . import views

urlpatterns = [
    path('menu', views.menu_excursao, name='menu'),
    path('adicionar', views.adicionar_excursao, name='adicionar'),
    path('listar', views.listar_excursao, name='listar'),
    path('atualizar/<pk>', views.atualizar_excursao, name='atualizar'),
    path('deletar/<pk>', views.deletar_excursao, name='deletar'),
]

