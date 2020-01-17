from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_agencia', views.adicionar_agencia, name='adicionar_agencia'),
    path('cadastrar_usuario', views.cadastrar_usuario, name='cadastrar_usuario'),
    path('login', views.login_view, name='login_view'),
    path('logout', views.logout_view, name='logout_view'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'), 
]
