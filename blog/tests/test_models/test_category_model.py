from django.test import TestCase

from blog.models import Category
from blog.tests.utils.set_up_test_data import SetUpTestData


class CategoryModelTest(TestCase):
    @classmethod
    def setUp(cls):
        cls.test_data = SetUpTestData()

    def test_category_string_representation(self):
        categories = Category.objects.all()
        for category in categories:
            self.assertEqual(str(category), category.name)

    def test_category_get_absolute_url(self):
        # TODO: Uncomment this test after adding category-detail url
        # categories = Category.objects.all()
        # for category in categories:
        #     self.assertEqual(category.get_absolute_url(), reverse('category-detail', args=[str(category.pk)]))
        pass
