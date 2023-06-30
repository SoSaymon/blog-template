from django.test import TestCase, Client
from django.urls import reverse

from blog.models import Post
from blog.tests.utils.set_up_test_data import SetUpTestData


class IndexViewTest(TestCase):
    @classmethod
    def setUp(cls):
        cls.client = Client()
        cls.set_up_test_data = SetUpTestData()

    def test_index_view(self):
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

        posts = response.context['posts']
        self.assertEqual(len(posts), 4)
        self.assertEqual(posts[0].title, 'Test post 4')
        self.assertEqual(posts[1].title, 'Test post 3')
        self.assertEqual(posts[2].title, 'Test post 2')
        self.assertEqual(posts[3].title, 'Test post 1')

        self.assertGreater(posts[0].created_at, posts[1].created_at)
        self.assertGreater(posts[1].created_at, posts[2].created_at)
        self.assertGreater(posts[2].created_at, posts[3].created_at)

    def test_index_view_with_no_posts(self):
        Post.objects.all().delete()
        response = self.client.get(reverse('index'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

        posts = response.context['posts']
        self.assertEqual(len(posts), 0)
