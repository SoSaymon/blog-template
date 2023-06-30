from django.contrib.auth.models import AnonymousUser
from django.test import TestCase, RequestFactory
from django.urls import reverse

from blog.models import User
from blog.views import ProfileView, EditProfileView


class ProfileViewTest(TestCase):
    @classmethod
    def setUp(cls):
        cls.factory = RequestFactory()
        cls.user = User.objects.create_user(
            username='test_user',
            password='test_password',
            email='test@example.com',
            role='author',
            is_active=True
        )

    def test_profile_view_authenticated_user(self):
        url = reverse('profile')
        request = self.factory.get(url)
        request.user = self.user

        response = ProfileView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<title>Profile test_user</title>', response.content)

    def test_profile_view_anonymous_user(self):
        url = reverse('profile')
        request = self.factory.get(url)
        request.user = AnonymousUser()

        response = ProfileView.as_view()(request)
        self.assertEqual(response.status_code, 302)


class EditProfileViewTest(TestCase):
    @classmethod
    def setUp(cls):
        cls.factory = RequestFactory()
        cls.user = User.objects.create_user(
            username='test_user',
            password='test_password',
            email='test@example.com',
            role='author',
        )

    def test_edit_profile_view_authenticated_user(self):
        url = reverse('edit-profile')
        request = self.factory.get(url)
        request.user = self.user

        response = EditProfileView.as_view()(request)
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<title>Edit profile</title>', response.content)
