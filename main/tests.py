from django.test import TestCase
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

from .models import Post


# Models Test
class MainTest(TestCase):
    """Test models in main app"""
    def test_post_models(self):
        user = User(username="joe")
        post = Post(user=user, title="TDD", body="I am practicing tdd")
        self.assertTrue(isinstance(post, Post))

    def test_home_page_is_displayed_200(self):
        url = reverse('home')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_create_post_page_is_displayed_200(self):
        url = reverse('create_post')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    """def test_post_object_is_created(self):
        url = reverse('create_post')
        superuser = User.objects.create_superuser("joe", "joe@doe.com", "joepassword")
        self.client.login(username="joe", password="joepassword")
        post_object = self.client.post(url, {'user': superuser, 'title': 'TDD', 'body': 'I am practicing TDD'})
        self.assertTrue(isinstance(post_object, Post))"""

    def test_post_page_displays_posts_200(self):
        url = reverse('list_posts')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_posts_are_actually_on_the_page(self):
        Post(title="TDD", body="TDD is fun")
        url = reverse('list_posts')
        resp = self.client.get(url)
        self.assertContains(resp, 'TDD')

    def test_user_can_view_a_post(self):
        user = User.objects.create(username="joe")
        post = Post.objects.create(user=user, title="TDD", body="TDD is fun")
        url = reverse('single_post', kwargs={'pk': post.pk})
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)
