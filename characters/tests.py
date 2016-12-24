from django.test import RequestFactory, TestCase, Client
from django.core.urlresolvers import reverse_lazy


class TestCharacterPage(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.client = Client()

    def test_character_detail_view(self):
        response = self.client.get(reverse_lazy('characters:detail', kwargs={'realm': 'thrall', 'name': 'beamsteels'}))
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Beamsteels', response.content)
