from django.test import TestCase
from django.urls import reverse

from blog.models import Tag
from .set_up_test_data import SetUpTestData


class TagModelTest(TestCase):
    @classmethod
    def setUp(cls):
        cls.test_data = SetUpTestData()

    def test_tag_string_representation(self):
        tags = Tag.objects.all()
        for tag in tags:
            self.assertEqual(str(tag), tag.name)

    def test_tag_get_absolute_url(self):
        # TODO: Uncomment this test after adding tag-detail url
        # tags = Tag.objects.all()
        # for tag in tags:
        #     self.assertEqual(tag.get_absolute_url(), reverse('tag-detail', args=[str(tag.pk)]))
        pass
