from django.test import TestCase
from django.urls import reverse

from blog.models import User
from .set_up_test_data import SetUpTestData


class UserModelTest(TestCase):
    @classmethod
    def setUp(cls):
        cls.test_data = SetUpTestData()

    def test_user_string_representation(self):
        users = User.objects.all()
        for user in users:
            self.assertEqual(str(user), user.username or user.email.split('@')[0])

    def test_user_get_absolute_url(self):
        users = User.objects.all()
        for user in users:
            if user.role == 'author':
                self.assertEqual(user.get_absolute_url(), reverse('author-detail', args=[str(user.pk)]))
            else:
                pass

    def test_user_is_role_methods(self):
        users = User.objects.all()
        for user in users:
            if user.role == 'user':
                self.assertTrue(user.is_user())
                self.assertFalse(user.is_moderator())
                self.assertFalse(user.is_author())
                self.assertFalse(user.is_admin())
            elif user.role == 'moderator':
                self.assertFalse(user.is_user())
                self.assertTrue(user.is_moderator())
                self.assertFalse(user.is_author())
                self.assertFalse(user.is_admin())
            elif user.role == 'author':
                self.assertFalse(user.is_user())
                self.assertFalse(user.is_moderator())
                self.assertTrue(user.is_author())
                self.assertFalse(user.is_admin())
            elif user.role == 'admin':
                self.assertFalse(user.is_user())
                self.assertFalse(user.is_moderator())
                self.assertFalse(user.is_author())
                self.assertTrue(user.is_admin())
