"""Tests."""
from django.test import TestCase
from django.urls import reverse_lazy
from django.core import mail
from urllib.parse import urlparse


class ProfileUnitTests(TestCase):
    """Test for Unit Profile."""

    def test_get_home_page(self):
        """Test home page."""
        response = self.client.get(reverse_lazy('home'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.templates[0].name, 'generic/home.html')
        self.assertEqual(response.templates[1].name, 'generic/base.html')

    def test_about_us_page(self):
        """Test home page."""
        response = self.client.get(reverse_lazy('about'), follow=True)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.templates[0].name, 'generic/about_us.html')
        self.assertEqual(response.templates[1].name, 'generic/base.html')
