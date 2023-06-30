from django.test import TestCase
from django.urls import reverse

from blog.models import Comment
from .set_up_test_data import SetUpTestData


class CommentModelTest(TestCase):
    @classmethod
    def setUp(cls):
        cls.test_data = SetUpTestData()

    def test_comment_str_representation(self):
        comments = Comment.objects.all()
        for comment in comments:
            self.assertEqual(str(comment), comment.content)

    def test_comment_get_absolute_url(self):
        # TODO: Uncomment this test when comment-detail view is implemented
        # comments = Comment.objects.all()
        # for comment in comments:
        #     self.assertEqual(comment.get_absolute_url(), reverse('comment-detail', args=[str(comment.pk)]))
        pass

    def test_comment_get_edit_url(self):
        # TODO: Uncomment this test when comment-edit view is implemented
        # comments = Comment.objects.all()
        # for comment in comments:
        #     self.assertEqual(comment.get_edit_url(), reverse('comment-edit', args=[str(comment.pk)]))
        pass

    def test_comment_model_permissions(self):
        comments = Comment.objects.all()
        for comment in comments:
            self.assertEqual(comment._meta.permissions, (
                ("can_approve", "Can approve comments"),
                ("can_edit", "Can edit comments"),
                ("can_delete", "Can delete comments"),
            ))

    def test_comment_model_ordering(self):
        comments = Comment.objects.all()
        for comment in comments:
            self.assertEqual(comment._meta.ordering, ['created_at'])
