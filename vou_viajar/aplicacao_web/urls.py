from django.contrib import admin
from django.urls import path
from aplicacao_web import views as web_views
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('post/agency', web_views.add_agency, name='add_agency'),
    path('base/', web_views.base, name='base'),
    path('index/', web_views.index, name='index'),
    path('login/', web_views.login, name='login'),
    # path('logout/', web_views.logout_view, name='logout'),
    path('oauth/', include('social_django.urls', namespace='social')),
    # path('settings/', web_views.settings, name='settings'),

]