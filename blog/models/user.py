from django.db import models
from django.urls import reverse


class User(models.Model):
    name = models.CharField(max_length=100, help_text='Username')
    email = models.EmailField(max_length=100, help_text='User email')
    bio = models.TextField(blank=True, help_text='User bio')
    created_at = models.DateTimeField(auto_now_add=True)

    ROLES = (
        ('admin', 'Admin'),
        ('author', 'Author'),
        ('moderator', 'Moderator'),
        ('user', 'User'),
    )

    role = models.CharField(max_length=10, choices=ROLES, default='user', help_text='User role')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('user-detail', args=[str(self.id)])

    def get_role(self):
        return self.role

    def get_role_verbose(self):
        return dict(User.ROLES)[self.role]

    def get_role_verbose_plural(self):
        return dict(User.ROLES)[self.role] + 's'

    def get_posts(self):
        return Post.objects.filter(author=self.id)