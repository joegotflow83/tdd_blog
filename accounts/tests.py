from django.test import TestCase
from django.core.urlresolvers import reverse


class AccountsTest(TestCase):
    def test_signup_page_displays_200(self):
        url = reverse("signup")
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_login_page_displays_200(self):
        url = reverse('login')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 200)

    def test_logout_page_redirects_to_login(self):
        url = reverse('logout')
        resp = self.client.get(url)
        self.assertEqual(resp.status_code, 302)
