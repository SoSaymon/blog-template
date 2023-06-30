from django.contrib.auth import get_user_model
from django.test import TestCase
from blog.forms import EditProfileForm

User = get_user_model()


class EditProfileFormTest(TestCase):
    @classmethod
    def setUp(cls):
        cls.user = User.objects.create_user(
            username='testuser',
            email='testuser@example.com',
            bio='test bio',
            role='author',
            is_staff=True,
            is_superuser=False,
            is_active=True,
        )

        cls.user2 = User.objects.create_user(
            username='testuser2',
            email='testuser2@example.com',
            bio='test bio',
            role='author',
            is_staff=True,
            is_superuser=False,
            is_active=True,
        )

    def test_valid_form(self):
        form_data = {
            'username': 'newusername',
            'email': 'newemail@example.com',
            'bio': 'new bio',
        }
        form = EditProfileForm(data=form_data, instance=self.user)
        self.assertTrue(form.is_valid())

    def test_empty_form(self):
        form_data = {}
        form = EditProfileForm(data=form_data, instance=self.user)
        self.assertFalse(form.is_valid())
        self.assertTrue(form.has_error('username', code='required'))
        self.assertTrue(form.has_error('email', code='required'))

    def test_username_already_exists(self):
        form_data = {
            'username': 'testuser',
            'email': 'testuser2@example.com',
            'bio': 'new bio',
        }
        form = EditProfileForm(data=form_data, instance=self.user2)
        self.assertEqual(len(form.errors), 1)
        self.assertTrue('username' in form.errors)
        self.assertTrue('Username already exists' in form.errors['username'])

    def test_email_already_exists(self):
        form_data = {
            'username': 'testuser2',
            'email': 'testuser@example.com',
            'bio': 'new bio',
        }
        form = EditProfileForm(data=form_data, instance=self.user2)
        self.assertEqual(len(form.errors), 1)
        self.assertTrue('email' in form.errors)
        self.assertTrue('Email already exists' in form.errors['email'])

    def test_username_and_email_already_exists(self):
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'bio': 'new bio',
        }
        form = EditProfileForm(data=form_data, instance=self.user2)
        self.assertEqual(len(form.errors), 2)
        self.assertTrue('username' in form.errors)
        self.assertTrue('Username already exists' in form.errors['username'])
        self.assertTrue('email' in form.errors)
        self.assertTrue('Email already exists' in form.errors['email'])

    def test_username_and_email_already_exists_with_same_user(self):
        form_data = {
            'username': 'testuser',
            'email': 'testuser@example.com',
            'bio': 'new bio',
        }
        form = EditProfileForm(data=form_data, instance=self.user)
        self.assertEqual(len(form.errors), 0)
        self.assertFalse('username' in form.errors)
        self.assertFalse('email' in form.errors)

    def test_save_form(self):
        form_data = {
            'username': 'newusername',
            'email': 'newemail@example.com',
            'bio': 'This is my new bio.',
        }
        form = EditProfileForm(data=form_data, instance=self.user)
        self.assertTrue(form.is_valid())
        saved_user = form.save()
        self.assertEqual(saved_user.username, 'newusername')
        self.assertEqual(saved_user.email, 'newemail@example.com')
        self.assertEqual(saved_user.bio, 'This is my new bio.')