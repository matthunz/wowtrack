from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    url(r'^login/', auth_views.login, name='login'),
    url(r'^logout/', views.Logout.as_view(), name='logout'),
    url(r'profile/', views.ProfileView.as_view(), name='profile')
]
