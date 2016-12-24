from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.views import generic
from . import models
import requests


class CharacterDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Character

    def get_object(self, queryset=None):
        try:
            return self.model.objects.get(name__iexact=self.kwargs['name'], realm__iexact=self.kwargs['realm'])
        except self.model.DoesNotExist:
            request = requests.get(
                'https://us.api.battle.net/wow/character/%s/%s?locale=en_US&fields=items&apikey=%s' % (
                    self.kwargs['realm'], self.kwargs['name'], 'x95frpjm3v3zdrnj3rbzr83e9b348hj9'
                ))

            if request.status_code != 200:
                raise Http404

            json = request.json()
            character = self.model.objects.create(
                name=self.kwargs['name'],
                realm=self.kwargs['realm']
            )
            models.Snapshot.objects.create(character=character, item_level=json['items']['averageItemLevel'])

            return character
