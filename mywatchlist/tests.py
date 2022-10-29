from django.test import TestCase
from django.urls import reverse
from mywatchlist.models import MyWatchList


# Create your tests here.
class mywatchlist_test(TestCase):
    def test_mywatchlist_html(self) :
        response = self.client.get(reverse('mywatchlist:html'))
        self.assertEqual(response.status_code, 200)
    def test_mywatchlist_xml(self) :
        response = self.client.get(reverse('mywatchlist:xml'))
        self.assertEqual(response.status_code, 200)
    def test_mywatchlist_json(self) :
        response = self.client.get(reverse('mywatchlist:json'))
        self.assertEqual(response.status_code, 200)

