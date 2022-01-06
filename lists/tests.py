from django.test import TestCase
#django2.X把django.core.urlresolvers包更改为了django.urls包
from django.urls import resolve
from lists.views import home_page
from django.http import HttpRequest
# Create your tests here.

class HOmePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)

    def test_home_page_returns_correct_html(self):
        request = HttpRequest()
        response = home_page(request)
        self.assertTrue(response.content.startswith(b'<html>'))
        self.assertIn(b'<title>worked</title>', response.content)
        self.assertTrue(response.content.endswith(b'</html>'))