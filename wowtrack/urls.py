from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^accounts/', include('accounts.urls', namespace='accounts')),
    url(r'^characters/', include('characters.urls', namespace='characters')),
    url(r'', views.HomeView.as_view(), name='home'),
]
