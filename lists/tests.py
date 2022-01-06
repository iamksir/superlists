from django.test import TestCase
#django2.X把django.core.urlresolvers包更改为了django.urls包
from django.urls import resolve
from lists.views import home_page
# Create your tests here.

class HOmePageTest(TestCase):

    def test_root_url_resolves_to_home_page_view(self):
        found = resolve('/')
        self.assertEqual(found.func, home_page)