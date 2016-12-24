from django.views import generic


class CharacterDetailView(generic.TemplateView):
    template_name = 'characters/character_detail.html'
