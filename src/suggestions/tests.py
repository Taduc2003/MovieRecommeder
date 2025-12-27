from django.test import TestCase

from django.test import TestCase, Client, tag
from django.contrib.auth import get_user_model
from movies.models import Movie
from suggestions.models import Suggestion

class SuggestionApiIntegrationTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username='testuser', password='testpass')
        cls.movie = Movie.objects.create(id=1, title="Movie 1", overview="Test movie")
        Suggestion.objects.create(user=cls.user, object_id=cls.movie.id, value=4.5, content_type_id=1)

    def test_api_suggestions(self):
        url = '/api/suggestions/?user_id={}'.format(self.user.id)
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        data = response.json()
        self.assertIn('suggestions', data)
        self.assertTrue(any(m['id'] == self.movie.id for m in data['suggestions']))

    def test_api_suggestions_user_not_found(self):
        url = '/api/suggestions/?user_id=99999'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 404)
        self.assertIn('error', response.json())

    def test_api_suggestions_missing_user_id(self):
        url = '/api/suggestions/'
        response = self.client.get(url)
        self.assertEqual(response.status_code, 400)
        self.assertIn('error', response.json())
