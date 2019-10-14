from django.urls import path
from . import views

urlpatterns = [
    path('cadastrar_agencia', views.adicionar_agencia, name='adicionar_agencia'),
    path('logout', views.logout_view, name='logout_view'),
    path('register', views.SignUp.as_view(), name='signup'),
    path('menu', views.menu, name='conta_menu'),

]
