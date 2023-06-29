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

    # SETTERS
    def set_content(self, content):
        self.content = content
        self.save()

    def set_approved(self, approved):
        self.approved = approved
        self.save()

    # GETTERS
    def get_content(self):
        return self.content

    def get_approved(self):
        return self.approved

    def get_post(self):
        return self.post

    def get_author(self):
        return self.author

    def get_created_at(self):
        return self.created_at

    def get_updated_at(self):
        return self.updated_at

    def get_absolute_url(self):
        return reverse('comment-detail', args=[str(self.pk)])

    def get_edit_url(self):
        return reverse('comment-edit', args=[str(self.pk)])

    @staticmethod
    def get_all_author_comments(author):
        return Comment.objects.filter(author=author)
