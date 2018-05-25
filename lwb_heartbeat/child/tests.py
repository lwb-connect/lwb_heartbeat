"""Test."""
from django.test import TestCase, Client
from .models import Child
import factory
from django.contrib.auth import get_user_model
import faker
from django.contrib.auth.models import User
from model_mommy import mommy
import tempfile
from django.urls import reverse_lazy
from .forms import ChildAddForm, ChildEditForm


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

    @classmethod
    def tearDownClass(cls):
        """Cleans up class by removing all attributes off user."""
        super(TestCase, cls)
        User.objects.all().delete()


# class ProfileUnitTests(TestCase):
#     """Profile tests."""

#     def test_user_can_see_its_profile(self):
#         """Test user profile view."""
#         user = User(
#             username='AlfredMolina',
#             email='AlfredMolina@AlfredMolina.com'
#         )
#         user.set_password('potatoe')
#         user.save()
#         self.user = user
#         image = PhotoFactory.build()
#         image.user = self.user
#         image.save()
#         self.image = image


# # class ImageTests(TestCase):
# #     """Testing Routes."""

# #     @classmethod
# #     def setUpClass(cls):
# #         """Define class."""
# #         super().setUpClass()

# #         for n in range(10):
# #             user = mommy.make(User)
# #             user.set_password('password')
# #             user.save()
# #             album = mommy.make(Album, user=user)
# #             photo = mommy.make(
# #                 Photo,
# #                 image=tempfile.NamedTemporaryFile(suffix='.jpg').name)
# #             album.photos.add(photo)

#     @classmethod
#     def tearDownClass(cls):
#         """Tear Down Class."""
#         User.objects.all().delete()
#         super().tearDownClass()


fake = faker.Faker()


class ChildFactory(factory.django.DjangoModelFactory):
    """Make child factory."""

    class Meta:
        """Class for Meta."""

        model = Child

    currently_in_lwb_care = factory.Faker('boolean')
    date_entered_lwb_care = factory.Faker('date')
    date_child_left_lwb_care = factory.Faker('date')
    program_number = factory.Faker('random_digit')
    nick_name = factory.Faker('name')
    given_name_sur = factory.Faker('name')
    given_name_first = factory.Faker('name')
    DOB = factory.Faker('date')
    # date_modified = factory.Faker('date')
    # location_country = factory.Faker('country')
    # education_program = factory.Faker('name')


class ChildProfileTests(TestCase):
    """Test child profiles."""
    @classmethod
    def setUpClass(cls):
        """Create 20 instances of child for testing purposes."""
        super(TestCase, cls)
        for _ in range(1):
            kid = ChildFactory.create()
            # kid.set_password(factory.Faker('password'))
            kid.save()

            # Probs don't need.....
            # user.profile.save()

    @classmethod
    def tearDownClass(cls):
        """Cleans up class by removing all attributes off child."""
        super(TestCase, cls)
        Child.objects.all().delete()

    def test_nick_name_on_child_exists(self):
        """Tests if child profile has a name."""
        test_child = Child.objects.first()
        self.assertIsNotNone(test_child.nick_name)

    def test_currently_in_lwb_care_exists(self):
        """Tests if child profile has in care property."""
        test_child = Child.objects.first()
        self.assertIsNotNone(test_child.currently_in_lwb_care)

    def test_DOB_exists(self):
        """Tests if child profile has a DOB."""
        test_child = Child.objects.first()
        self.assertIsNotNone(test_child.DOB)

    def test_given_name_sur_exists(self):
        """Tests if child profile has a surname"""
        test_child = Child.objects.first()
        self.assertIsNotNone(test_child.given_name_sur)

    # def test_child_profile_edit_form(self):
    #     """Test the profile edit form for a child."""

    #     test_user = User.objects.first()
    #     test_child = Child.objects.first()

    #     # fields = ['currently_in_lwb_care', 'date_entered_lwb_care',
    #     #           'date_child_left_lwb_care', 'program_number',
    #     #           'nick_name', 'given_name_sur', 'given_name_first', 'DOB',
    #     #           'location_country', 'education_program',
    #     #           'image', 'description']

    #     form = ChildEditForm(
    #         {'currently_in_lwb_care': test_child.currently_in_lwb_care,
    #             'date_entered_lwb_care': test_child.date_entered_lwb_care,
    #             'date_child_left_lwb_care': test_child.date_child_left_lwb_care,
    #             'program_number': test_child.program_number,
    #             'nick_name': test_child.nick_name,
    #             'given_name_sur': test_child.given_name_sur,
    #             'given_name_first': test_child.given_name_first,
    #             'DOB': test_child.DOB,},
    #             # username=test_user.username
    #             )

    #     # self.assertTrue(form['first_name'].data == 'Jay')
    #     # self.assertTrue(form['last_name'].data == 'Adams')
    #     self.assertTrue(form['currently_in_lwb_care'].data == test_child.currently_in_lwb_care)
    #     self.assertTrue(form['date_entered_lwb_care'].data == test_child.date_entered_lwb_care)
    #     self.assertTrue(form['date_child_left_lwb_care'].data == test_child.date_child_left_lwb_care)
    #     self.assertTrue(form['program_number'].data == test_child.program_number)
    #     self.assertTrue(form['nick_name'].data == test_child.nick_name)
    #     self.assertTrue(form['given_name_sur'].data == test_child.given_name_sur)
    #     self.assertTrue(form['given_name_first'].data == test_child.given_name_first)
    #     self.assertTrue(form['DOB'].data == test_child.DOB)
        # self.assertTrue(form['date_modified'].data == test_child.date_modified)


