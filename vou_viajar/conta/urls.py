from django.urls import path

from . import views

urlpatterns = [
    path(
        'cadastrar_agencia',
        views.adicionar_agencia,
        name='adicionar_agencia',
    ),
    path('login/', views.login, name='login'),
    # path('logout/', views.logout_view, name='logout'),
]
