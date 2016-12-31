from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^new/', views.CharacterCreateView.as_view(), name='create'),
    url(r'(?P<realm>[\w\-]+)/(?P<name>[\w\-]+)', views.CharacterDetailView.as_view(), name='detail'),
]