class TestChildViews(TestCase):
    """Test child related views work."""
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

    def test_200_status_on_authenticated_request_to_childlist(self):
        """Check that an authenticated request to childlist returns 200 status."""
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('childlist'))
        self.client.logout()
        self.assertEqual(response.status_code, 200)

    def test_200_status_on_authenticated_request_to_child_create(self):
        """Check that an authenticated request to child create returns 200 status."""
        self.client.force_login(self.user)
        response = self.client.get(reverse_lazy('child_create'))
        self.client.logout()
        self.assertEqual(response.status_code, 200)


    def test_404_status_on_authenticated_request_to_child_detail(self):
        """Check that an authenticated request to child detail returns 404 status."""
        self.client.force_login(self.user)

        response = self.client.get('/child/1', follow=True)
        # response = self.client.get(reverse_lazy('/staff/settings/' + self.user.username))
        self.assertEqual(response.status_code, 404)
        self.client.logout()

    # def test_200_status_on_authenticated_request_to_child_detail(self):
    #     """Check that an authenticated request to child detail returns 200 status."""
    #     self.client.force_login(self.user)

    #     response = self.client.get('/child/child/1', follow=True)
    #     # response = self.client.get(reverse_lazy('/staff/settings/' + self.user.username))
    #     self.assertEqual(response.status_code, 200)
    #     self.client.logout()

    # def test_200_status_on_authenticated_request_to_store(self):
    #     """Test 200 status."""
    #     user = User.objects.first()
    #     # self.client.login(username=user.username, password='password')
    #     self.client.force_login(user)
    #     response = self.client.get(reverse_lazy("albums"))
    #     self.client.logout()
    #     self.assertEqual(response.status_code, 200)

    # def test_200_status_on_authenticated_request_to_product(self):
    #     """Test authenticated 200 status."""
    #     user = User.objects.first()
    #     album = Album.objects.first()
    #     self.client.force_login(user)
    #     response = self.client.get(reverse_lazy('album', args=[album.id]))
    #     self.client.logout()
    #     self.assertEqual(response.status_code, 200)

#     def test_302_status_on_unauthenticated_request_to_product(self):
#         """Test 302 on unathenticated."""
#         album = Album.objects.first()
#         response = self.client.get(reverse_lazy('album', args=[album.id]))
#         self.assertEqual(response.status_code, 302)

#     def test_404_status_on_bad_request_to_product(self):
#         """Test 404 status on bad request."""
#         response = self.client.get('/store/products/does_not_exist')
#         self.assertEqual(response.status_code, 404)

#     def test_302_status_on_unauthenticated_request_to_store(self):
#         """Test 302 on not athenticated request to store."""
#         response = self.client.get(reverse_lazy("albums"))
#         self.assertEqual(response.status_code, 302)

#     def test_only_public_childs_are_shown(self):
#         """Test that only public products shown."""
#         user = User.objects.first()
#         child = Child.objects.first()
#         child.published = 'PUBLIC'
#         child.save()

#         self.client.force_login(user)
#         response = self.client.get(reverse_lazy("childs"))
#         self.client.logout()

#         childs = response.context['childs']
#         for child in childs:
#             self.assertEqual(child.published, 'PUBLIC')

# #     def test_user_can_see_photo_one(self):
# #         """Test id user can see other user view."""
# #         users = list(User.objects.all())
# #         self.client.force_login(users[0])
# #         response = self.client.get(reverse_lazy('photo', args=[Photo.objects.first().id]))
# #         self.assertEqual(response.status_code, 200)

# #     def test_user_photo_view_uses_base_template(self):
# #         """Test id user can see other user view."""
# #         users = list(User.objects.all())
# #         self.client.force_login(users[0])
# #         response = self.client.get(reverse_lazy('photo', args=[Photo.objects.first().id]))
# #         self.assertTemplateUsed(response, 'generic/base.html')

