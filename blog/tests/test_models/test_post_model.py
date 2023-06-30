from django.test import TestCase
from django.urls import reverse

from blog.models import Post
from .set_up_test_data import SetUpTestData


class PostModelTest(TestCase):
    @classmethod
    def setUp(cls):
        cls.test_data = SetUpTestData()

    def test_post_model_str_representation(self):
        posts = Post.objects.all()
        for post in posts:
            self.assertEqual(str(post), post.title)

    def test_post_model_get_absolute_url(self):
        posts = Post.objects.all()
        for post in posts:
            self.assertEqual(post.get_absolute_url(), reverse('post-detail', args=[str(post.id)]))

    def test_post_model_permissions(self):
        posts = Post.objects.all()
        for post in posts:
            self.assertEqual(post._meta.permissions, (
                ("can_publish", "Can publish posts"),
                ("can_edit", "Can edit posts"),
                ("can_delete", "Can delete posts"),
            ))

    def test_post_model_ordering(self):
        posts = Post.objects.all()
        for post in posts:
            self.assertEqual(post._meta.ordering, ['-updated_at'])
