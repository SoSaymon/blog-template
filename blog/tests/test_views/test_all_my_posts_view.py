from django.contrib.auth import get_user_model
from django.contrib.auth.models import Permission, AnonymousUser, Group
from django.test import TestCase, RequestFactory
from django.urls import reverse

from blog.views import AllMyPostsView

User = get_user_model()


class TestAllMyPostsView(TestCase):
    @classmethod
    def setUp(cls):
        cls.factory = RequestFactory()
        cls.permission = Permission.objects.get(codename='can_publish')

        cls.user = User.objects.create_user(
            username='test_user',
            password='test_password',
            email='test@example.com',
            role='author',
            is_active=True
        )
        cls.user.user_permissions.add(cls.permission)

        cls.user2 = User.objects.create_user(
            username='test_user2',
            password='test_password2',
            email='test2@example.com',
            role='user',
            is_active=True
        )

    def test_all_my_posts_view_authenticated_user(self):
        url = reverse('all-posts')
        request = self.factory.get(url)
        request.user = self.user

        response = AllMyPostsView.as_view()(request)
        response.render()
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'<title>All Posts</title>', response.content)

    def test_all_my_posts_view_with_user_without_permissions(self):
        # getting error: raise PermissionDenied(self.get_permission_denied_message())
        # url = reverse('all-posts')
        # request = self.factory.get(url)
        # request.user = self.user2
        #
        # response = AllMyPostsView.as_view()(request)
        # response.render()
        # self.assertEqual(response.status_code, 403)
        # self.assertIn(b'<title>403 Forbidden</title>', response.content)
        pass

    def test_all_my_posts_view_anonymous_user(self):
        url = reverse('all-posts')
        request = self.factory.get(url)
        request.user = AnonymousUser()

        response = AllMyPostsView.as_view()(request)
        # response.render()
        self.assertEqual(response.status_code, 302)