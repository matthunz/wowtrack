from django.test import RequestFactory, TestCase
from django.core.urlresolvers import reverse_lazy
from . import views


class TestCharacterPage(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_character_detail_view(self):
        request = self.factory.get(reverse_lazy('characters:detail', kwargs={'realm': '', 'name': ''}))
        response = views.CharacterDetailView.as_view()(request)
        self.assertEqual(response.status_code, 200)
