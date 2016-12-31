from django.core.urlresolvers import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import generic
from django.shortcuts import get_object_or_404
from . import models


class CharacterDetailView(LoginRequiredMixin, generic.DetailView):
    model = models.Character

    def get_object(self, queryset=None):
        return get_object_or_404(self.model, name__iexact=self.kwargs['name'], realm__iexact=self.kwargs['realm'])


class CharacterCreateView(LoginRequiredMixin, generic.CreateView):
    model = models.Character
    fields = ['name', 'realm']
    success_url = reverse_lazy('accounts:profile')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(CharacterCreateView, self).form_valid(form)
