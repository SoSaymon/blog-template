from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
from django.db import models
from django.urls import reverse


class CustomUserManager(UserManager):
    def _create_user(self, username, email, password, **extra_fields):
        if not username:
            raise ValueError('The given username must be set')

        if not email:
            raise ValueError('The given email must be set')

        email = self.normalize_email(email)
        user = self.model(username=username, email=email, **extra_fields)
        user.set_password(password)

        user.save(using=self._db)

        return user

    def create_user(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)

        return self._create_user(username, email, password, **extra_fields)

    def create_superuser(self, username, email=None, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
        extra_fields.setdefault('is_active', True)
        extra_fields.setdefault('role', 'admin')

        return self._create_user(username, email, password, **extra_fields)


class User(AbstractBaseUser, PermissionsMixin):
    username = models.CharField(max_length=150, unique=True, help_text='Your username')
    email = models.EmailField(max_length=150, unique=True, help_text='Your email address')
    bio = models.TextField(max_length=500, blank=True, help_text='Your bio')

    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)

    created_at = models.DateTimeField(auto_now_add=True)
    last_login = models.DateTimeField(auto_now=True)

    USERNAME_FIELD = 'email'
    EMAIL_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    ROLES = (
        ('user', 'User'),
        ('moderator', 'Moderator'),
        ('author', 'Author'),
        ('admin', 'Admin'),
    )

    role = models.CharField(max_length=10, choices=ROLES, default='user')

    objects = CustomUserManager()

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
        ordering = ['-created_at']

    def __str__(self):
        return self.username or self.email.split('@')[0]

    def get_absolute_url(self):
        if self.role == 'author':
            return reverse('author-detail', args=[str(self.pk)])
        else:
            # TODO: Add user detail view for admins and moderators only
            pass

    # SETTERS
    def set_username(self, username):
        self.username = username
        self.save()

    def set_email(self, email):
        self.email = email
        self.save()

    def set_bio(self, bio):
        self.bio = bio
        self.save()

    def set_role(self, role):
        self.role = role
        self.save()

    def set_is_staff(self, is_staff):
        self.is_staff = is_staff
        self.save()

    def set_is_superuser(self, is_superuser):
        self.is_superuser = is_superuser
        self.save()

    def set_is_active(self, is_active):
        self.is_active = is_active
        self.save()

    # GETTERS
    def get_username(self):
        return self.username

    def get_email(self):
        return self.email

    def get_bio(self):
        return self.bio

    def get_role(self):
        return self.role

    def get_is_staff(self):
        return self.is_staff

    def get_is_superuser(self):
        return self.is_superuser

    def get_is_active(self):
        return self.is_active

    def get_created_at(self):
        return self.created_at

    def get_last_login(self):
        return self.last_login

    # METHODS
    def is_admin(self):
        return True if self.role == 'admin' else False

    def is_moderator(self):
        return True if self.role == 'moderator' else False

    def is_author(self):
        return True if self.role == 'author' else False

    def is_user(self):
        return True if self.role == 'user' else False
