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