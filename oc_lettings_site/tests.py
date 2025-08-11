from django.test import TestCase, Client
from django.urls import reverse


class MainViewsTest(TestCase):
    def setUp(self):
        """Set up test data."""
        self.client = Client()

    def test_home_view(self):
        """Test the home page view."""
        url = reverse('index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

    def test_home_view_content(self):
        """Test the home page content."""
        url = reverse('index')
        response = self.client.get(url)
        self.assertContains(response, 'Profiles')
        self.assertContains(response, 'Lettings')

    def test_home_view_links(self):
        """Test that the home page has working links."""
        url = reverse('index')
        response = self.client.get(url)
        
        # Check profiles link
        profiles_url = reverse('profiles:index')
        self.assertContains(response, f'href="{profiles_url}"')
        
        # Check lettings link
        lettings_url = reverse('lettings:index')
        self.assertContains(response, f'href="{lettings_url}"')
