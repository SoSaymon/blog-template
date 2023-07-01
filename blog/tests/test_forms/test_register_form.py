from django.contrib.auth import get_user_model
from django.test import TestCase
from blog.forms import RegistrationForm


class RegistrationFormTest(TestCase):
    @classmethod
    def setUp(cls):
        cls.User = get_user_model()

    def test_valid_form(self):
        form_data = RegistrationForm(data={
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
        })
        self.assertTrue(form_data.is_valid())

    def test_empty_form(self):
        form_data = RegistrationForm(data={})
        self.assertFalse(form_data.is_valid())
        self.assertTrue(form_data.has_error('username', code='required'))
        self.assertTrue(form_data.has_error('email', code='required'))
        self.assertTrue(form_data.has_error('password1', code='required'))
        self.assertTrue(form_data.has_error('password2', code='required'))

    def test_username_already_exists(self):
        self.User.objects.create_user(
            username='testuser',
            email='test@example.com',
            role='author',
            bio='test bio',
            is_staff=True,
        )
        form_data = RegistrationForm(data={
            'username': 'testuser',
            'email': 'test2@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
        })
        self.assertFalse(form_data.is_valid())
        self.assertTrue(form_data.has_error('username'))
        self.assertTrue('Username already exists' in form_data.errors['username'])

    def test_email_already_exists(self):
        self.User.objects.create_user(
            username='testuser',
            email='test@example.com',
            role='author',
            bio='test bio',
            is_staff=True,
        )
        form_data = RegistrationForm(data={
            'username': 'testuser2',
            'email': 'test@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
        })
        self.assertFalse(form_data.is_valid())
        self.assertTrue(form_data.has_error('email'))
        self.assertTrue('Email already exists' in form_data.errors['email'])

    def test_passwords_dont_match(self):
        form_data = RegistrationForm(data={
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword2',
        })
        self.assertFalse(form_data.is_valid())
        self.assertTrue(form_data.has_error('password2'))



