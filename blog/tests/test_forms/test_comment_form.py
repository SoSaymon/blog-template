from django.test import TestCase
from blog.forms import CommentForm


class CommentFormTest(TestCase):
    def test_valid_form(self):
        form_data = {'content': 'This is a test comment'}
        form = CommentForm(data=form_data)
        self.assertTrue(form.is_valid())

    def test_empty_form(self):
        form_data = {}
        form = CommentForm(data=form_data)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error('content', code='required'))
