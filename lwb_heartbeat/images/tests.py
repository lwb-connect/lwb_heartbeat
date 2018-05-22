from django.test import TestCase, Client, override_settings, RequestFactory
from django.core.files.uploadedfile import SimpleUploadedFile
from django.urls import reverse_lazy
from django.conf import settings
from .models import Photo
from .forms import PhotoForm, PhotoEditForm
from .views import PhotoCreateView, PhotoEditView
from users.models import UserProfile
import factory
import faker
import os


fake = faker.Faker()


class UserFactory(factory.django.DjangoModelFactory):
    """creates a user for testing"""

    class Meta:
        model = UserProfile

    username = factory.Faker('user_name')
    email = factory.Faker('email')


class PhotoFactory(factory.django.DjangoModelFactory):
    """create fake photos for testing"""
    
    class Meta:
        model = Photo

    image = SimpleUploadedFile('test.jpg', b'file_content', content_type='image/jpg')
    location = factory.Faker('word')
    description = factory.Faker('text')
    date_uploaded = factory.Faker('date')
    date_modified = factory.Faker('date')
    date_published = factory.Faker('date')
    # published = factory.Faker('random_element', elements=[
    #     ('PRIVATE', 'Private'),
    #     ('SHARED', 'Shared'),
    #     ('PUBLIC', 'Public'),
    # ])


# DO
# eliminate unneccessary stuff
class PhotoFormsTest(TestCase):
    """test photo forms"""

    @classmethod
    def setUp(self):
        super(TestCase, self)

        user = UserProfile(username='testing',
                    email='testing@testing.com')
        user.save()
        self.user = user
        self.client = Client()

        photo = PhotoFactory.build()
        photo.user_id = self.user.id
        photo.save()
        self.photo = photo

        self.request = RequestFactory()

    @classmethod
    def tearDown(self):
        User.objects.all().delete()
        Photo.objects.all().delete()

        super(TestCase, self)
