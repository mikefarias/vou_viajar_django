from django.urls import path

from . import views

urlpatterns = [
    path('menu', views.menu_excursao, name='menu'),
    path('adicionar', views.adicionar_excursao, name='adicionar_excursao'),
    path('listar', views.listar_excursao, name='listar_excursao'),
    path('atualizar/<pk>', views.atualizar_excursao, name='atualizar_excursao'),
    path('deletar/<pk>', views.deletar_excursao, name='deletar_excursao'),
    path('destino/adicionar', views.adicionar_destino, name='adicionar_destino'),
    path('destino/listar', views.listar_destino, name='listar_destino'),
    path('destino/atualizar/<pk>', views.atualizar_destino, name='atualizar_destino'),
    path('destino/deletar/<pk>', views.deletar_destino, name='deletar_destino'),
    path('orcamento/adicionar', views.adicionar_orcamento, name='adicionar_orcamento'),
    path('orcamento/listar', views.listar_orcamento, name='listar_orcamento'),
    path('orcamento/atualizar/<pk>', views.atualizar_orcamento, name='atualizar_orcamento'),
    path('orcamento/deletar/<pk>', views.deletar_orcamento, name='deletar_orcamento'),
]

