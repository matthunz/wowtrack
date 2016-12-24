from django.contrib.auth import logout
from django.core.urlresolvers import reverse_lazy
from django.views import generic


class Logout(generic.RedirectView):
    url = reverse_lazy('home')

    def get(self, request, *args, **kwargs):
        logout(request)
        return super().get(request, *args, **kwargs)
