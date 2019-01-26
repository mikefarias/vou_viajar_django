from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from . import views as web_views

urlpatterns = [
    path('post/agencia', web_views.adicionar_agencia, name='adicionar_agencia'),
    path('post/excursao', web_views.adicionar_excursao, name='adicionar_excursao'),
    path('base/', web_views.base, name='base'),
    path('login/', web_views.login, name='login'),
    # path('logout/', web_views.logout_view, name='logout'),
    path('', web_views.index, name='index'),
]
