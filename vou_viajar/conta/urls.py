from django.urls import path
from . import views

urlpatterns = [
    path('add_agency', views.add_agency, name='add_agency'),
    path('update_agency/<pk>', views.update_agency, name='update_agency'),
    path('add_user', views.add_user, name='add_user'),
    path('add_profile', views.add_profile, name='add_profile'),
    path('login', views.login_view, name='login_view'),
    path('logout', views.logout_view, name='logout_view'),
    path('activate/<uidb64>/<token>/', views.activate, name='activate'), 
]
