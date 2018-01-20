from django.core.urlresolvers import resolve
from django.test import TestCase
from django.http import HttpRequest
from ttt.views import index

class HomePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, index)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = index(request)
        html = response.content.decode('utf8')
        self.assertIn('<title> ML-TTT </title>', html)
        self.assertIn('<nav>', html)
