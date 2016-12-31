from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import Http404
from django.views import generic
from django.shortcuts import get_object_or_404
from . import models
import requests


class CharacterDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Character

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, name__iexact=self.kwargs['name'], realm__iexact=self.kwargs['realm'])


class CharacterCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.Character
    fields = ['name', 'realm']
    success_url = reverse_lazy('accounts:profile')

    def form_valid(self, form):
        request = requests.get(
            'https://us.api.battle.net/wow/character/%s/%s?locale=en_US&fields=items&apikey=%s' % (
                form.instance.realm, form.instance.name, 'x95frpjm3v3zdrnj3rbzr83e9b348hj9'
            ))

        if request.status_code != 200:
            raise Http404

        form.instance.user = self.request.user
        return super(CharacterCreateView, self).form_valid(form)