# #     def test_user_must_be_logged_in_to_see_photo(self):
# #         """Test id user can see other user view."""
# #         users = list(User.objects.all())
# #         response = self.client.get(reverse_lazy('photo', args=[Photo.objects.first().id]))
# #         self.assertEqual(response.status_code, 302)

# #     def test_user_can_see_photos(self):
# #         """Test id user can see other user view."""
# #         users = list(User.objects.all())
# #         self.client.force_login(users[0])
# #         response = self.client.get(reverse_lazy('photos'))
# #         self.assertEqual(response.status_code, 200)

# #     def test_user_photos_view_uses_base_template(self):
# #         """Test id user can see other user view."""
# #         users = list(User.objects.all())
# #         self.client.force_login(users[0])
# #         response = self.client.get(reverse_lazy('photos'))
# #         self.assertTemplateUsed(response, 'generic/base.html')

# #     def test_user_must_be_logged_in_to_see_photos(self):
# #         """Test id user can see other user view."""
# #         users = list(User.objects.all())
# #         response = self.client.get(reverse_lazy('photos'))
# #         self.assertEqual(response.status_code, 302)

# #     def test_user_can_see_library(self):
# #         """Test id user can see other user view."""
# #         users = list(User.objects.all())
# #         self.client.force_login(users[0])
# #         response = self.client.get(reverse_lazy('library'))
# #         self.assertEqual(response.status_code, 200)

# #     def test_user_library_view_uses_base_template(self):
# #         """Test id user can see other user view."""
# #         users = list(User.objects.all())
# #         self.client.force_login(users[0])
# #         response = self.client.get(reverse_lazy('library'))
# #         self.assertTemplateUsed(response, 'generic/base.html')

# #     def test_user_must_be_logged_in_to_see_library(self):
# #         """Test id user can see other user view."""
# #         users = list(User.objects.all())
# #         response = self.client.get(reverse_lazy('library'))
# #         self.assertEqual(response.status_code, 302)

# #     def test_user_can_see_album_one(self):
# #         """Test id user can see other user view."""
# #         users = list(User.objects.all())
# #         self.client.force_login(users[0])
# #         response = self.client.get(reverse_lazy('album', args=[Album.objects.first().id]))
# #         self.assertEqual(response.status_code, 200)

# #     def test_user_album_view_uses_base_template(self):
# #         """Test id user can see other user view."""
# #         users = list(User.objects.all())
# #         self.client.force_login(users[0])
# #         response = self.client.get(reverse_lazy('album', args=[Album.objects.first().id]))
# #         self.assertTemplateUsed(response, 'generic/base.html')

# #     def test_user_must_be_logged_in_to_see_album(self):
# #         """Test id user can see other user view."""
# #         users = list(User.objects.all())
# #         response = self.client.get(reverse_lazy('album', args=[Album.objects.first().id]))
# #         self.assertEqual(response.status_code, 302)

# #     def test_user_can_see_albums(self):
# #         """Test id user can see other user view."""
# #         users = list(User.objects.all())
# #         self.client.force_login(users[0])
# #         response = self.client.get(reverse_lazy('albums'))
# #         self.assertEqual(response.status_code, 200)

# #     def test_user_albums_view_uses_base_template(self):
# #         """Test id user can see other user view."""
# #         users = list(User.objects.all())
# #         self.client.force_login(users[0])
# #         response = self.client.get(reverse_lazy('albums'))
# #         self.assertTemplateUsed(response, 'generic/base.html')

# #     def test_user_must_be_logged_in_to_see_albums(self):
# #         """Test id user can see other user view."""
# #         users = list(User.objects.all())
# #         response = self.client.get(reverse_lazy('albums'))
# #         self.assertEqual(response.status_code, 302)


# # class ImageFormTests(ImageTests):
# #     """Image form tests class."""

# #     def test_init_album(self):
# #         """Test image form."""
# #         user = list(User.objects.all())[0]
# #         AlbumForm(username=user.username)

# #     def test_init_photo(self):
# #         """Test image form."""
# #         user = list(User.objects.all())[0]
# #         PhotoForm(username=user.username)

# #     def test_invalid_data_album(self):
# #         """Test image form."""
# #         user = list(User.objects.all())[0]
# #         form = AlbumForm({}, username=user.username)
# #         self.assertFalse(form.is_valid())

# #     def test_invalid_data_photo(self):
# #         """Test image form."""
# #         user = list(User.objects.all())[0]
# #         form = PhotoForm({}, username=user.username)
# #         self.assertFalse(form.is_valid())
