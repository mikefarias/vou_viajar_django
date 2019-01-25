from django.contrib import admin
from django.urls import path
from django.conf.urls import include

from . import views as web_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/agencia', web_views.adicionar_agencia, name='adicionar_agencia'),
    path('post/excursao', web_views.adicionar_excursao, name='adicionar_excursao'),
    path('base/', web_views.base, name='base'),
    path('index/', web_views.index, name='index'),
    path('login/', web_views.login, name='login'),
    # path('logout/', web_views.logout_view, name='logout'),
    path('oauth/', include('social_django.urls', namespace='social')),
    # path('settings/', web_views.settings, name='settings'),

]
