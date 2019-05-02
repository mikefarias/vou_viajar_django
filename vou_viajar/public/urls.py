from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('login', views.login, name='login'),
    path('logout', views.logout, name='logout'),
    path('destinos', views.destinos, name='destinos'),
    path('blog', views.blog, name='blog'),
]
