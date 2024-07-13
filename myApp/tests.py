from django.test import TestCase
from django.urls import reverse

class HomePageTests(TestCase):
    def test_home_page_status_code(self):
        response = self.client.get(reverse('home'))
        self.assertEqual(response.status_code, 200)

    def test_home_page_template(self):
        response = self.client.get(reverse('home'))
        self.assertTemplateUsed(response, 'myApp/home.html')

    # This test is designed to fail
    def test_failing_case(self):
        response = self.client.get(reverse('home'))
        # Intentionally fail the test by asserting an incorrect status code
        self.assertEqual(response.status_code, 404)
