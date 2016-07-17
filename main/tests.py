from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from .models import Post


# Models Test
class MainTest(TestCase):
    """Test models in main app"""
    def test_post_models(self):
        user = User.objects.create(username="joe")
        post = Post.objects.create(user=user, title="TDD", body="I am practicing tdd")
        self.assertTrue(isinstance(post, Post))

    def test_home_page_is_displayed_200(self):
        url = reverse('home')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
