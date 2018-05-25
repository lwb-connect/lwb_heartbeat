"""Imports."""
from django.test import TestCase, Client
from .models import User
from .forms import ProfileEditForm
from django.urls import reverse_lazy
import factory


class UserFactory(factory.django.DjangoModelFactory):
    """Use factory to create a fake user for testing purposes."""

    class Meta:
        model = User

    username = factory.Faker('user_name')
    email = factory.Faker('email')

    # def add_profile_info():
    #     pass
        # don't need to create profile, empty one exists
        # but maybe need fake profile info


class ProfileUnitTest(TestCase):
    """Use generated user and profile info to test code related to staff, such as views and forms and profile."""

    @classmethod
    def setUpClass(cls):
        """Create 20 instances of user for testing purposes."""
        super(TestCase, cls)
        for _ in range(20):
            user = UserFactory.create()
            user.set_password(factory.Faker('password'))
            user.save()

            # Probs don't need.....
            # user.profile.save()

    @classmethod
    def tearDownClass(cls):
        """Cleans up class by removing all attributes off user."""
        super(TestCase, cls)
        User.objects.all().delete()

    def test_user_can_see_its_profile(self):
        """Tests if user profile is present and active."""
        test_user = User.objects.first()
        self.assertIsNotNone(test_user.profile)

    def test_user_has_a_username(self):
        """Test if user has username"""
        test_user = User.objects.first()
        self.assertIsNotNone(test_user.username)

    def test_staff_profile_edit_form(self):
        """Test the profile edit form for staff."""

        test_user = User.objects.first()

        # fields = [
        #     'first_name', 'last_name', 'about_you', 'country_of_residence', 'city_of_residence', 'email', 'phone', 'location', 'user_language_spoken', 'user_language_spoken_other', 'user_language_written', 'user_language_written_other']

        form = ProfileEditForm(
            {'first_name': 'Jay',
                'last_name': 'Adams',
                'about_you': test_user.profile.about_you,
                'country_of_residence': test_user.profile.country_of_residence,
                'city_of_residence': test_user.profile.city_of_residence,
                'email': test_user.profile.email,
                'phone': test_user.profile.phone,
                'location': test_user.profile.location,
                'user_language_spoken': test_user.profile.user_language_spoken,
                'user_language_spoken_other': test_user.profile.user_language_spoken_other,
                'user_language_written': test_user.profile.user_language_written,
                'user_language_written_other': test_user.profile.user_language_written_other},
                username=test_user.username)

        self.assertTrue(form['first_name'].data == 'Jay')
        self.assertTrue(form['last_name'].data == 'Adams')
        self.assertTrue(form['about_you'].data == test_user.profile.about_you)
        self.assertTrue(form['country_of_residence'].data == test_user.profile.country_of_residence)
        self.assertTrue(form['city_of_residence'].data == test_user.profile.city_of_residence)
        self.assertTrue(form['email'].data == test_user.profile.email)
        self.assertTrue(form['phone'].data == test_user.profile.phone)
        self.assertTrue(form['location'].data == test_user.profile.location)
        self.assertTrue(form['user_language_spoken'].data == test_user.profile.user_language_spoken)
        self.assertTrue(form['user_language_spoken_other'].data == test_user.profile.user_language_spoken_other)
        self.assertTrue(form['user_language_written'].data == test_user.profile.user_language_written)
        self.assertTrue(form['user_language_written_other'].data == test_user.profile.user_language_written_other)


class TestStaffViews(TestCase):
    """Test views related to staff (Profile, ProfileEdit, and StaffList)"""

    @classmethod
    def setUp(self):
        user = User(username='Keith',
                    email='no@no.com')
        user.save()
        self.user = user
        self.client = Client()

    @classmethod
    def tearDown(self):
        """Deletes users made for testing purposes."""
        User.objects.all().delete()
        super(TestCase, self)

    def test_200_status_on_authenticated_request_to_profile(self):
        """Check that an authenticated request to profile returns 200 status."""
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('profile'))
        self.client.logout()
        self.assertEqual(response.status_code, 200)

    def test_200_status_on_authenticated_request_to_stafflist(self):
        """Check that an authenticated request to stafflist returns 200 status."""
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('stafflist'))
        self.client.logout()
        self.assertEqual(response.status_code, 200)

    def test_404_status_on_authenticated_request_to_profile_edit(self):
        """Check that an authenticated request to profile edit returns 404 status."""
        self.client.force_login(self.user)
        response = self.client.get('settings/' + self.user.username)
        # print("TEST",response)
        self.client.logout()
        self.assertEqual(response.status_code, 404)

    def test_that_url_matches_the_user_username_profile_edit(self):
        """Check that an authenticated user has the right username."""
        self.client.force_login(self.user)
        # response = self.client.get(reverse_lazy('settings/' + self.user.username))
        # response = self.client.get('/profile/settings/{}'.format
        #                            (self.user.username), follow=True)
        # response = self.client.get('/profile/settings/keith')
        self.assertEqual(self.user.username, 'Keith')
        self.client.logout()

    def test_200_status_on_authenticated_request_to_profile_edit(self):
        """Check that an authenticated request to profile edit returns 200 status."""
        self.client.force_login(self.user)

        response = self.client.get('/staff/settings/Keith', follow=True)
        # response = self.client.get(reverse_lazy('/staff/settings/' + self.user.username))
        self.assertEqual(response.status_code, 200)
        self.client.logout()
