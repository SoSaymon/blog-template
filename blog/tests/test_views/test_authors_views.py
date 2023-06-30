from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.urls import reverse

from blog.tests.utils.set_up_test_data import SetUpTestData


class AuthorListViewTest(TestCase):
    NUMBER_OF_UNIQUE_AUTHORS = 1

    @classmethod
    def setUp(cls):
        cls.client = Client()
        cls.test_data = SetUpTestData()

    def test_author_list_view(self):
        response = self.client.get(reverse('authors'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/author_list.html')

        authors = response.context['authors']
        self.assertEqual(len(authors), self.NUMBER_OF_UNIQUE_AUTHORS)


User = get_user_model()


class AuthorDetailViewTest(TestCase):
    @classmethod
    def setUp(cls):
        cls.client = Client()
        cls.user = User.objects.create_user(
            username='test_user',
            password='test_password',
            email='test@example.com',
            role='author',
        )

    def test_author_detail_view(self):
        url = reverse('author-detail', kwargs={'pk': self.user.pk})
        response = self.client.get(url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'blog/author_detail.html')

        author = response.context['author']
        self.assertEqual(author, self.user)
