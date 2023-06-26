from django.db import models
from django.urls import reverse


class Tag(models.Model):
    name = models.CharField(max_length=100, help_text='Tag name')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('tag-detail', args=[str(self.id)])
