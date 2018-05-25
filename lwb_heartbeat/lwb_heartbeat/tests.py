"""Imports."""
from django.test import TestCase, Client
from django.contrib.auth.models import User
# from .forms import ProfileEditForm
from django.urls import reverse_lazy
import factory
from random import choice



# class ProfileUnitTest(TestCase):
#     """
#     Use generated user and profile info to test code
#     related to staff.

#     Such as views and forms and profile.
#     """

#     @classmethod
#     def setUpClass(cls):
#         """Create 20 instances of user for testing purposes."""
#         super(TestCase, cls)
#         for _ in range(20):
#             user = UserFactory.create()
#             user.set_password(factory.Faker('password'))
#             user.save()


class TestStaffViews(TestCase):
    """Test views related to staff (Profile, ProfileEdit, and StaffList)."""

    @classmethod
    def setUp(self):
        """Set up."""
        user = User(username='Keith',
                    email='no@no.com')
        user.save()
        self.user = user
        self.client = Client()

    @classmethod
    def tearDown(self):
        """Tear down."""
        """Deletes users made for testing purposes."""
        User.objects.all().delete()
        super(TestCase, self)

    def test_200_status_on_authenticated_request_to_profile(self):
        """Check that an authenticated request returns 200 status."""
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('home'))
        self.client.logout()
        self.assertEqual(response.status_code, 200)

    def test_200_status_on_authenticated_request_to_about_us(self):
        """Check that an authenticated request returns 200 status."""
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('about'))
        self.client.logout()
        self.assertEqual(response.status_code, 200)
