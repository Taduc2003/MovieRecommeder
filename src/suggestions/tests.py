from django.test import TestCase

from django.test import TestCase, Client, tag
from django.contrib.auth import get_user_model
from movies.models import Movie
from suggestions.models import Suggestion

class SuggestionApiIntegrationTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(username='testuser', password='testpass')
        cls.movie = Movie.objects.create(id=1, title="Movie 1")
        Suggestion.objects.create(user=cls.user, object_id=cls.movie.id, value=4.5, content_type_id=1)

    @tag('integration')
    def test_top_n_recommendation(self):
        self.client.login(username='testuser', password='testpass')
        response = self.client.get('/api/suggestions/')
        self.assertEqual(response.status_code, 200)
        self.assertTrue(len(response.json().get('suggestions', [])) > 0)

    # @tag('integration')
    # def test_cold_start(self):
    #     new_user = get_user_model().objects.create_user(username='cold', password='cold')
    #     self.client.login(username='cold', password='cold')
    #     response = self.client.get('/api/suggestions/')
    #     self.assertEqual(response.status_code, 200)
    #     # Không được crash, có thể trả về danh sách phổ biến hoặc rỗng
