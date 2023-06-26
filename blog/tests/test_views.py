from django.test import TestCase
from django.urls import reverse

from blog.models import Post, Category, Tag, Comment, User
from .set_up_test_data import SetUpTestData


class TestIndexView(TestCase):
    test_data = SetUpTestData()

    @classmethod
    def setUp(cls):
        td = cls.test_data

        td.create_users(td, td.usernames)
        td.create_tags(td, td.tags)
        td.create_categories(td, td.categories)
        td.create_posts(td, td.posts)
        td.create_comments(td, td.comments)

    def test_index_view(self):
        response = self.client.get('/blog/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'index.html')

        # # test context
        self.assertIn('posts', response.context)
        self.assertEqual(len(response.context['posts']), self.test_data.num_of_posts)


class TestPostListView(TestCase):
    test_data = SetUpTestData()

    @classmethod
    def setUp(cls):
        td = cls.test_data

        td.create_users(td, td.usernames)
        td.create_tags(td, td.tags)
        td.create_categories(td, td.categories)
        td.create_posts(td, td.posts)
        td.create_comments(td, td.comments)

    def test_post_list_view(self):
        response = self.client.get('/blog/posts/')
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_list.html')

        # # test context
        self.assertIn('posts', response.context)
        self.assertEqual(len(response.context['posts']), self.test_data.num_of_posts)


class TestPostDetailView(TestCase):
    test_data = SetUpTestData()

    @classmethod
    def setUp(cls):
        td = cls.test_data

        td.create_users(td, td.usernames)
        td.create_tags(td, td.tags)
        td.create_categories(td, td.categories)
        td.create_posts(td, td.posts)
        td.create_comments(td, td.comments)

    def test_post_detail_view(self):
        posts = Post.objects.all()

        for post in posts:
            url = reverse('post-detail', kwargs={'pk': post.pk})
            response = self.client.get(url)
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, 'blog/post_detail.html')

            # # test context
            self.assertIn('post', response.context)
            self.assertEqual(response.context['post'], post)
