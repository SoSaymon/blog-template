from django.db import models
from django.urls import reverse


class Post(models.Model):
    title = models.CharField(max_length=100, help_text='Post title')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    author = models.ForeignKey('User', on_delete=models.CASCADE, help_text='Post author')
    tags = models.ManyToManyField('Tag', blank=True, help_text='Post tags')
    category = models.ForeignKey('Category', on_delete=models.SET_NULL, null=True, blank=True, default='Uncategorized',
                                 help_text='Post category')

    class Meta:
        ordering = ['-updated_at']
        permissions = (
            ("can_publish", "Can publish posts"),
            ("can_edit", "Can edit posts"),
            ("can_delete", "Can delete posts"),

        )

    def __str__(self):
        return self.title

    def display_tags(self):
        return ', '.join(tag.name for tag in self.tags.all()[:3])

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.id)])


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


class Tag(models.Model):
    name = models.CharField(max_length=100, help_text='Tag name')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag-detail', args=[str(self.id)])


class Category(models.Model):
    name = models.CharField(max_length=100, help_text='Category name')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category-detail', args=[str(self.id)])


class Comment(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey('User', on_delete=models.CASCADE, related_name='comments')
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    approved = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_at']
        permissions = (
            ("can_approve", "Can approve comments"),
            ("can_edit", "Can edit comments"),
            ("can_delete", "Can delete comments"),
        )
        verbose_name = 'Comment'
        verbose_name_plural = 'Comments'

    def __str__(self):
        return self.content

    def approve(self):
        self.approved = True
        self.save()

    def get_absolute_url(self):
        return reverse('post-detail', args=[str(self.post.id)])
