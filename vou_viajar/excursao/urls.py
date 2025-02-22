from django.urls import path

from . import views

urlpatterns = [
    path('home', views.home, name='home'),
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
    path('prestadorservico/adicionar', views.adicionar_prestador_servico, name='adicionar_prestador_servico'),
    path('prestadorservico/listar', views.listar_prestador_servico, name='listar_prestador_servico'),
    path('prestadorservico/listar/<pk>', views.get_service_provider_type, name='listar_prestador_servico_tipo'),
    path('prestadorservico/atualizar/<pk>', views.atualizar_prestador_servico, name='atualizar_prestador_servico'),
    path('prestadorservico/deletar/<pk>', views.deletar_prestador_servico, name='deletar_prestador_servico'),
    path('transporte/adicionar', views.adicionar_transporte, name='adicionar_transporte'),
    path('transporte/listar', views.listar_transporte, name='listar_transporte'),
    path('transporte/atualizar/<pk>', views.atualizar_transporte, name='atualizar_transporte'),
    path('transporte/deletar/<pk>', views.deletar_transporte, name='deletar_transporte'),
    path('roteiro/adicionar', views.adicionar_roteiro, name='adicionar_roteiro'),
    path('roteiro/listar', views.listar_roteiro, name='listar_roteiro'),
    path('roteiro/atualizar/<pk>', views.atualizar_roteiro, name='atualizar_roteiro'),
    path('roteiro/deletar/<pk>', views.deletar_roteiro, name='deletar_roteiro'),
]