from django.urls import path

from . import views

urlpatterns = [
    path('menu', views.menu_excursao, name='menu'),
    path('adicionar', views.adicionar_excursao, name='adicionar'),
    path('listar', views.listar_excursao, name='listar'),
    path('atualizar/<pk>', views.atualizar_excursao, name='atualizar'),
    path('deletar/<pk>', views.deletar_excursao, name='deletar'),
    path('destino/adicionar', views.adicionar_destino, name='adicionar_destino'),
    path('destino/listar', views.listar_destino, name='listar_destino'),
    path('destino/atualizar/<pk>', views.atualizar_destino, name='atualizar_destino'),
    path('destino/deletar/<pk>', views.deletar_destino, name='deletar_destino'),
]

