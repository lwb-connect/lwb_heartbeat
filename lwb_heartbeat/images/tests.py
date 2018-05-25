"""Test."""
from django.test import TestCase
from .models import Photo
import factory
from django.contrib.auth import get_user_model
import faker
from django.contrib.auth.models import User
from model_mommy import mommy
import tempfile
from django.urls import reverse_lazy
from .forms import PhotoForm

fake = faker.Faker()


# class PhotoFactory(factory.django.DjangoModelFactory):
#     """Make photo factory."""

#     class Meta:
#         """Class for Meta."""

#         model = Photo

#     image = factory.Faker('image_url')
#     description = factory.Faker('word')
#     date_uploaded = factory.Faker('date')
#     date_modified = factory.Faker('date')
#     date_published = factory.Faker('date')
#     published = factory.Faker(
#         'random_element',
#         elements=[
#             ('PRIVATE', 'Private'),
#             ('SHARED', 'Shared'),
#             ('PUBLIC', 'Public'),
#          ]
#     )


# class ImageTests(TestCase):
#     """Testing Routes."""

#     @classmethod
#     def setUpClass(cls):
#         """Define class."""
#         super().setUpClass()

#     @classmethod
#     def tearDownClass(cls):
#         """Tear Down Class."""
#         User.objects.all().delete()
#         super().tearDownClass()


# class ImageViewTests(ImageTests):
#     """Image view class test."""

#     class ImageFormTests(ImageTests):
#         """Image form tests class."""

#     def test_init_photo(self):
#         """Test image form."""
#         user = list(User.objects.all())[0]
#         PhotoForm(username=user.username)
