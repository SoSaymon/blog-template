from django.db import models
from django.urls import reverse


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

    def get_absolute_url(self):
        return reverse('comment-detail', args=[str(self.pk)])

    def get_edit_url(self):
        return reverse('comment-edit', args=[str(self.pk)])
