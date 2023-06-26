from django.db import models


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
