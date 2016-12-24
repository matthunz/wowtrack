from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'(?P<realm>)/(?P<name>)', views.CharacterDetailView.as_view(), name='detail'),
]
