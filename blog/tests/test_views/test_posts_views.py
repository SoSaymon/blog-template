from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth import get_user_model
from blog.models import Post, Category
from blog.forms import CommentForm
from blog.tests.utils.set_up_test_data import SetUpTestData


class PostListViewTest(TestCase):
    @classmethod
    def setUp(cls):
        cls.client = Client()
        cls.testdata = SetUpTestData()

    def test_post_list_view(self):
        response = self.client.get(reverse('posts'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_list.html')

        posts = response.context['posts']
        self.assertEqual(len(posts), len(self.testdata.post_data))
        for post in posts:
            self.assertIn(post, posts)


User = get_user_model()


class PostDetailViewTest(TestCase):
    @classmethod
    def setUp(cls):
        cls.client = Client()
        cls.user = User.objects.create_user(
            username='test_user',
            password='test_password',
            email='test@example.com',
            role='author',
        )

        cls.post = Post.objects.create(
            title='Test post title',
            content='Test post content',
            author=cls.user,
            category=Category.objects.create(name='Test category'),
        )

    def test_post_detail_view(self):
        url = reverse('post-detail', kwargs={'pk': self.post.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/post_detail.html')

        post = response.context['post']
        self.assertEqual(post, self.post)

    def test_post_detail_view_with_comment(self):
        self.client.login(username='test_user', password='test_password')

        url = reverse('post-detail', kwargs={'pk': self.post.pk})
        response = self.client.get(url)

        comments = response.context['comments']
        self.assertEqual(len(comments), 0)

        comment_form = response.context['comment_form']
        self.assertIsInstance(comment_form, CommentForm)
